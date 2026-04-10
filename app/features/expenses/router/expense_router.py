from fastapi import APIRouter
from typing import Optional
from datetime import date
from app.features.expenses.service.expense_service import ExpenseService

from app.features.expenses.schemas.expense_schema import ExpenseCreate , ExpenseResponse
from typing import List
router = APIRouter()
service = ExpenseService()


@router.post("/expenses", response_model=ExpenseResponse)
async def create_expense(expense: ExpenseCreate):
    return await service.create_expense(expense.model_dump())


@router.get("/expenses", response_model=List[ExpenseResponse])
async def get_expenses(
    category: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
):
    return await service.get_expenses(category, start_date, end_date)