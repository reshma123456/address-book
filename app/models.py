"""SQLAlchemy models representing database tables."""
from sqlalchemy import Column, Integer, Float, String
from app.database import Base

class Address(Base):
    """Database model storing address details and coordinates."""

    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    address_line = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)