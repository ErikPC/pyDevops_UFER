from src.model.data_extraction.values_extraction import get_values
from pymongo.errors import PyMongoError


def delete_data(collection):
    # get all services
    servicios = get_values(collection, 'name')

    # print all services
    print('servicios disponibles:', servicios)

    # delete document from the database
    servicio_eliminar = input("Escribe el servicio que quieres eliminar: \n").strip().title()
    confirm = input("Vuelve a escribir el servicio: \n").strip().title()

    if servicio_eliminar != confirm:
        print("Los servicios no coinciden")

    elif servicio_eliminar in servicios:

        try:
            collection.delete_one({"name": servicio_eliminar})
        except PyMongoError:
            print("La operación ha fallado")
        else:
            print("Servicio eliminado correctamente")
            return True

    else:
        print("item no encontrado")
