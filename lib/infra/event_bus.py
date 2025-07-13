"""
In-process event bus for domain events
"""
from collections import defaultdict
from typing import Any

from settings import logger


class EventBus:
    """
    Simple in-process event bus for domain events.
    
    This provides a lightweight way to decouple domain logic from
    webhook delivery and other side effects.
    """
    
    def __init__(self):
        self._subscribers = defaultdict(list)
    
    def subscribe(self, event_type, handler) -> None:
        """
        Subscribe a handler function to an event type.
        
        :param event_type: The type of event to subscribe to
        :param handler: Function to call when event is published
        """
        self._subscribers[event_type].append(handler)
        logger.debug(f"Subscribed handler {handler.__name__} to event {event_type.__name__}")
    
    def publish(self, event: Any) -> None:
        """
        Publish an event to all subscribed handlers.
        
        :param event: The event object to publish
        """
        event_type = type(event)
        handlers = self._subscribers[event_type]
        
        logger.debug(f"Publishing {event_type.__name__} to {len(handlers)} handlers")
        
        for handler in handlers:
            try:
                handler(event)
            except Exception as e:
                logger.error(f"Error in event handler {handler.__name__}: {e}")
                # Don't let one handler failure stop others from executing
                continue


# Global event bus instance
event_bus = EventBus()
