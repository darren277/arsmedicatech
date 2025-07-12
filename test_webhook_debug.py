"""
Debug script to test webhook delivery
"""
import logging
from lib.tasks import deliver_webhooks
from lib.db.surreal import DbController
from lib.models.webhook_subscription import WebhookSubscription

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

print(f"[debug] WebhookSubscription class: {WebhookSubscription}")
import inspect
print(f"[debug] WebhookSubscription defined in: {inspect.getfile(WebhookSubscription)}")
print(f"[debug] id(WebhookSubscription.from_dict): {id(WebhookSubscription.from_dict)}")

def test_webhook_delivery():
    """Test webhook delivery with debug output"""
    print("🔍 Testing webhook delivery...")
    
    # First, let's check what webhook subscriptions exist
    db = DbController()
    try:
        db.connect()
        
        # Get all webhook subscriptions
        query = "SELECT * FROM webhook_subscription"
        results = db.query(query)
        
        print(f"📋 Found {len(results)} webhook subscription records")
        
        # Debug: Print raw results
        print("\n🔍 Raw results:")
        for i, result in enumerate(results):
            print(f"  Result {i}: {result}")
        
        subscriptions = []
        for i, result in enumerate(results):
            print(f"\n📄 Processing result {i}: {result}")
            print(f"    [debug] About to call from_dict for result {i}")
            try:
                subscription = WebhookSubscription.from_dict(result)
                subscriptions.append(subscription)
                print(f"    ✅ Parsed: {subscription.id}: {subscription.event_name} -> {subscription.target_url} (enabled: {subscription.enabled})")
            except Exception as e:
                print(f"    ❌ Failed to parse result: {e}")
        
        print(f"\n📊 Total parsed subscriptions: {len(subscriptions)}")
        
        if not subscriptions:
            print("❌ No webhook subscriptions found!")
            return
        
        # Direct test: try from_dict on the first record if available
        if results and results[0].get('result') and len(results[0]['result']) > 0:
            print("\n[direct test] Trying from_dict on the first record...")
            try:
                record = results[0]['result'][0]
                subscription = WebhookSubscription.from_dict(record)
                print(f"[direct test] ✅ Parsed: {subscription.id}: {subscription.event_name} -> {subscription.target_url} (enabled: {subscription.enabled})")
            except Exception as e:
                print(f"[direct test] ❌ Failed to parse record: {e}")
        
        # Test webhook delivery
        print("\n🚀 Testing webhook delivery...")
        deliver_webhooks('appointment.created', {
            'appointment_id': 'test:123',
            'patient_id': 'patient:456',
            'provider_id': 'provider:789',
            'test': True
        })
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    test_webhook_delivery() 