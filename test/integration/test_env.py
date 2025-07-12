"""
Test environment variables
"""

import os

def test_env():
    """Test environment variables"""
    print("🔍 Testing Environment Variables")
    print("=" * 50)
    
    # Check ENCRYPTION_KEY
    encryption_key = os.getenv('ENCRYPTION_KEY')
    if encryption_key:
        print(f"✅ ENCRYPTION_KEY is set (length: {len(encryption_key)})")
        print(f"   First 10 chars: {encryption_key[:10]}...")
    else:
        print("❌ ENCRYPTION_KEY is not set")
        print("   Please set: export ENCRYPTION_KEY='your-secure-key-here'")
    
    # Check other environment variables
    print("\n📋 Other Environment Variables:")
    env_vars = [
        'SURREALDB_NAMESPACE',
        'SURREALDB_DATABASE', 
        'SURREALDB_HOST',
        'SURREALDB_PORT',
        'SURREALDB_USER',
        'SURREALDB_PASS'
    ]
    
    for var in env_vars:
        value = os.getenv(var)
        if value:
            print(f"   {var}: {value}")
        else:
            print(f"   {var}: Not set")

if __name__ == "__main__":
    test_env() 