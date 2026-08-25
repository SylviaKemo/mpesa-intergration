import httpx
import base64
import os 
from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

def get_mpesa_access_token() -> str:
     """
    Get access token from M-Pesa Daraja API
    Returns: access_token string
    """
     # Create Basic Auth header
     credentials = f"{CONSUMER_KEY}:{CONSUMER_SECRET}"
     encoded = base64.b64encode(credentials.encode()).decode()

      # Call M-Pesa auth endpoint
     response = httpx.get(
         "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials",
         headers = {
            "Authorization" : f"Basic {encoded}"
         }
      )

      # Check if successful
     if response.status_code !=  200:
         raise Exception(f"Failed to get access token: {response.text}")

     # Extract and return token
     token = response.json()["access_token"]
     return token