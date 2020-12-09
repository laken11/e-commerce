from abc import ABCMeta, abstractmethod
from typing import List
from app.Dto.CustomerDto import EditCustomerDto, ListCustomerDto, RegisterCustomerDto, CustomerDetails
from app.repositories.CustomerRepository import CustomerRepository


class CustomerManagementService(metaclass=ABCMeta):
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
        """Delete customer object"""
        raise NotImplementedError


class DefaultCustomerManagementService(CustomerManagementService):
    repository: CustomerRepository

    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def register_customer(self, model: RegisterCustomerDto):
        return self.repository.register_customer(model)

    def edit_customer(self, model: EditCustomerDto, customer_id: int):
        return self.repository.edit_customer(model, customer_id=customer_id)

    def list_customers(self) -> List[ListCustomerDto]:
        return self.repository.list_customers()

    def customer_details(self, customer_id: int) -> CustomerDetails:
        return self.repository.customer_details(customer_id=customer_id)

    def delete_customer(self, customer_id: int):
        return self.repository.delete_customer(customer_id)
