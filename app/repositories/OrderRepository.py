from abc import abstractmethod, ABCMeta
from app.Dto.OrderDto import EditOrderDto, ListOrderDto, CreateOrderDto, OrderDetailsDto
from app.models import Order, Product, Customer
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
        try:
            order = Order()
            product = Product.objects.get(name=model.product_name)
            customer = Customer.objects.get(customer__user__last_name=model.customer_last_name)
            order.customer_id = customer.id
            order.paid = model.paid
            order.status = model.status
            order.order_reference = model.order_reference
            order.shipping_address = model.shipping_address
            order.save()
            order.product.add(product, through_default={'unit_price': model.unit_price, 'quantity': model.quantity})
            return True
        except Order.DoesNotExist:
            return False

    def edit_order(self, order_id: int, model: EditOrderDto):
        try:
            order = Order.objects.get(id=order_id)
            try:
                product = Product.objects.get(name=model.product_name)
                order.paid = model.paid
                order.status = model.status
                order.shipping_address = model.shipping_address
                order.save()
                order.product.add(product, through_default={'unit_price': model.unit_price, 'quantity': model.quantity})
                return True
            except Product.DoesNotExist:
                return False
        except Order.DoesNotExist:
            return False

    def list_order(self) -> List[ListOrderDto]:
        orders = Order.objects.all()
        result: List[ListOrderDto] = []
        for order in orders:
            item = ListOrderDto()
            item.paid = order.paid
            item.status = order.status
            item.shipping_address = order.shipping_address
            item.product_name = order.product.name
            item.product = order.product.get(category__product__name=item.product_name)
            item.order_reference = order.order_reference
            item.customer_first_name = order.customer.user.first_name
            result.append(item)
        return result

    def order_details(self, order_id: int) -> OrderDetailsDto:
        try:
            order = Order.objects.get(id=order_id)
            result = OrderDetailsDto()
            result.customer_first_name = order.customer.user.first_name
            result.order_reference = order.order_reference
            result.paid = order.paid
            result.status = order.status
            result.shipping_address = order.shipping_address
            result.product_name = order.product.name
            result.product = order.product.get(category__product__name=result.product_name)
            result.customer_last_name = order.customer.user.last_name
            return result
        except Order.DoesNotExist as e:
            raise e

