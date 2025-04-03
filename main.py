import json
from typing import Union
from bson.json_util import dumps
from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

# Initialize FastAPI application
app = FastAPI()

# Enable CORS for all origins (to allow frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to MongoDB (Cloud-based)
client = MongoClient("mongodb+srv://shaun:shaun123@cluster0.hgdl308.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["WebServices"]
collection = db["products"]

# Pydantic model for product validation
class Product(BaseModel):
    ProductID: str
    Name: str
    UnitPrice: float
    StockQuantity: int
    Description: str

# Root endpoint (Test if API is running)
@app.get("/")
def read_root():
    return {"message": "API is running!"}

# Get a single product by ID
@app.get("/getSingleProduct/{product_id}")
def getSingleProduct(product_id: str):
    product = collection.find_one({"Product ID": product_id}, {"_id": 0})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Get all products
@app.get("/getAll")
def get_all():
    products = list(collection.find({}, {"_id": 0}))
    return products

# Add a new product using JSON body (POST request)
@app.post("/addNew")
def add_new(product: Product):
    product_data = product.dict()
    existing_product = collection.find_one({"Product ID": product.ProductID})
    if existing_product:
        raise HTTPException(status_code=400, detail="Product already exists")
    collection.insert_one(product_data)
    return {"message": "Product added successfully"}

# Delete a product by ID
@app.delete("/deleteOne/{product_id}")
def delete_one(product_id: str):
    result = collection.delete_one({"Product ID": product_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

# Get products starting with a specific letter
@app.get("/startsWith/{letter}")
def starts_with(letter: str):
    products = list(collection.find({"Name": {"$regex": f"^{letter}", "$options": "i"}}, {"_id": 0}))
    return products

# Paginate products by range of IDs
@app.get("/paginate/{start_id}/{end_id}")
def paginate(start_id: str, end_id: str):
    products = list(collection.find({"Product ID": {"$gte": start_id, "$lte": end_id}}, {"_id": 0}).limit(10))
    return products

# Convert product price from USD to EUR using exchange rate API
@app.get("/convert/{product_id}")
def convert(product_id: str):
    product = collection.find_one({"Product ID": product_id}, {"_id": 0})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch exchange rates")
    exchange_rate = response.json().get("rates", {}).get("EUR", 0.85)
    euro_price = product["Unit Price"] * exchange_rate
    return {"Product ID": product_id, "Name": product["Name"], "Price_EUR": round(euro_price, 2)}
