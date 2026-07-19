from services.sale_service import SaleService

SaleService.delete_all_sales()

SaleService.add_sale(
    product_id=1,
    country="Mali",
    sale_date="2026-01-15",
    units_sold=120
)

sales = SaleService.get_sales()

for sale in sales:
    print(sale)