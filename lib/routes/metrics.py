from flask import Blueprint, jsonify, request

from lib.services.auth_decorators import require_auth
from lib.services.metrics_service import (get_user_metric_set_by_date,
                                          get_user_metric_sets,
                                          save_user_metric_set,
                                          upsert_user_metric_set_by_date)

metrics_bp = Blueprint('metrics', __name__)


@metrics_bp.route('/api/users/<user_id>/metrics', methods=['POST'])
@require_auth
def post_user_metrics(user_id: str):
    data = request.get_json()
    date = data.get('date')
    metrics = data.get('metrics', [])
    if not date or not metrics:
        return jsonify({'error': 'Missing date or metrics'}), 400
    save_user_metric_set(user_id, date, metrics)
    return jsonify({'status': 'success'}), 201

@metrics_bp.route('/api/users/<user_id>/metrics', methods=['GET'])
@require_auth
def get_user_metrics(user_id: str):
    metric_sets = get_user_metric_sets(user_id)
    return jsonify({'metrics': metric_sets})

@metrics_bp.route('/api/metrics/user/<user_id>/date/<date>', methods=['GET'])
@require_auth
def get_user_metrics_by_date(user_id: str, date: str):
    metric_set = get_user_metric_set_by_date(user_id, date)
    return jsonify({'metrics': metric_set.get('metrics', [])})

@metrics_bp.route('/api/metrics/user/<user_id>/date/<date>', methods=['POST'])
@require_auth
def upsert_user_metrics_by_date(user_id: str, date: str):
    data = request.get_json()
    metrics = data.get('metrics', [])
    if not metrics:
        return jsonify({'error': 'Missing metrics'}), 400
    upsert_user_metric_set_by_date(user_id, date, metrics)
    return jsonify({'status': 'success'})
