from typing import Generator
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture(scope="module")
def mock_client() -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client


@pytest.fixture
def mock_model() -> Generator[MagicMock, None, None]:
    with patch("ml_models.xor.XORModel.forward", autospec=True) as mock:
        yield mock
