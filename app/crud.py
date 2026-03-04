"""CRUD operations for interacting with the database."""
import logging
from sqlalchemy.orm import Session
from app import models, schemas

logger = logging.getLogger(__name__)

def create_address(db: Session, address: schemas.AddressCreate) -> models.Address:
    """Create and store a new address."""
    try:
        db_address = models.Address(**address.model_dump())
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
        logger.info("Address created with id=%s", db_address.id)
        return db_address
    except Exception as exc:
        logger.exception("Failed to create address")
        db.rollback()
        raise exc

def get_addresses(db: Session):
    """Retrieve all addresses."""
    return db.query(models.Address).all()

def get_address(db: Session, address_id: int):
    """Retrieve a single address."""
    return db.query(models.Address).filter(models.Address.id == address_id).first()

def update_address(db: Session, address_id: int, address: schemas.AddressUpdate):
    """Update address details."""
    db_address = get_address(db, address_id)
    if not db_address:
        return None

    for key, value in address.model_dump().items():
        setattr(db_address, key, value)

    db.commit()
    db.refresh(db_address)
    logger.info("Address updated id=%s", address_id)
    return db_address

def delete_address(db: Session, address_id: int):
    """Delete an address."""
    db_address = get_address(db, address_id)
    if not db_address:
        return None

    db.delete(db_address)
    db.commit()
    logger.warning("Address deleted id=%s", address_id)
    return db_address