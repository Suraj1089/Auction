from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from auction import models
from auction import database
from auction import models
from auction.routers import auction, authentication, user

app = FastAPI()

router = APIRouter(
    prefix="/auctions",
    tags=["auctions"],
)

get_db = database.get_db


models.Base.metadata.create_all(bind=database.engine)

app.include_router(auction.router)
app.include_router(user.router)
app.include_router(authentication.router)
