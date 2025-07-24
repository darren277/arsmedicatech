"""
Uploads API Routes
"""
from typing import Tuple

import boto3  # type: ignore
from flask import Blueprint, Response, jsonify, request
from werkzeug.datastructures import FileStorage

from lib.data_types import UserID
from lib.models.upload import (FileType, Upload, UploadStatus, create_upload,
                               get_upload_by_id, get_uploads_by_user,
                               update_upload_status)
from lib.services.auth_decorators import get_current_user, require_auth
from lib.services.upload_service import process_upload_task
from settings import BUCKET_NAME, logger

uploads_bp = Blueprint('uploads', __name__)

@uploads_bp.route('/api/uploads', methods=['POST'])
@require_auth
def upload_file_route() -> Tuple[Response, int]:
    """
    Upload a file, create Upload record, upload to S3, trigger Celery if needed.
    """
    user = get_current_user()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401

    if 'file' not in request.files:
        return jsonify({"error": "No file part in request"}), 400
    file: FileStorage = request.files['file']
    filename = file.filename or ""
    if filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_type = Upload.get_file_type_from_extension(filename)
    uploader_id: UserID = UserID(user.user_id) if not isinstance(user.user_id, UserID) else user.user_id
    s3_key = Upload.generate_s3_key(uploader_id, filename)
    file_size = 0
    try:
        # Upload to S3
        s3 = boto3.client('s3')
        file.seek(0, 2)  # Seek to end to get size
        file_size = file.tell()
        file.seek(0)
        s3.upload_fileobj(file, BUCKET_NAME, s3_key)
        logger.info(f"Uploaded file to S3: {BUCKET_NAME}/{s3_key}")
    except Exception as e:
        logger.error(f"Failed to upload file to S3: {e}")
        return jsonify({"error": "Failed to upload file to S3"}), 500

    # Create Upload record
    upload = Upload(
        uploader=uploader_id,
        file_name=filename,
        file_path=s3_key,
        file_type=file_type,
        bucket_name=BUCKET_NAME,
        status=UploadStatus.PENDING,
        file_size=file_size,
        s3_key=s3_key,
    )
    upload_id = create_upload(upload)
    if not upload_id:
        return jsonify({"error": "Failed to create upload record"}), 500

    # Trigger Celery task if needed
    if file_type in (FileType.PDF, FileType.IMAGE, FileType.AUDIO):
        task = process_upload_task.apply_async(args=[upload_id, file_type.value, s3_key])  # type: ignore
        update_upload_status(upload_id, UploadStatus.PENDING, task_id=task.id)
    else:
        update_upload_status(upload_id, UploadStatus.COMPLETED)

    return jsonify({"id": upload_id, **upload.to_dict()}), 201

@uploads_bp.route('/api/uploads', methods=['GET'])
@require_auth
def list_uploads_route():
    """
    List uploads for the current user.
    """
    user = get_current_user()
    if not user:
        return jsonify({"error": "Unauthorized"}), 401
    uploader_id: UserID = UserID(user.user_id) if not isinstance(user.user_id, UserID) else user.user_id
    uploads = get_uploads_by_user(uploader_id)
    return jsonify(uploads), 200

@uploads_bp.route('/api/uploads/<upload_id>', methods=['GET'])
@require_auth
def get_upload_route(upload_id: str) -> Tuple[Response, int]:
    """
    Get details for a specific upload.
    """
    upload = get_upload_by_id(upload_id)
    if not upload:
        return jsonify({"error": "Upload not found"}), 404
    return jsonify(upload), 200
