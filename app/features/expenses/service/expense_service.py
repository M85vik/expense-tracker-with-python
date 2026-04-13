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

    async def get_expense_by_id(self, expense_id: int):
        expense = await self.repo.get_expense_by_id(expense_id)
        if not expense:
            raise Exception("Expense not found")
        return expense

    async def delete_expense(self, expense_id: int):
        deleted = await self.repo.delete_expense(expense_id)
        if not deleted:
            raise Exception("Expense not found")
        return {"message": "Expense deleted successfully"}

    async def get_summary(self, month: int, year: int):
        expenses = await self.repo.get_expenses_by_month(month, year)

        total = 0
        by_category = {}

        for exp in expenses:
            amount = float(exp["amount"])
            category = exp["category"]

            total += amount

            if category in by_category:
                by_category[category] += amount

            else:
                by_category[category] = amount

        return {
            "total": total,
            "by_category": by_category
        }
