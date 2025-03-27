# test_main.py
import pytest
from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch

client = TestClient(app)

# Mock data
mock_product = {
    "ProductID": "AUTO001",
    "Name": "Starter Motor",
    "UnitPrice": 243.69,
    "StockQuantity": 50,
    "Description": "High-quality Starter Motor designed for durability and performance."
}

@patch("main.collection.find_one", return_value=mock_product)
def test_get_single_product(mock_db):
    response = client.get("/getSingleProduct?id=AUTO001")
    assert response.status_code == 200
    assert response.json()["ProductID"] == "AUTO001"

@patch("main.collection.find", return_value=[mock_product])
def test_get_all(mock_db):
    response = client.get("/getAll")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@patch("main.collection.insert_one", return_value=None)
def test_add_new(mock_db):
    response = client.post("/addNew", json=mock_product)
    assert response.status_code == 200
    assert response.json()["message"] == "Product added successfully"

@patch("main.collection.delete_one", return_value=type("MockDelete", (), {"deleted_count": 1}))
def test_delete_one(mock_db):
    response = client.delete("/deleteOne?id=AUTO001")
    assert response.status_code == 200
    assert response.json()["message"] == "Product deleted successfully"
