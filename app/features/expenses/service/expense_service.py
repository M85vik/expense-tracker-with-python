from typing import Optional
from datetime import date
from app.features.expenses.repository.expense_repository import ExpenseRepository


class ExpenseService:
    def __init__(self):
        self.repo = ExpenseRepository()

    async def create_expense(self, expense: dict):
        return await self.repo.create_expense(expense)

    async def get_expenses(
        self,
        category: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None
    ):
        return await self.repo.get_expenses(category, start_date, end_date)
