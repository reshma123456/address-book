"""Pydantic schemas for request validation and response serialization."""
from pydantic import BaseModel, Field

class AddressBase(BaseModel):
    """Base schema containing shared address attributes."""
    address_line: str
    city: str
    country: str
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

class AddressCreate(AddressBase):
    """Schema used when creating an address."""
    pass

class AddressUpdate(AddressBase):
    """Schema used when updating an address."""
    pass

class AddressResponse(AddressBase):
    """Schema returned by API responses."""
    id: int

    class Config:
        from_attributes = True