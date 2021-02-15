from abc import ABCMeta, abstractmethod
from app.Dto.OrderDto import EditOrderDto, ListOrderDto, OrderDetailsDto, CreateOrderDto
from app.repositories.OrderRepository import OrderRepository
from typing import List


class OrderManagementService(metaclass=ABCMeta):
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


class DefaultOrderManagementService(OrderManagementService):
    repository: OrderRepository

    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(self, model: CreateOrderDto):
        return self.repository.create_order(model)

    def edit_order(self, order_id: int, model: EditOrderDto):
        return self.repository.edit_order(order_id, model)

    def list_order(self) -> List[ListOrderDto]:
        return self.repository.list_order()

    def order_details(self, order_id: int) -> OrderDetailsDto:
        return self.repository.order_details(order_id)
