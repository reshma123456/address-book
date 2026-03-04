"""API routes for managing addresses."""
import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas, models
from app.services.distance_service import is_within_distance

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/addresses", tags=["Addresses"])

@router.post("/", response_model=schemas.AddressResponse, status_code=status.HTTP_201_CREATED)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    """Create a new address."""
    logger.info("Create address request received")
    return crud.create_address(db, address)

@router.get("/", response_model=list[schemas.AddressResponse])
def list_addresses(db: Session = Depends(get_db)):
    """Return all stored addresses."""
    logger.info("Fetching all addresses")
    return crud.get_addresses(db)

@router.put("/{address_id}", response_model=schemas.AddressResponse)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    """Update an existing address."""
    updated = crud.update_address(db, address_id, address)
    if not updated:
        logger.error("Address not found id=%s", address_id)
        raise HTTPException(status_code=404, detail="Address not found")
    return updated

@router.delete("/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    """Delete an address."""
    deleted = crud.delete_address(db, address_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"message": "Address deleted successfully"}

@router.get("/nearby", response_model=list[schemas.AddressResponse])
def nearby_addresses(lat: float, lon: float, distance: float, db: Session = Depends(get_db)):
    """Return addresses within a given radius."""
    logger.info("Searching nearby addresses")
    addresses = db.query(models.Address).all()
    results = [
        a for a in addresses
        if is_within_distance(lat, lon, a.latitude, a.longitude, distance)
    ]
    return results