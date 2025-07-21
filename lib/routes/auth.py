"""
Auth routes for handling authentication with AWS Cognito and federated identity providers like Google.
"""
import base64
import secrets
from typing import Any, Dict, Tuple, Union
from urllib import parse

import requests
from flask import Response, jsonify, redirect, request, session, url_for
from werkzeug.wrappers.response import Response as BaseResponse

from lib.services.user_service import UserService
from settings import (CLIENT_ID, CLIENT_SECRET, COGNITO_DOMAIN, LOGOUT_URI,
                      REDIRECT_URI, logger)


def cognito_login_route() -> Union[Tuple[Response, int], BaseResponse]:
    # Handle error returned from Cognito
    error = request.args.get('error')
    error_description = request.args.get('error_description')

    if error:
        decoded_description = parse.unquote(error_description or '')
        logger.warning("Cognito auth error: %s - %s", error, decoded_description)
        return jsonify({'error': error, 'description': decoded_description}), 400

    code = request.args.get('code')

    token_url = f'https://{COGNITO_DOMAIN}/oauth2/token'

    auth_string = f'{CLIENT_ID}:{CLIENT_SECRET}'
    auth_header = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {auth_header}'
    }

    body = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }

    response = requests.post(token_url, headers=headers, data=body)

    if response.status_code != 200:
        logger.error("Token exchange failed: %s - %s", response.status_code, response.text)
        return jsonify({'status': response.status_code, 'message': response.text}), 400

    if response.status_code == 200:
        tokens = response.json()

        user_info_url = f'https://{COGNITO_DOMAIN}/oauth2/userInfo'
        headers = {
            'Authorization': f'Bearer {tokens["access_token"]}'
        }

        user_response = requests.get(user_info_url, headers=headers)

        if user_response.status_code != 200:
            logger.error("Failed to fetch user info: %s - %s", user_response.status_code, user_response.text)
            return jsonify({'status': user_response.status_code, 'message': user_response.text}), 400

        if user_response.status_code == 200:
            user_info = user_response.json()
            email = user_info.get('email')
            name = user_info.get('name', '')
            first_name, last_name = '', ''
            if name:
                parts = name.split(' ', 1)
                first_name = parts[0]
                last_name = parts[1] if len(parts) > 1 else ''
            username = email.split('@')[0] if email else None
            if not email or not username:
                logger.error("Missing email or username in federated login response")
                return jsonify({'error': 'Missing email or username from identity provider'}), 400

            # Get role from query param, default to 'patient'
            role_from_query = request.args.get('role', 'patient')

            user_service = UserService()
            user_service.connect()
            try:
                user = user_service.get_user_by_email(email)
                if not user:
                    # Create user with a random password (not used for federated login)
                    random_password = secrets.token_urlsafe(16)
                    success, message, user = user_service.create_user(
                        username=username,
                        email=email,
                        password=random_password,
                        first_name=first_name,
                        last_name=last_name,
                        role=role_from_query
                    )
                    if not success or not user:
                        logger.error(f"Failed to create user from federated login: {message}")
                        return jsonify({'error': 'Failed to create user', 'message': message}), 500
                else:
                    # Optionally update user info if changed
                    updates: Dict[str, Any] = {}
                    if first_name and user.first_name != first_name:
                        updates['first_name'] = first_name
                    if last_name and user.last_name != last_name:
                        updates['last_name'] = last_name
                    if updates and user.id is not None:
                        user_service.update_user(str(user.id), updates)
                # Store user info in session (mimic other routes)
                session['user_id'] = user.id
                session['auth_token'] = None  # No local token for federated login, unless you want to create one
                return redirect(url_for('index'))
            except Exception as e:
                logger.error("Failed to create/update user in database: %s", e)
                session['user'] = user_info
                return redirect(url_for('index'))
            finally:
                user_service.close()

    return jsonify({'error': 'Unknown error occurred during authentication'}), 500


def auth_logout_route() -> BaseResponse:
    session.clear()

    logout_url = (
        f'https://{COGNITO_DOMAIN}/logout?'
        f'client_id={CLIENT_ID}&'
        f'logout_uri={parse.quote(LOGOUT_URI)}'
    )

    return redirect(logout_url)
