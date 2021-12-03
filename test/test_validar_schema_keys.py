import pytest
from src.model.data_validation.validate_schema_keys import validate_keys

ufer_schema_invalid_keys = {
    "nombre": "Ufer Gold",
    "description": "Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and "
                   "amenities you can imagine.",
    "conductor": "Autopilot",
    "passengers": 1,
    "privacy": "Private",
    "seats": "King Size",
    "propulsion": "Photon Engine",
    "top_speed": 1080000000,
    "price": 120,
    "amenities": ["WiFi", "Bluetooth", "Tinted Screens", "HiFi Audio System", "A/C", "Champagne Bottle", "Water",
                  "Snacks"]
}
ufer_schema_invalid_keys_and_types = {
    "nombre": "Ufer Gold",
    "description": "Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and "
                   "amenities you can imagine.",
    "conductor": "Autopilot",
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


@pytest.mark.test_validar_keys
def test_validar_keys():
    assert validate_keys(ufer_schema_invalid_keys) == False
    assert validate_keys(ufer_schema_invalid_keys_and_types) == False


@pytest.mark.test_validar_keys
def test_validar_keys():
    assert validate_keys(ufer_schema_valid) == True
