import httpx
import base64
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

SHORTCODE = os.getenv("SHORTCODE")
PASSKEY = os.getenv("PASSKEY")

def generate_password(timestamp: str) -> str:
    """Generate M-Pesa password from shortcode, passkey, and timestamp"""
    data = f"{SHORTCODE}{PASSKEY}{timestamp}"
    password = base64.b64encode(data.encode()).decode()
    return password

def call_mpesa_stk_push( access_token: str, amount: float,phone_number: str) -> str:
     """ Call M-Pesa STK Push endpoint Returns: CheckoutRequestID """
     # Generate timestamp
     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

     # Generate password
     password = generate_password(timestamp)

     # Prepare request body
     payload = {
        "BusinessShortCode": SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": int(amount),  # M-Pesa expects integer
        "PartyA": phone_number,
        "PartyB": SHORTCODE,
        "PhoneNumber": phone_number,
        "CallbackURL": "https://herring-trial-endurable.ngrok-free.dev/payments/callback",
        "AccountReference": "Payment",
        "TransactionDesc": "M-Pesa payment"
     }

     # Call M-Pesa
     response = httpx.post(
          "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
          json=payload,
          headers={
               "Authorization": f"Bearer {access_token}",
               "Content-Type" : "application/json"
          }
     )

     # Check response
     if response.status_code != 200 :
          raise Exception(f"STK Push failed: {response.text}")

     # Extract CheckoutRequestID
     checkout_id = response.json()["CheckoutRequestID"]
     return checkout_id




