from sqlalchemy.orm import Session
from auction import models, schemas
from fastapi import HTTPException, status

# function to get all auctions
def get_all(db: Session):
    auctions = db.query(models.Auction).all()
    return auctions

# function to create a new auction
def create(request: schemas.Auction, db: Session):
    new_auction = models.Auction(title=request.title, description=request.description, start_price=request.start_price, current_price=request.current_price, bid_increment=request.bid_increment, start_time=request.start_time, end_time=request.end_time, image=request.image, owner_id=1)
    db.add(new_auction)
    db.commit()
    db.refresh(new_auction)
    return new_auction

# function to delete an auction
def destroy(id: int, db: Session):
    auction = db.query(models.Auction).filter(models.Auction.id == id)

    if not auction.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Auction with id {id} not found")

    auction.delete(synchronize_session=False)
    db.commit()
    return 'done'


# function to update an auction
def update(id: int, request: schemas.Auction, db: Session):
    auction = db.query(models.Auction).filter(models.Auction.id == id)

    if not auction.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Auction with id {id} not found")

    auction.update(request)
    db.commit()
    return 'updated'


def show(id: int, db: Session):
    auction = db.query(models.Auction).filter(models.Auction.id == id).first()
    if not auction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Auction with the id {id} is not available")
    return auction


# function to get all auctions by owner
def get_auctions_by_owner(owner_id: int, db: Session):
    auctions = db.query(models.Auction).filter(models.Auction.owner_id == owner_id).all()
    return auctions


# function to get all auctions by bidder
def get_auctions_by_bidder(bidder_id: int, db: Session):
    auctions = db.query(models.Auction).filter(models.Auction.bids.any(models.Bid.bidder_id == bidder_id)).all()
    return auctions


# function to get all auctions by category
def get_auctions_by_category(category_id: int, db: Session):
    auctions = db.query(models.Auction).filter(models.Auction.categories.any(models.Category.id == category_id)).all()
    return auctions


# function to get all auctions by status
def get_auctions_by_status(status: str, db: Session):
    auctions = db.query(models.Auction).filter(models.Auction.status == status).all()
    return auctions


# function to get all auctions by title
def get_auctions_by_title(title: str, db: Session):
    auctions = db.query(models.Auction).filter(models.Auction.title == title).all()
    return auctions