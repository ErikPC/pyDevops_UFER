from pymongo import database
import pytest
from src.model.data_deletion import delete_data
from src.repository.db_connection.connect_db import connect_db

database = connect_db()
collection = database['pruebas']
# Cuenado esto funcione , hay que cambiar 'pruebas' por el nombre de de la coleccion definitiva
collection.insert_one(
    {
        'nombre': 'Joan',
        'edad': 20,
        'deportes': ['padel', 'futbol', 'boxeo'],
        "services": "uber"
    }
)


@pytest.mark.test_delete_data
def test_delete_data():
    delete_data(collection)
