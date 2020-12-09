from typing import List
from app.models import Product, Category, ProductImage
from app.Dto.ProductDto import CreateProductDto, EditProductDto, ListProductDto, ProductDetailsDto
from abc import ABCMeta, abstractmethod
from app.serializer import ProductSerializer


class ProductRepository(metaclass=ABCMeta):
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


class DjangoORMProductRepository(ProductRepository):
    def create_product(self, model: CreateProductDto):
        try:
            image = ProductImage.objects.get(name=model.image_name)
            try:
                category_name = model.category_name
                category = Category.objects.get(name=category_name)
                product = Product()
                product.ProductImage_id = image.id
                product.name = model.name
                product.price = model.price
                product.description = model.description
                product.save()
                product.category.add(category)
                return True
            except Category.DoesNotExist:
                return False
        except ProductImage.DoesNotExist:
            return False

    def edit_product(self, product_id: int, model: EditProductDto):
        try:
            product = Product.objects.get(id=product_id)
            try:
                image = ProductImage.objects.get(name=model.image_name)
                try:
                    category = Category.objects.get(name=model.category_name)
                    product.ProductImage_id = image.id
                    product.name = model.name
                    product.price = model.price
                    product.description = model.description
                    product.save()
                    product.category.add(category)
                    return True
                except Category.DoesNotExist:
                    return False
            except ProductImage.DoesNotExist:
                return False
        except Product.DoesNotExist:
            return False

    def list_product(self) -> List[ListProductDto]:
        products = Product.objects.all()
        result: List[ListProductDto] = []
        for product in products:
            item = ListProductDto()
            item.id = product.id
            item.name = product.name
            item.price = product.price
            item.description = product.description
            item.product_image = product.ProductImage
            item.category = product.category.get(product__name=item.name)
            item.id = product.id
            result.append(item)
        return result

    def product_details(self, product_id: int):
        try:
            product = Product.objects.get(id=product_id)
            result = ProductDetailsDto()
            result.name = product.name
            result.id = product.id
            result.product_image = product.ProductImage
            result.description = product.description
            result.category = product.category.get(product__name=result.name)
            result.price = product.price
            return result
        except Product.DoesNotExist:
            return False

    def delete_product(self, product_id: int):
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return True
        except Product.DoesNotExist:
            return False
