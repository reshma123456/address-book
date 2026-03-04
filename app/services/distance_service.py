"""Service responsible for geographic distance calculations."""
from geopy.distance import geodesic

def is_within_distance(
    user_lat: float,
    user_lon: float,
    addr_lat: float,
    addr_lon: float,
    max_distance_km: float,
) -> bool:
    """Check if an address is within the given distance."""
    user_location = (user_lat, user_lon)
    address_location = (addr_lat, addr_lon)

    distance = geodesic(user_location, address_location).km
    return distance <= max_distance_km