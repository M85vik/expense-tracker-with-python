import asyncio
from app.database.db import get_db_connection

async def test():
    conn = await get_db_connection()
    result = await conn.fetch("SELECT 1;")
    print(result)
    await conn.close()

asyncio.run(test())