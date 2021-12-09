import pytest
from src.model.data_creation.create_service.fill_operations.fill_string import fill_string


@pytest.mark.test_fill_string
def test_fill_string():
    input = '   ufer life   '
    key_name = 'name'
    output = fill_string('name')
    assert output == 'ufer life'
