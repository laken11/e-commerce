class CreateOrderDto:
    customer_id: int
    product_name: int
    status: str
    paid: str
    shipping_address: str
    order_reference: str
    unit_price: float
    quantity: int
    customer_last_name: str


class EditOrderDto:
    customer_id: int
    product_name: int
    status: str
    paid: str
    shipping_address: str
    order_reference: str
    unit_price: float
    quantity: int


class ListOrderDto:
    paid: str
    shipping_address: str
    order_reference: str
    product_name: str
    customer_first_name: str
    customer_last_name: str
    status: str


class OrderDetailsDto:
    paid: str
    shipping_address: str
    order_reference: str
    product_name: str
    customer_first_name: str
    customer_last_name: str
    status: str

