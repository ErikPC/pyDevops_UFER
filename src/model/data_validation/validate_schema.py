from src.model.data_validation.validate_schema_keys import validate_keys
from src.model.data_validation.validate_schema_value_types import validate_value_types


def validate_schema(schema):

    if not (validate_keys(schema) and validate_value_types(schema)):
        print("invalid schema")
        print(schema)
        return False
    print("the schema is correct")
    return True
