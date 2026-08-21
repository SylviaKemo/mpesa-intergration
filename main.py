import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")

print(consumer_key, consumer_secret)

all_payments = [
         {
            "amount" : 1000,
            "phone_number" : "254712345678",
            "status" : "pending"
         },
         {
            "amount": -250, 
            "phone_number": "354712345678",
            "status": "pending"
         },
         {
               "amount": 1500, 
                "phone_number": "254712345678",
                "status": "pending"   
         }
]

payment = {
    "amount" : 100,
"phone_number" : "254712345678",
"status" : "pending"
}

invalid_payment = {
    "amount": 150, 
    "phone_number": "712345678",
    "status": "pending"
}

broken_payment = {
       "amount" : 100
}

def validate_amount(amount : int) :
        return amount > 0 
    
def validate_phone_number (number : str) :
        return number.startswith("254")

def validate_payment (payment : dict):
       try :
            amount = payment["amount"]
            phone_number = payment["phone_number"]

            return validate_amount(amount) and validate_phone_number(phone_number) 
       except KeyError:
            return False
      
result = validate_payment(broken_payment)
print(result)

for payment in all_payments:
      result = validate_payment(payment)
      phone = payment["phone_number"]
      if result:
             print(f"Payment from {phone} is valid")
      else :
             print(f" Payment from {phone} is invalid")