from abc import abstractmethod, ABCMeta
from app.Dto.OrderDto import EditOrderDto, ListOrderDto, CreateOrderDto, OrderDetailsDto
from app.models import Order
from typing import List


class OrderRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_order(self, model: CreateOrderDto):
        """Create Order Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_order(self, order_id: int, model: EditOrderDto):
        """Edit Order Object"""
        raise NotImplementedError

    @abstractmethod
    def list_order(self) -> List[ListOrderDto]:
        """List Order Objects"""
        raise NotImplementedError

    @abstractmethod
    def order_details(self, order_id: int) -> OrderDetailsDto:
        """Return Order Object"""
        raise NotImplementedError


class DjangoORMOrderRepository(OrderRepository):
    def create_order(self, model: CreateOrderDto):
        order = Order()
        order.status = model.status
        order.customer_id = model.customer_id
        order.order_reference = model.order_reference
        order.paid = model.paid
        order.order_reference = order.order_reference
