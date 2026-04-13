from typing import Optional
from datetime import date
from app.database.db import get_db_connection


class ExpenseRepository:

    async def create_expense(self, expense: dict):
        conn = await get_db_connection()

        query = """
        INSERT INTO expenses (title, amount, category, date, description)
        VALUES ($1, $2, $3, $4, $5)
        RETURNING *;
        """

        result = await conn.fetchrow(
            query,
            expense["title"],
            expense["amount"],
            expense["category"],
            expense["date"],
            expense.get("description")
        )

        await conn.close()
        return dict(result)

    async def get_expenses(
        self,
        category: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None
    ):
        conn = await get_db_connection()

        query = "SELECT * FROM expenses WHERE 1=1"
        params = []
        idx = 1

        if category:
            query += f" AND category = ${idx}"
            params.append(category)
            idx += 1

        if start_date:
            query += f" AND date >= ${idx}"
            params.append(start_date)
            idx += 1

        if end_date:
            query += f" AND date <= ${idx}"
            params.append(end_date)
            idx += 1

        rows = await conn.fetch(query, *params)

        await conn.close()
        return [dict(row) for row in rows]


    async def get_expense_by_id(self, expense_id:int):
        conn = await get_db_connection()

        query = "SELECT * FROM expenses WHERE id = $1 RETURNING id"

        result = await conn.fetchrow(query, expense_id)

        await conn.close()
        return dict(result)



    async def get_expenses_by_month(self, month: int, year: int):

        conn = await get_db_connection()

        query = """
        SELECT category, amount
        FROM expenses
        WHERE EXTRACT(MONTH FROM date) = $1
        AND EXTRACT(YEAR FROM date) = $2
        """

        rows = await conn.fetch(query, month, year)

        await conn.close()
        return [dict(row) for row in rows]
    
    
    async def get_expense_by_id(self, expense_id: int):
        conn = await get_db_connection()

        query = "SELECT * FROM expenses WHERE id = $1"
        result = await conn.fetchrow(query, expense_id)

        await conn.close()
        return dict(result) if result else None

    async def delete_expense(self, expense_id: int):
        conn = await get_db_connection()

        query = "DELETE FROM expenses WHERE id = $1 RETURNING id"
        result = await conn.fetchrow(query, expense_id)

        await conn.close()
        return result is not None