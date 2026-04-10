from fastapi import APIRouter
from typing import Optional
from datetime import date
from app.features.expenses.service.expense_service import ExpenseService

from app.features.expenses.schemas.expense_schema import ExpenseCreate
router = APIRouter()
service = ExpenseService()


@router.post("/expenses")
async def create_expense(expense: ExpenseCreate):
    return await service.create_expense(expense.model_dump())


@router.get("/expenses")
async def get_expenses(
    category: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None
):
    return await service.get_expenses(category, start_date, end_date)