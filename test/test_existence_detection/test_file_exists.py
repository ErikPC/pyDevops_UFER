import pytest
from src.model.content_generation.existence_detection.file_exists import file_exists


@pytest.mark.test_file_exists
def test_file_exists():
    assert file_exists('test_dir/', 'hola', '.md') == True
    assert file_exists('test_dir/', 'hi', '.md') == True
    assert file_exists('test_dir/', 'hey', '.html') == True
    assert file_exists('adir/', 'index', '.js') == False

