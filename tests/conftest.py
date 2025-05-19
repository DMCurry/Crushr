import pytest
from fastapi.testclient import TestClient
import sys, pathlib
from dotenv import load_dotenv
load_dotenv(dotenv_path=pathlib.Path(__file__).parent.parent / ".env")

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.resolve()))
from main import app
from app.dependencies import get_current_user  # or wherever you defined it

# A dummy user dict matching what your real dep returns
fake_user = {"id": 1001}

@pytest.fixture(autouse=True)
def override_auth_dependency():
    # override get_current_user with a zero-arg function
    def _override_get_current_user():
        return fake_user

    # override get_current_user to just return our fake_user
    app.dependency_overrides[get_current_user] = _override_get_current_user
    yield
    app.dependency_overrides.clear()


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c