from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..database import get_db
from ..import models, schemas
from passlib.context import CryptContext


router = APIRouter(
    tags=['Seller']
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/seller', response_model=schemas.DisplaySeller)
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashedPassword = pwd_context.hash(request.password)
    new_seller = models.Seller(username=request.username, email=request.email, password=hashedPassword)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller