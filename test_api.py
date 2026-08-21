import httpx

# Make a GET request to a test API
# response = httpx.get("https://jsonplaceholder.typicode.com/posts/1")

# Make a POST request 
response = httpx.post(
    "https://jsonplaceholder.typicode.com/posts",
     json = {
          "title" : "Payment for order #123",
          "body" : "Amount: 100, Phone: 2541234567",
          "userId" : 1
          }
    )

# Print the status code
print(f"Status code : {response.status_code}")

# print the response body (as JSON)
print(f"Response : {response.json()}")