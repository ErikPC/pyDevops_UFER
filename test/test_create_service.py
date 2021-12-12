import pytest
from src.model.data_creation.create_service.create_service import create_service
from src.repository.db_connection.connect_db import connect_db

database = connect_db()
collection = database['ufer']


@pytest.mark.test_create_service
def test_create_service():
    create_service(collection)
