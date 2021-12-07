from src.repository.db_connection.config_params import PYDEVOPS_KEYS


def validate_keys(schema_to_validate):
    assert isinstance(schema_to_validate, dict)
    is_valid = False
    counter = 0
    print("validating schema keys")

    for key in schema_to_validate.keys():

        if key not in PYDEVOPS_KEYS:
            is_valid = False
            print("the schema has an invalid key")
            return is_valid
        else:
            counter += 1

    # the document doesn't have all required keys
    if counter < len(PYDEVOPS_KEYS):
        is_valid = False
        print("The schema does't have all the required keys")
    else:
        is_valid = True

    return is_valid
