from src.model.data_creation.create_service.fill_operations.fill_array import fill_array
from src.model.data_creation.create_service.fill_operations.fill_int import fill_int
from src.model.data_creation.create_service.fill_operations.fill_string import fill_string
from src.model.data_validation import validate_schema
from src.model.data_validation.validate_schema import validate_schema
from src.repository.db_connection.config_params import *
from pymongo.errors import OperationFailure


def create_service(collection):
    # generate empty_values document
    document = {
        "name": "",
        "description": "",
        "driver": "",
        "passengers": 0,
        "privacy": "",
        "seats": "",
        "propulsion": "",
        "top_speed": 0,
        'price': 0,
        "amenities": []
    }

    user_instructions = "Para crear un servicio, sigue el siguiente schema:\n" "\n \t\"name\": \"\"," \
                        "\n\t\"description\": \"\",\n\t" "\"driver\": \"\",\n\t\"passengers\": \"\"," \
                        "\n\t\"privacy\": \"\",\n\t\"seats\": \"\",\n\t\"propulsion\": ""\"\",\n\t\"top_speed\": " \
                        "0,\n\t\"amenities\": []\n\t  "

    # tell the user how to fill the values
    print(user_instructions)

    # fill every value of the empty document (depending on the value type it has)
    for index in range(len(PYDEVOPS_KEYS)):
        if PYDEVOPS_VALUE_TYPES[index] == str:
            if PYDEVOPS_KEYS[index] == 'name':
                document[PYDEVOPS_KEYS[index]] = fill_string(PYDEVOPS_KEYS[index]).title()
            else:
                document[PYDEVOPS_KEYS[index]] = fill_string(PYDEVOPS_KEYS[index])
        elif PYDEVOPS_VALUE_TYPES[index] == int:
            document[PYDEVOPS_KEYS[index]] = fill_int(PYDEVOPS_KEYS[index])
        elif PYDEVOPS_VALUE_TYPES[index] == list:
            document[PYDEVOPS_KEYS[index]] = fill_array()

    # schema validation
    if validate_schema(document):

        try:
            new_document_id = collection.insert_one(document)
        except OperationFailure:
            print('the insert operation failed')
        else:
            print('insertion done successfully')
            return new_document_id
    else:
        return False
