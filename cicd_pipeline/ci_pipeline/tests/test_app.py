from unittest.mock import MagicMock, patch

import pytest
import torch
from fastapi.testclient import TestClient


def test_predict(mock_client: TestClient, mock_model: MagicMock):
    test_input = {"x1": 0, "x2": 1}
    expected_tensor = [[test_input["x1"], test_input["x2"]]]
    mock_model.return_value = torch.Tensor([0.0])

    response = mock_client.post("/predict/", json=test_input)

    assert response.status_code == 200
    assert response.json() == {"prediction": 0.0}

    mock_model.assert_called_once()
    args, _ = mock_model.call_args
    assert args[1].tolist() == expected_tensor


@pytest.mark.parametrize("x1, x2", [(0, 0), (0, 1), (1, 0), (1, 1)])
def test_predict_with_model_input(
    mock_client: TestClient,
    mock_model: MagicMock,
    x1: float,
    x2: float,
):
    response = mock_client.post("/predict/", json={"x1": x1, "x2": x2})

    mock_model.assert_called_once()
    args, _ = mock_model.call_args

    assert torch.equal(args[1], torch.tensor([[x1, x2]], dtype=torch.float32))
    assert response.status_code == 200
