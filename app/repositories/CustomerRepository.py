from abc import ABCMeta, abstractmethod
from typing import List
from app.models import Customer
from app.Dto.CustomerDto import CustomerDetails, EditCustomerDto, ListCustomerDto, RegisterCustomerDto
from django.contrib.auth.models import User, Group

from app.serializer import CustomerSerializer


class CustomerRepository(metaclass=ABCMeta):
    @abstractmethod
    def register_customer(self, model: RegisterCustomerDto):
        """Register Customer Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_customer(self, model: EditCustomerDto, customer_id: int):
        """Edit Customer Object"""
        raise NotImplementedError

    @abstractmethod
    def customer_details(self, customer_id: int) -> CustomerDetails:
        """Return Customer Object"""
        raise NotImplementedError

    @abstractmethod
    def list_customers(self) -> List[ListCustomerDto]:
        """List Customer Objects"""
        raise NotImplementedError

    @abstractmethod
    def delete_customer(self, customer_id: int):
        """Delete Customer Object"""
        return NotImplementedError


class DjangoORMCustomerRepository(CustomerRepository):
    def register_customer(self, model: RegisterCustomerDto):
        customer = Customer()
        customer.state = model.state
        customer.address = model.address
        customer.phone = model.phone
        customer.country = model.country
        user = User.objects.create_user(model.username, model.email, model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.save()
        data = {
            'state': customer.state,
            'address': customer.address,
            'phone': customer.phone,
            'country': customer.country,
            'user_id': user.id
        }
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer
        return serializer

    def edit_customer(self, model: EditCustomerDto, customer_id: int):
        try:
            customer = Customer.objects.get(pk=customer_id)
            user = customer.user
            user.last_name = model.last_name
            user.first_name = model.first_name
            user.email = model.email
            user.username = model.username
            user.save()
            customer.state = model.state
            customer.address = model.address
            customer.phone = model.phone
            customer.country = model.country
            data = {
                'state': customer.state,
                'phone': customer.phone,
                'country': customer.country,
                'address': customer.address,
                'user_id': user.id
            }
            serializer = CustomerSerializer(customer, data=data)
            if serializer.is_valid():
                serializer.save()
                return serializer
            return serializer
        except Customer.DoesNotExist as e:
            message = 'Customer Dose Not exit'
            print(message)
            raise e

    def customer_details(self, customer_id: int) -> CustomerDetails:
        try:
            customer = Customer.objects.get(pk=customer_id)
            result = CustomerDetails()
            result.address = customer.address
            result.phone = customer.phone
            result.country = customer.country
            result.state = customer.state
            user_id = customer.user.id
            result.user = User.objects.get(id=user_id)
            return result
        except Customer.DoesNotExist as e:
            message = 'Customer Dose Not exit'
            print(message)
            raise e

    def list_customers(self) -> List[ListCustomerDto]:
        customers = Customer.objects.all()
        result: List[ListCustomerDto] = []
        for customer in customers:
            user_id = customer.user.pk
            item = ListCustomerDto()
            item.user = User.objects.get(pk=user_id)
            item.address = customer.address
            item.phone = customer.phone
            item.state = customer.state
            item.country = customer.country
            result.append(item)
        return result

    def delete_customer(self, customer_id: int):
        try:
            customer = Customer.objects.get(id=customer_id)
            customer.delete()
            return True
        except Customer.DoesNotExist as e:
            message = 'Customer dose not exit'
            print(message)
            raise e





