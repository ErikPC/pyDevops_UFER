from pymongo import database
import pytest
from src.model.data_deletion import delete_data
from src.repository.db_connection.connect_db import connect_db

database = connect_db()
collection = database['ufer']



@pytest.mark.test_delete_data
def test_delete_data():
    delete_data(collection)
