from fastapi import FastAPI
from database import Base, engine
from routes.customer_routes import router as customer_router
from routes.debt_routes import router as debt_router
from routes.advance_routes import router as advance_router
from routes.item_routes import router as item_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Retail Shop API")

app.include_router(customer_router, prefix="/customers", tags=["Customers"])
app.include_router(debt_router, prefix="/debts", tags=["Debts"])
app.include_router(advance_router, prefix="/advances", tags=["Advances"])
app.include_router(item_router, prefix="/items", tags=["Items"])
