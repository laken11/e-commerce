from app.repositories.ProductReopsitory import ProductRepository
from app.Dto.ProductDto import CreateProductDto, ProductDetailsDto, ListProductDto, EditProductDto
from typing import List
from abc import abstractmethod, ABCMeta


class ProductManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_product(self, model: CreateProductDto):
        """Create Product Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_product(self, product_id: int, model: EditProductDto):
        """Edit Product Object"""
        raise NotImplementedError

    @abstractmethod
    def product_details(self, product_id: int):
        """Return Product Object"""
        raise NotImplementedError

    @abstractmethod
    def list_product(self) -> List[ListProductDto]:
        """List Product Objects"""
        raise NotImplementedError

    @abstractmethod
    def delete_product(self, product_id: int):
        """Delete Product Object"""
        raise NotImplementedError


class DefaultProductManagementService(ProductManagementService):
    repository: ProductRepository

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(self, model: CreateProductDto):
        return self.repository.create_product(model)

    def edit_product(self, product_id: int, model: EditProductDto):
        return self.repository.edit_product(product_id, model)

    def list_product(self) -> List[ListProductDto]:
        return self.repository.list_product()

    def product_details(self, product_id: int):
        return self.repository.product_details(product_id)

    def delete_product(self, product_id: int):
        return self.repository.delete_product(product_id)
