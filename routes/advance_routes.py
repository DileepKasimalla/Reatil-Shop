from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Advance)
def add_advance(advance: schemas.AdvanceCreate, db: Session = Depends(get_db)):

    db_advance = models.Advance(
        customer_id=advance.customer_id,
        amount=advance.amount,
        used_amount=advance.used_amount,
        pending_amount=advance.pending_amount
    )

    db.add(db_advance)
    db.commit()
    db.refresh(db_advance)
    return db_advance


@router.get("/customer/{customer_id}", response_model=list[schemas.Advance])
def get_customer_advances(customer_id: int, db: Session = Depends(get_db)):
    return db.query(models.Advance).filter(models.Advance.customer_id == customer_id).all()


@router.put("/repaid/{advance_id}")
def repay_advance(advance_id: int, db: Session = Depends(get_db)):
    adv = db.query(models.Advance).filter(models.Advance.id == advance_id).first()
    adv.repaid = True
    db.commit()
    return {"message": "Advance marked as repaid"}
