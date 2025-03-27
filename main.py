from typing import Union
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

# ✅ Get a single product by query parameter
@app.get("/getSingleProduct")
def get_single_product(id: str = Query(..., description="Product ID")):
    product = collection.find_one({"ProductID": id}, {"_id": 0})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# ✅ Get a single product by path parameter
@app.get("/getSingleProduct/{id}")
def get_single_product_path(id: str):
    product = collection.find_one({"ProductID": id}, {"_id": 0})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# ✅ Get all products
@app.get("/getAll")
def get_all():
    return list(collection.find({}, {"_id": 0}))

# ✅ Add a new product using JSON body (POST request)
@app.post("/addNew")
def add_new(product: Product):
    product_data = product.dict()
    
    # Check if product already exists
    existing_product = collection.find_one({"ProductID": product.ProductID})
    if existing_product:
        raise HTTPException(status_code=400, detail="Product already exists")
    
    # Insert into MongoDB
    collection.insert_one(product_data)
    return {"message": "Product added successfully"}

# ✅ Delete a product by ID
@app.delete("/deleteOne")
def delete_one(id: str):
    result = collection.delete_one({"ProductID": id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

# ✅ Get products starting with a specific letter (case-insensitive)
@app.get("/startsWith")
def starts_with(letter: str):
    return list(collection.find({"Name": {"$regex": f"^{letter}", "$options": "i"}}, {"_id": 0}))

# ✅ Paginate products by range of IDs
@app.get("/paginate")
def paginate(start_id: str, end_id: str):
    return list(collection.find({"ProductID": {"$gte": start_id, "$lte": end_id}}, {"_id": 0}).limit(10))

# ✅ Convert product price from USD to EUR using exchange rate API
@app.get("/convert")
def convert(id: str):
    product = collection.find_one({"ProductID": id}, {"_id": 0})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Fetch exchange rates
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch exchange rates")

    # Convert price to EUR
    exchange_rate = response.json().get("rates", {}).get("EUR", 0.85)
    euro_price = product["UnitPrice"] * exchange_rate
    return {"ProductID": id, "Name": product["Name"], "Price_EUR": round(euro_price, 2)}

# ✅ Example test route
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
