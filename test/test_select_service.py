import pytest
from src.model.service_selection.select_service import select_service

services = ['Ufer Lite', 'Ufer Gold', 'Ufer Life', 'Ufer Bus']


@pytest.mark.test_select_service
def test_select_service():
    select_service()
