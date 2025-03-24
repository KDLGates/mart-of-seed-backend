# This is a fallback version that doesn't require database
# Original imports commented out to prevent circular imports
# import random
# import math
# from datetime import datetime, timedelta
# from models.models import db, Seed, SeedPrice

print("Using fallback seed_db module")

# Fallback seed types list without requiring database
SEED_TYPES = [
    {"name": "Tomato", "species": "Solanum lycopersicum"},
    {"name": "Carrot", "species": "Daucus carota"},
    {"name": "Sunflower", "species": "Helianthus annuus"},
    # ...other seeds...
]

def seed_database():
    """
    Fallback version of seed_database that doesn't require DB access
    """
    print("Database seeding skipped - using fallback module")
    return False