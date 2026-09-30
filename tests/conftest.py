import pytest
from app import app as flask_app
@pytest.fixture
def client(): 
    flask_app.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False
    )
    with flask_app.test_client() as c:
        yield c