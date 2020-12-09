class CreateOrderDto:
    customer_id: int
    product_id: int
    status: str
    paid: str
    shipping_address: str
    order_reference: str


class EditOrderDto:
    product_id: str
    status: str
    paid: str
    shipping_address: str
    order_reference: str
    status: str


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

