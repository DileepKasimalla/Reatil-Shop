from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional, List


# ----------------------- CUSTOMER -----------------------
class CustomerCreate(BaseModel):
    name: str


class Customer(BaseModel):
    id: int
    name: str
    created_at: datetime

    class Config:
        orm_mode = True


# ----------------------- DEBT (MULTIPLE ITEMS) -----------------------
class DebtCreate(BaseModel):
    customer_id: int
    item: List[str]      # list of item names
    cost: List[float]    # list of costs
    total_cost: float = 0.0

    @model_validator(mode="after")
    def validate_items_and_costs(self):
        # Validate equal length
        if len(self.item) != len(self.cost):
            raise ValueError("Number of items and costs must be the same.")

        # Auto calculate total cost
        self.total_cost = sum(self.cost)
        return self


class Debt(BaseModel):
    id: int
    customer_id: int
    item: List[str]
    cost: List[float]
    total_cost: float
    date: datetime
    repaid: bool

    class Config:
        orm_mode = True


# ----------------------- ADVANCE -----------------------
class AdvanceCreate(BaseModel):
    customer_id: int
    amount: float
    used_amount: Optional[float] = 0
    pending_amount: float


class Advance(BaseModel):
    id: int
    customer_id: int
    amount: float
    used_amount: float
    pending_amount: float
    date: datetime
    repaid: bool

    class Config:
        orm_mode = True


# ----------------------- ITEMS PRICE RANGE -----------------------
class ItemCreate(BaseModel):
    name: str
    min_price: float
    max_price: float


class Item(BaseModel):
    id: int
    name: str
    min_price: float
    max_price: float

    class Config:
        orm_mode = True
