from src.model.data_creation.create_service.create_service import create_service
from src.model.data_deletion.data_deletion import delete_data
from src.model.data_extraction.data_extraction import load_data
from src.model.data_updation.update_price.update_price import update_price

def controller(collection):
    salir = False
    menu = [1,2,3,4,9]
    while not salir:
        selection = input("Tiene las siguientes opciones:\n 1-Crear un servicio\n 2-Eliminar un servicio\n 3-Vicualizar un servicio\n 4-Cambiar un precio\n 9-Exit")
        if selection not in menu:
            print("No es una entrada valida")
        if selection == 1:
            create_service(collection)
        if selection == 2:
            delete_data(collection)
        if selection == 3:
            load_data(collection)
        if selection == 4:
            update_price(collection)
        if selection == 9:
            salir = True