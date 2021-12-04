import pytest
from src.model.data_validation.validate_schema_value_types import validate_value_types

ufer_schema_invalid_types = {

    "name": "Ufer Gold",
    "description": "Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and "
                   "amenities you can imagine.",
    "driver": "Autopilot",
    "passengers": 1,
    "privacy": "Private",
    "seats": "King Size",
    "propulsion": "Photon Engine",
    "top_speed": 1080000000,
    "price": "120",
    "amenities": ["WiFi", "Bluetooth", "Tinted Screens", "HiFi Audio System", "A/C", "Champagne Bottle", "Water",
                  "Snacks"]
}

ufer_schema_valid = {

    "name": "Ufer Gold",
    "description": "Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and "
                   "amenities you can imagine.",
    "driver": "Autopilot",
    "passengers": 1,
    "privacy": "Private",
    "seats": "King Size",
    "propulsion": "Photon Engine",
    "top_speed": 1080000000,
    "price": 120,
    "amenities": ["WiFi", "Bluetooth", "Tinted Screens", "HiFi Audio System", "A/C", "Champagne Bottle", "Water",
                  "Snacks"]
}


@pytest.mark.validate_value_types
def test_validate_value_types():
    assert validate_value_types(ufer_schema_valid) == True
    assert validate_value_types(ufer_schema_invalid_types) == False

