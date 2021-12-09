import pytest
from src.model.service_selection.select_service.select_service import select_service
<<<<<<< HEAD

services = ['Ufer Lite', 'Ufer Gold', 'Ufer Life', 'Ufer Bus']
=======
>>>>>>> 12118c3e056879ab54aac6280a8e1107e5ec087b


@pytest.mark.test_select_service
def test_select_service():
    services = ['Ufer Gold', 'Ufer Lite', 'Ufer Loco', 'Ufer Fly', 'Ufer Style']
    select_service(services)
