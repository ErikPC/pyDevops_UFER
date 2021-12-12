from src.model.content_generation.template.template_config import destiny
from src.model.content_generation.template.template_config import file_type
from src.model.content_generation.existence_detection.file_exists import file_exists
import os


def delete_service(service):

    # tell the user which service wants to delete
    # input('Service to delete: ').strip().title()
    service_to_delete = service

    if file_exists(destiny, service_to_delete, file_type):
        os.remove(destiny + service_to_delete + file_type)
    else:
        print("The service doesn't exists")
