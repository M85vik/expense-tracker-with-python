from fastapi import FastAPI
from app.features.expenses.router.expense_router import router as expense_router

app = FastAPI()
app.include_router(expense_router)
@app.get("/")
def home():
    return {"message": "Expense Tracker API running 🚀"}