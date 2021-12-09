import pytest
from src.model.data_creation.create_service.fill_operations.fill_array import fill_array


@pytest.mark.test_fill_array
def test_fill_array():
    # add amenities vodzka and wifi
    output = fill_array()
    assert output == ['vodzka', 'wifi']
