from src.model.data_creation.create_service.create_service import create_service
from src.model.data_deletion.data_deletion import delete_data
from src.model.content_generation.file_generation.generate_files import generate_files
from src.model.data_updation.update_price.update_price import update_price
from src.model.content_deletion.delete_service import delete_service


def controller(collection):
    salir = False
    menu = ['1', '2', '3', '4', '5', '9']
    while not salir:
        selection = input(
            "Tiene las siguientes opciones:\n 1-Crear un servicio\n 2-Eliminar un servicio de la pagina\n "
            "3-Visualizar un "
            "servicio\n 4-Cambiar un precio\n 5-Eliminar servicio de atlas\n 9-Exit\n").strip()
        if selection not in menu:
            print("No es una entrada valida")
        if selection == '1':
            create_service(collection)
            generate_files(collection)
        if selection == '2':
            delete_service()
        if selection == '3':
            generate_files(collection)
        if selection == '4':
            update_price(collection)
        if selection == '5':
            delete_data(collection)
        if selection == '6':
            salir = True
