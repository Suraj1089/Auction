from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Auction(Base):
    __tablename__ = 'auctions'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    start_price = Column(Integer)
    current_price = Column(Integer)
    bid_increment = Column(Integer)
    start_time = Column(String)
    end_time = Column(String)
    image = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="auctions")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    is_active = Column(Integer)
    is_superuser = Column(Integer)

    auctions = relationship('Auction', back_populates="owner")


class Bid(Base):
    __tablename__ = 'bids'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    auction_id = Column(Integer, ForeignKey('auctions.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    auction = relationship("Auction", back_populates="bids")
    user = relationship("User", back_populates="bids")
