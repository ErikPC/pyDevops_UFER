PYDEVOPS_KEYS = ['name', 'description', 'driver', 'passengers', 'privacy', 'seats', 'propulsion', 'top_speed', 'price', 'amenities']

def validate_keys(schema_to_validate):
    assert isinstance(schema_to_validate, dict)
    isValid = False
    print("validating schema keys")

    for key in schema_to_validate.keys():
        if key not in PYDEVOPS_KEYS:
            isValid = False
            print("the schema has an invalid key")
            return isValid
    isValid = True
    assert isinstance(isValid, bool)
    return isValid
