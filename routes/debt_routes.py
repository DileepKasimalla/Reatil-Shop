from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Debt)
def add_debt(debt: schemas.DebtCreate, db: Session = Depends(get_db)):

    db_debt = models.Debt(
        customer_id=debt.customer_id,
        item=debt.item,
        cost=debt.cost,
        total_cost=sum(debt.cost)
    )

    db.add(db_debt)
    db.commit()
    db.refresh(db_debt)
    return db_debt


@router.get("/customer/{customer_id}", response_model=list[schemas.Debt])
def get_customer_debts(customer_id: int, db: Session = Depends(get_db)):
    return db.query(models.Debt).filter(models.Debt.customer_id == customer_id).all()


@router.put("/repaid/{debt_id}")
def mark_debt_repaid(debt_id: int, db: Session = Depends(get_db)):
    debt = db.query(models.Debt).filter(models.Debt.id == debt_id).first()
    debt.repaid = True
    db.commit()
    return {"message": "Debt marked as repaid"}
