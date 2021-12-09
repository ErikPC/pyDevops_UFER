import pytest
from src.model.data_creation.create_service.fill_operations.fill_int import fill_int


@pytest.mark.test_fill_int
def test_fill_int():
    desired_output = 80
    output = fill_int('price')
    assert output == desired_output
