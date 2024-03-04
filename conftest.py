import pytest
from tests import BooksCollector

def pytest_make_parametrize_id(val):  
    return repr(val)

@pytest.fixture
def collector():
    return BooksCollector()