"""
This module contains the models for the metrics.

Metrics are KPIs that are tracked for a given date.

This is an abstract model that can be used to track any metric, whether that's patient lab results, patient health tracking KPIs, clinic management KPIs, etc.
"""
from typing import Dict, Any, List, Optional, Tuple


class Metric:
    def __init__(self, metric_name: str, metric_value: str, metric_unit: str, range: Optional[Tuple[float, float]] = None):
        self.metric_name = metric_name
        self.metric_value = metric_value
        self.metric_unit = metric_unit
        self.range = range
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'metric_name': self.metric_name,
            'metric_value': self.metric_value,
            'metric_unit': self.metric_unit,
            'range': self.range
        }

class MetricSet:
    def __init__(self, date: str, metrics: List[Metric]):
        self.date = date
        self.metrics = metrics

    def to_dict(self) -> Dict[str, Any]:
        return {
            'date': self.date,
            'metrics': [metric.to_dict() for metric in self.metrics]
        }
