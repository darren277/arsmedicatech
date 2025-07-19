"""
Service for handling user health metrics (KPI) persistence and retrieval using SurrealDB.
"""
from typing import Any, Dict, List

from lib.db.surreal import DbController
from lib.models.metrics import Metric, MetricSet

# Initialize DB controller (ensure connect is called once at startup)
db = DbController()
db.connect()

def save_user_metric_set(user_id: str, date: str, metrics: List[Dict[str, Any]]) -> None:
    """
    Save a metric set for a user for a given date.
    :param user_id: The user's ID
    :param date: The date for the metric set (ISO string)
    :param metrics: List of metric dicts
    """
    metric_objs = [Metric(**m) for m in metrics]
    metric_set = MetricSet(user_id=user_id, date=date, metrics=metric_objs)
    db.create('MetricSet', metric_set.to_dict())

def get_user_metric_sets(user_id: str) -> List[Dict[str, Any]]:
    """
    Retrieve all metric sets for a user.
    :param user_id: The user's ID
    :return: List of metric set dicts
    """
    results = db.query("SELECT * FROM MetricSet WHERE user_id = $user_id", {"user_id": user_id})

    # Convert RecordID to string
    for result in results:
        if 'id' in result:
            result['id'] = str(result['id'])

    return results

def get_user_metric_set_by_date(user_id: str, date: str) -> Dict[str, Any]:
    """
    Retrieve the metric set for a user on a specific date.
    :param user_id: The user's ID
    :param date: The date (ISO string)
    :return: Metric set dict or empty dict
    """
    results = db.query(
        "SELECT * FROM MetricSet WHERE user_id = $user_id AND date = $date",
        {"user_id": user_id, "date": date}
    )
    if results and 'result' in results[0]:
        result_list = results[0]['result']
        return result_list[0] if result_list else {}
    return results[0] if results else {}

def upsert_user_metric_set_by_date(user_id: str, date: str, metrics: List[Dict[str, Any]]) -> None:
    """
    Create or update the metric set for a user on a specific date.
    :param user_id: The user's ID
    :param date: The date (ISO string)
    :param metrics: List of metric dicts
    """
    existing = get_user_metric_set_by_date(user_id, date)
    metric_objs = [Metric(**m) for m in metrics]
    metric_set = MetricSet(user_id=user_id, date=date, metrics=metric_objs)
    if existing and existing.get('id'):
        db.update(f"MetricSet:{existing['id']}", metric_set.to_dict())
    else:
        db.create('MetricSet', metric_set.to_dict())
