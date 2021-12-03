from jsonschema import validate
from jsonschema.exceptions import ValidationError

correct_schema = {

    "type": "object",
    "properties" : {
        "name": {"type" : "string"},
        "description": {"type" : "string"},
        "driver": {"type" : "string"},
        "passengers": {"type": "number"},
        "privacy": {"type" : "string"},
        "seats": {"type" : "string"},
        "propulsion": {"type" : "string"},
        "top_speed": {"type": "number"},
        "price" : {"type" : "number"},
        "amenities": {"type": "array"}
    }
}

def validate_value_types(schema_to_validate):
    print("validating schema value types...")
    try:
        validate(instance=schema_to_validate, schema=correct_schema)

    except ValidationError:
        print("invalid value type")
    else:
        return True
    return False