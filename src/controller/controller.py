from src.model.data_creation.create_service.create_service import create_service
from src.model.data_deletion.data_deletion import delete_data
from src.model.content_generation.file_generation.generate_files import generate_files
from src.model.data_updation.update_price.update_price import update_price
from src.model.content_deletion.delete_service import delete_service
from src.model.content_generation.template.template_config import *
from src.model.content_updation.update_price import update_service_price


def controller(collection):
    salir = False
    menu = ['1', '2', '3', '4', '5', '9']

    while not salir:
        selection = input(
            "Tiene las siguientes opciones:\n 1-Crear un servicio\n 2-Eliminar un servicio de la pagina\n "
            "3-Generar contenido en la página "
            "\n 4-Cambiar un precio\n 9-Exit\n").strip()

        # invalid input
        if selection not in menu:
            print("No es una entrada valida")

        # create a service
        if selection == '1':
            create_service(collection)
            generate_files(collection)

        # delete a service
        if selection == '2':
            servicio_a_eliminar = delete_data(collection)
            if servicio_a_eliminar is not None:
                delete_service(servicio_a_eliminar)

        # generate content
        if selection == '3':
            generate_files(collection)

        # update price of an existing service
        if selection == '4':
            info = update_price(collection)
            update_service_price(info, destiny, file_type)

        # exit
        if selection == '9':
            salir = True
