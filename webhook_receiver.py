"""
Simple Webhook Receiver

This script creates a local HTTP server to receive and display webhooks.
Run this script and use http://localhost:8000/webhook as your webhook URL.
"""
from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Store received webhooks
received_webhooks = []

@app.route('/webhook', methods=['POST'])
def webhook():
    """Receive webhook POST requests"""
    try:
        # Get the webhook data
        data = request.get_json()
        headers = dict(request.headers)
        
        # Create webhook record
        webhook_record = {
            'timestamp': datetime.now().isoformat(),
            'headers': headers,
            'data': data,
            'method': request.method,
            'url': request.url
        }
        
        # Store the webhook
        received_webhooks.append(webhook_record)
        
        # Print webhook details
        print("\n" + "="*60)
        print(f"📨 WEBHOOK RECEIVED at {webhook_record['timestamp']}")
        print("="*60)
        print(f"Event: {data.get('event', 'Unknown')}")
        print(f"Delivery ID: {data.get('delivery_id', 'Unknown')}")
        print(f"Headers: {json.dumps(headers, indent=2)}")
        print(f"Data: {json.dumps(data, indent=2)}")
        print("="*60)
        
        # Return success
        return jsonify({"status": "success", "message": "Webhook received"}), 200
        
    except Exception as e:
        print(f"❌ Error processing webhook: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/webhooks', methods=['GET'])
def list_webhooks():
    """List all received webhooks"""
    return jsonify({
        "webhooks": received_webhooks,
        "count": len(received_webhooks)
    })

@app.route('/', methods=['GET'])
def home():
    """Home page with instructions"""
    return f"""
    <html>
    <head><title>Webhook Receiver</title></head>
    <body>
        <h1>🔗 Webhook Receiver</h1>
        <p>This server is ready to receive webhooks!</p>
        
        <h2>📊 Received Webhooks: {len(received_webhooks)}</h2>
        
        <h3>🔧 Usage:</h3>
        <ul>
            <li>Use <code>http://localhost:8000/webhook</code> as your webhook URL</li>
            <li>View all webhooks at <a href="/webhooks">/webhooks</a></li>
            <li>Webhooks will be displayed in the console</li>
        </ul>
        
        <h3>📋 Recent Webhooks:</h3>
        <ul>
            {''.join([f'<li>{w["timestamp"]} - {w["data"].get("event", "Unknown")}</li>' for w in received_webhooks[-5:]])}
        </ul>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("🚀 Starting Webhook Receiver Server")
    print("=" * 50)
    print("📡 Server will be available at: http://localhost:8000")
    print("🔗 Webhook endpoint: http://localhost:8000/webhook")
    print("📊 View webhooks at: http://localhost:8000/webhooks")
    print("=" * 50)
    print("⏳ Waiting for webhooks...")
    print()
    
    app.run(host='0.0.0.0', port=8000, debug=True) 