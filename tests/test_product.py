import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.product import Product
from services.product_service import ProductService


oreo = Product(
    product_name="Oreo Chocolate Biscuit",
    category="Biscuit",
    brand="Oreo",
    supplier_country="Turkey",
    destination_country="Mali",
    quantity=500,
    unit="Cartons",
    cost_price=12,
    selling_price=18,
    manufacture_date="2026-07-01",
    expiry_date="2027-07-01",
    warehouse="Bamako Warehouse",
    status="Available"
)

ProductService.add_product(oreo)

print("✅ Product added successfully!")