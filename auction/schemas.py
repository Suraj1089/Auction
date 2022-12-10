from pydantic import BaseModel


class AuctionBase(BaseModel):
    title: str
    description: str
    start_price: float
    current_price: float
    bid_increment: float
    start_time: str
    end_time: str
    image: str
    owner_id: int


class Auction(BaseModel):
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str
    auctions: list = []
    bids: list = []
    is_active: bool = True
    is_superuser: bool = False


class ShowUser(BaseModel):
    name: str
    email: str
    auctions: list = []
    bids: list = []
    is_active: bool = True
    is_superuser: bool = False

    class Config():
        orm_mode = True


class ShowAuction(BaseModel):
    title: str
    description: str
    start_price: float
    current_price: float
    bid_increment: float
    start_time: str
    end_time: str
    image: str
    owner: ShowUser
    bids: list = []

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None


class Bid(BaseModel):
    auction_id: int
    user_id: int
    amount: float

    class Config():
        orm_mode = True


class ShowBid(BaseModel):
    auction: ShowAuction
    user: ShowUser
    amount: float

    class Config():
        orm_mode = True


class Bidder(BaseModel):
    auction_id: int
    user_id: int
    amount: float

    class Config():
        orm_mode = True


class ShowBidder(BaseModel):
    auction: ShowAuction
    user: ShowUser
    amount: float

    class Config():
        orm_mode = True


class Winner(BaseModel):
    auction_id: int
    user_id: int
    amount: float

    class Config():
        orm_mode = True


class ShowWinner(BaseModel):
    auction: ShowAuction
    user: ShowUser
    amount: float

    class Config():
        orm_mode = True
