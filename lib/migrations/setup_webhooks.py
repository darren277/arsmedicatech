"""
Migration script to set up webhook subscriptions table
"""
from lib.db.surreal import DbController
from settings import logger


def setup_webhook_subscriptions_table():
    """
    Set up the webhook_subscription table in SurrealDB
    """
    db = DbController()
    try:
        db.connect()
        
        # Create webhook_subscription table
        logger.info("Creating webhook_subscription table...")
        
        # Define the table schema
        schema_query = """
        DEFINE TABLE webhook_subscription SCHEMAFULL;
        
        DEFINE FIELD event_name ON webhook_subscription TYPE string;
        DEFINE FIELD target_url ON webhook_subscription TYPE string;
        DEFINE FIELD secret ON webhook_subscription TYPE string;
        DEFINE FIELD enabled ON webhook_subscription TYPE bool DEFAULT true;
        DEFINE FIELD created_at ON webhook_subscription TYPE datetime DEFAULT time::now();
        DEFINE FIELD updated_at ON webhook_subscription TYPE datetime DEFAULT time::now();
        
        DEFINE INDEX idx_event_name ON webhook_subscription COLUMNS event_name;
        DEFINE INDEX idx_enabled ON webhook_subscription COLUMNS enabled;
        DEFINE INDEX idx_created_at ON webhook_subscription COLUMNS created_at;
        """
        
        result = db.query(schema_query, {})
        logger.info(f"Schema creation result: {result}")
        
        # Create some sample webhook subscriptions for testing
        logger.info("Creating sample webhook subscriptions...")
        
        sample_subscriptions = [
            {
                "event_name": "appointment.created",
                "target_url": "https://webhook.site/your-unique-url",
                "secret": "your-secret-key-here",
                "enabled": True
            },
            {
                "event_name": "appointment.cancelled",
                "target_url": "https://webhook.site/your-unique-url",
                "secret": "your-secret-key-here",
                "enabled": True
            }
        ]
        
        for subscription in sample_subscriptions:
            result = db.create('webhook_subscription', subscription)
            if result:
                logger.info(f"Created sample subscription: {result.get('id')}")
            else:
                logger.error(f"Failed to create sample subscription: {subscription}")
        
        logger.info("Webhook subscriptions table setup completed successfully!")
        
    except Exception as e:
        logger.error(f"Error setting up webhook subscriptions table: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    setup_webhook_subscriptions_table() 