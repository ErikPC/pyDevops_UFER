from src.model.data_extraction.values_extraction import get_values
from pymongo.errors import OperationFailure


def delete_data(collection):
    # get all services
    servicios = get_values(collection, 'name')

    # print all services
    print('servicios disponibles:', servicios)

    # delete document from the database
    servicio_eliminar = input("Escribe el servicio que quieres eliminar: \n")
    confirm = input("Vuelve a escribir el servicio: \n")

    if servicio_eliminar != confirm:
        print("Los servicios no coinciden")

    elif servicio_eliminar in servicios:

        try:
            collection.delete_one({"name": servicio_eliminar})
        except OperationFailure:
            print("La operación ha fallado")
        else:
            print("Se ha eliminado correctamente")
            return True

    else:
        print("item no encontrado")
