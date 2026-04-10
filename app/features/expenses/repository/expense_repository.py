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