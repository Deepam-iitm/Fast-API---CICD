from fastapi import FastAPI
from schemas import SimpleInterestRequest

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome !!"}


@app.post("/si")
def calculate_si(req: SimpleInterestRequest):
    ans = (req.principal*req.rate*req.time)/100

    return {
    "principal": req.principal,
    "interest": round(ans, 2),
    "total_amount": round(req.principal + ans, 2)
    }

# uvicorn main:app --reload