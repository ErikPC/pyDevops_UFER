from src.model.data_creation.create_service.fill_operations.fill_array import fill_array
from src.model.data_creation.create_service.fill_operations.fill_int import fill_int
from src.model.data_creation.create_service.fill_operations.fill_string import fill_string
from src.model.data_validation import validate_schema
from src.model.data_validation.validate_schema import validate_schema


def create_service(collection):
    document = {
        "name": "",
        "description": "",
        "driver": "",
        "passengers": 0,
        "privacy": "",
        "seats": "",
        "propulsion": "",
        "top_speed": 0,
        "amenities": []
    }

    user_instructions = "Para crear un servicio, sigue el siguiente schema:\n" "\n \t\"name\": \"\"," \
                        "\n\t\"description\": \"\",\n\t" "\"driver\": \"\",\n\t\"passengers\": \"\"," \
                        "\n\t\"privacy\": \"\",\n\t\"seats\": \"\",\n\t\"propulsion\": ""\"\",\n\t\"top_speed\": " \
                        "0,\n\t\"amenities\": []\n\t  "

    # tell the user how to fill the values
    print(user_instructions)

    # functions to fill every value of the dict
    document['name'] = fill_string('name')
    document["description"] = fill_string('description')
    document['driver'] = fill_string('driver')
    document["passengers"] = fill_int('passengers')
    document['privacy'] = fill_string('privacy')
    document['seats'] = fill_string('seats')
    document['propulsion'] = fill_string('propulsion')
    document["top_speed"] = fill_int('top speed')
    document["amenities"] = fill_array()

