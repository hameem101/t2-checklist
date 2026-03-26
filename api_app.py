from fastapi import FastAPI
from pydantic import BaseModel
import database_app
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="Retail Backend API")
# from here copy 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# till here

# ---------- DATA MODELS ----------
 
class Category(BaseModel):
    name: str
    description: str | None = None
 
 
class Product(BaseModel):
    name: str
    category_id: int
    price: float
    stock: int
    description: str | None = None
 
 
class Customer(BaseModel):
    email: str
    first_name: str
    last_name: str
    city: str | None = None
    country: str | None = None
 
 
# ---------- CATEGORY ENDPOINTS ----------
 
@app.get("/categories")
def get_categories():
    data = database_app.get_categories()
    return [
        {"id": c[0], "name": c[1], "description": c[2]}
        for c in data
    ]
 
 
@app.post("/categories")
def create_category(category: Category):
    database_app.add_category(category.name, category.description)
    return {"message": "Category created"}
 
 
# ---------- PRODUCT ENDPOINTS ----------
 
@app.get("/products")
def get_products():
    data = database_app.get_products_with_categories()
    return [
        {
            "id": p[0],
            "product_name": p[1],
            "category_name": p[2],
            "price": p[3],
            "stock": p[4]
        }
        for p in data
    ]
 
 
@app.post("/products")
def create_product(product: Product):
    database_app.add_product(
        product.name,
        product.category_id,
        product.price,
        product.stock,
        product.description
    )
    return {"message": "Product created"}
 
 
# ---------- CUSTOMER ENDPOINTS ----------
 
@app.get("/customers")
def get_customers():
    data = database_app.get_customers()
    return [
        {
            "id": c[0],
            "email": c[1],
            "first_name": c[2],
            "last_name": c[3],
            "city": c[4],
            "country": c[5]
        }
        for c in data
    ]
 
 
@app.post("/customers")
def create_customer(customer: Customer):
    database_app.add_customer(
        customer.email,
        customer.first_name,
        customer.last_name,
        customer.city,
        customer.country
    )
    return {"message": "Customer created"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)