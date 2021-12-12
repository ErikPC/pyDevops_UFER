import pytest
from src.model.service_selection.select_service.select_service import select_service


@pytest.mark.test_select_service
def test_select_service():
    services = ['Ufer Gold', 'Ufer Lite', 'Ufer Loco', 'Ufer Fly', 'Ufer Style', 'Ufer Life']
    select_service(services)
