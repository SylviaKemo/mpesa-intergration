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


if payment["amount"] > 0 and payment["phone_number"].startswith("254"):
    print("Payment is valid")
else :
    print("Payment is invalid") 

def validate_payment(payment: dict) :
        return payment["amount"] > 0 and payment["phone_number"].startswith("254")
    

result = validate_payment(invalid_payment)

print(result)