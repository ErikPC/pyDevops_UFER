from src.model.data_validation import validate_schema

def create_service(collection):
    print("Para crear un servicio, sigue el siguiente schema:\n" "{\n \t\"name\": \"\",\n\t\"description\": \"\",\n\t \"driver\": \"\",\n\t\"passengers\": \"\",\n\t \"privacy\": \"\",\n\t \"seats\": \"\",\n\t \"propulsion\": \"\",\n\t \"top_speed\": 0,\n\t \"amenities\": []\n\t }")

    servicio_creado = input("Porfavor siga el schema:\n")

    is_valid = validate_schema(servicio_creado)

    if is_valid == True:
        collection.insert_one(servicio_creado)
    else:
        print("no es un schema valido")