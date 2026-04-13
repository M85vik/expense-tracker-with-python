from pydantic import BaseModel
from datetime import date
from typing import Optional


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    date: date   # 🔥 THIS is key
    description: Optional[str] = None


class ExpenseResponse(BaseModel):
    id:int
    title:str
    amount:float
    category:str
    date:date
    description:Optional[str]=None
