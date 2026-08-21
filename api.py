from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import validate_amount,validate_phone_number

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
    amount: int
    phone_number : str
    status : str


# first endpoint
@app.post("/payment/stk-push")
def initiate_payment(request : PaymentRequest) -> PaymentResponse :
    if not validate_amount(request.amount) :
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")
    elif not validate_phone_number(request.phone_number):
        raise HTTPException(status_code=400, detail= "Invalid number" )
    else :
        return PaymentResponse(
            status = "Pending",
            message = f"Payment of {request.amount} initiated for {request.phone_number}"
        )

@app.get("/payment/{payment_id}")
def get_payment(payment_id : int) -> PaymentDetail :
    return PaymentDetail(
                    id=payment_id,
                    amount=100,
                    phone_number="2541234567",
                    status="pending"
    )
        

    
