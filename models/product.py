class Product:

    def __init__(
        self,
        product_name,
        category,
        brand,
        supplier_country,
        destination_country,
        quantity,
        unit,
        cost_price,
        selling_price,
        manufacture_date,
        expiry_date,
        warehouse,
        status,
        product_id=None
    ):

        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.brand = brand
        self.supplier_country = supplier_country
        self.destination_country = destination_country
        self.quantity = quantity
        self.unit = unit
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.manufacture_date = manufacture_date
        self.expiry_date = expiry_date
        self.warehouse = warehouse
        self.status = status