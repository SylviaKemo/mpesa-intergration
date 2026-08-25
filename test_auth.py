from mpesa_auth import get_mpesa_access_token

try:
    token = get_mpesa_access_token()
    print(f"Success! Token: {token}")
except Exception as e:
    print(f"Error: {e}")