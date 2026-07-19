import random
from datetime import datetime, timedelta

from services.seasonal_event_service import SeasonalEventService
from services.sale_service import SaleService
from services.product_service import ProductService


def generate_demo_sales():

    SaleService.delete_all_sales()

    products = ProductService.get_all_products()

    countries = [
        "Mali",
        "Burkina Faso",
        "Côte d'Ivoire",
        "Angola"
    ]

    start_date = datetime(2026, 1, 1)

    for product in products:

        product_id = product[0]

        current_date = start_date

        for _ in range(180):      # 180 days

            units = random.randint(10, 80)

            SaleService.add_sale(
                product_id=product_id,
                country=random.choice(countries),
                sale_date=current_date.strftime("%Y-%m-%d"),
                units_sold=units
            )

            current_date += timedelta(days=1)


def seed_database():

    print("Seeding demo products...")
    ProductService.seed_demo_products()

    print("Seeding seasonal events...")
    SeasonalEventService.seed_default_events()

    print("Generating demo sales...")
    generate_demo_sales()

    print("Database successfully seeded.")


if __name__ == "__main__":
    seed_database()