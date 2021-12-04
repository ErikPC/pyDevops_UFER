from src.model.data_validation import validate_schema


def create_service(collection):
    item_template = {
        "name": "",
        "description": "",
        "driver": "",
        "passengers": "",
        "privacy": "",
        "seats": "",
        "propulsion": "",
        "top_speed": 0,
        "amenities": []
    }

    user_instructions = "Para crear un servicio, sigue el siguiente schema:\n" "{\n \t\"name\": \"\"," \
                        "\n\t\"description\": \"\",\n\t " "\"driver\": \"\",\n\t\"passengers\": \"\"," \
                        "\n\t \"privacy\": \"\",\n\t \"seats\": \"\",\n\t \"propulsion\": ""\"\",\n\t \"top_speed\": " \
                        "0,\n\t \"amenities\": []\n\t } "

    # tell the user how to fill the values
    print(user_instructions)


