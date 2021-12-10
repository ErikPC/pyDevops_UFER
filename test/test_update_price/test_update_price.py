import pytest
from src.model.content_updation.update_price import update_service_price

# route: test_files/name_file.file_type

route = 'test_files/'
file_type = '.md'

# valid info
info1 = {
    'name': 'Ufer Bacon',
    'current_price': 30,
    'new_price': 20
}

# valid info
info2 = {
    'name': 'Ufer Spam',
    'current_price': 40,
    'new_price': 50
}

# invalid info
info_bad = {
    'name': 'Ufer Loco',
    'current_price': 40,
    'new_price': 50
}

# None info
info3 = None


@pytest.mark.test_update_price
def test_update_price():
    assert update_service_price(info1, route, file_type) == True
    assert update_service_price(info2, route, file_type) == True
    assert update_service_price(info3, route, file_type) == False
    assert update_service_price(info_bad, route, file_type) is None
