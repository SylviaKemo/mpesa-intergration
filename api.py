payments_db = {}
next_payment_id = 1

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import validate_amount,validate_phone_number

def save_payment(amount: float, phone_number: str, status: str = "Pending") -> dict :
    global next_payment_id

    payment = {
        "id" : next_payment_id,
        "amount" : amount,
        "phone_number": phone_number,
        "status": status
    }

    payments_db[next_payment_id] = payment
    next_payment_id += 1

    return payment

# create the FASTAPI App
app = FastAPI()

# Define what data we expect from the customer
class PaymentRequest(BaseModel) :
    amount : float
    phone_number : str

# Define what we get back
class PaymentResponse(BaseModel) :
    status : str
    message : str

class PaymentDetail(BaseModel):
    id : int
    amount: float
    phone_number : str
    status : str

class UpdatePaymentDetails(BaseModel):
    status : str
    

# first endpoint
@app.post("/payment/stk-push")
def initiate_payment(request : PaymentRequest) -> PaymentResponse :
    if not validate_amount(request.amount) :
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")
    elif not validate_phone_number(request.phone_number):
        raise HTTPException(status_code=400, detail= "Invalid number" )
    else :
        #save the payment
        payment = save_payment(request.amount, request.phone_number)   

        return PaymentResponse(
            status = "Pending",
             message=f"Payment ID {payment['id']} created for {request.phone_number}"
        )

@app.get("/payment/{payment_id}")
def get_payment(payment_id : int) -> PaymentDetail :
      # Check if payment exists
    if payment_id not in payments_db:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    # Return the stored payment
    payment = payments_db[payment_id]
    return PaymentDetail(
        id=payment["id"],
        amount=payment["amount"],
        phone_number=payment["phone_number"],
        status=payment["status"]
    )

    
@app.get("/payments")
def list_payments (status: str = None ) -> list :
     # If no status specified, return all
  if status is None :
      return list(payment_db.values())

    # Filter to only payments with matching status
  filtered = []

  for payment in payments_db.values() :
      if payment["status"] == status:
          filtered.append(payment)
  return filtered

@app.put("/payment/{payment_id}")
def updated_payment(payment_id : int, request : UpdatePaymentDetails) -> PaymentDetail:
    if payment_id not in payments_db:
        raise HTTPException(status_code=404, detail="Payment not found")

    # update the payment
    payment = payments_db[payment_id]
    payment["status"] = request.status

    # Return the updated payment
    return PaymentDetail (
        id = payment["id"],
        amount=payment["amount"],
        phone_number=payment["phone_number"],
        status=payment["status"]
    )

@app.delete("/payment/{payment_id}")
def delete_payment(payment_id : int) :
    if payment_id not in payments_db:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    del payments_db[payment_id]

    return {"message" : "Payment deleted successfully"}

    