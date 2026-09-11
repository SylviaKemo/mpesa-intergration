from mpesa_auth import get_mpesa_access_token
from mpesa_stk_push import call_mpesa_stk_push, generate_password
from datetime import datetime
import os

try:
    # Step 1: Get access token
    print("Getting access token...")
    token = get_mpesa_access_token()
    print(f"✓ Token: {token[:20]}...")  # Show first 20 chars
    
    # Step 2: Check credentials are loaded
    SHORTCODE = os.getenv("SHORTCODE")
    PASSKEY = os.getenv("PASSKEY")
    print(f"✓ Shortcode: {SHORTCODE}")
    print(f"✓ Passkey: {PASSKEY[:10]}...")
    
    # Step 3: Generate password
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    password = generate_password(timestamp)
    print(f"✓ Timestamp: {timestamp}")
    print(f"✓ Password: {password[:20]}...")
    
    # Step 4: Call STK Push
    print("\nCalling STK Push...")
    checkout_id = call_mpesa_stk_push(
        access_token=token,
        amount=1,
        phone_number="254708374149"
    )
    print(f"✓ Success! CheckoutRequestID: {checkout_id}")
    
except Exception as e:
    print(f"✗ Error: {e}")