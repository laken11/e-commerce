from app.Dto.ProductImageDto import RegisterImageUrl, EditImageUrl, ImageUrlDetails, ListImageUrl
from app.repositories.ProdutImageRepository import ProductImageRepository
from abc import ABCMeta, abstractmethod
from typing import List


class ProductImageManagementService(metaclass=ABCMeta):
    @abstractmethod
    def register_image(self, model: RegisterImageUrl):
        """Register Image Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_image(self,image_id: int, model: EditImageUrl):
        """Edit image object"""
        raise NotImplementedError

    @abstractmethod
    def list_image(self) -> List[ListImageUrl]:
        """List image Objects"""
        raise NotImplementedError

    @abstractmethod
    def image_details(self, image_id: int) -> ImageUrlDetails:
        """Return image object"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, image_id: int):
        """Delete image object"""
        raise NotImplementedError


class DefaultProductImageManagementService(ProductImageManagementService):
    repository: ProductImageRepository

    def __init__(self, repository: ProductImageRepository):
        self.repository = repository

    def register_image(self, model: RegisterImageUrl):
        return self.repository.register_image(model)

    def edit_image(self,image_id: int, model: EditImageUrl):
        return self.repository.edit_image(image_id, model)

    def list_image(self) -> List[ListImageUrl]:
        return self.repository.list_image()

    def image_details(self, image_id: int) -> ImageUrlDetails:
        return self.repository.image_details(image_id)

    def delete(self, image_id: int):
        return self.repository.delete(image_id)
