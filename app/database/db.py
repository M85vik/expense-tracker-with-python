import asyncpg
import os 
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


async def get_db_connection():
    return await asyncpg.connect(DATABASE_URL)



pool = None


async def init_db():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)

    