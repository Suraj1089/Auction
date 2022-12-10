from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from auction import schemas, models, oauth2
from sqlalchemy.orm import Session
from auction.repository import auction
from auction import database


router = APIRouter(
    prefix="/auction",
    tags=['Auctions']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowAuction])
def all(db: Session = Depends(get_db)):
    return auction.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Auction, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return auction.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowAuction)
def show(id: int, db: Session = Depends(get_db)):
    return auction.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return auction.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Auction, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return auction.update(id, request, db)
