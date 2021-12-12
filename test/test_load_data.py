import pytest
from src.model.data_extraction.data_extraction import load_data
from src.repository.db_connection.connect_db import connect_db

database = connect_db()
collection = database['pruebas']
load = load_data(collection)

@pytest.mark.test_load_data
def test_load_data():
    assert isinstance(load , list)
    assert len(load) >= 0