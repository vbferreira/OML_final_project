import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_valid_input():
    payload = {
        "LIMIT_BAL": 50000,
        "SEX": 2,
        "EDUCATION": 2,
        "MARRIAGE": 1,
        "AGE": 35,
        "PAY_0": 0,
        "PAY_2": 0,
        "PAY_3": 0,
        "PAY_4": 0,
        "PAY_5": 0,
        "PAY_6": 0,
        "BILL_AMT1": 1000,
        "BILL_AMT2": 1000,
        "BILL_AMT3": 1000,
        "BILL_AMT4": 1000,
        "BILL_AMT5": 1000,
        "BILL_AMT6": 1000,
        "PAY_AMT1": 500,
        "PAY_AMT2": 500,
        "PAY_AMT3": 500,
        "PAY_AMT4": 500,
        "PAY_AMT5": 500,
        "PAY_AMT6": 500
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "probability" in response.json()

def test_predict_invalid_input():
    # Missing required fields
    payload = {"LIMIT_BAL": 50000}

    response = client.post("/predict", json=payload)
    assert response.status_code == 422
