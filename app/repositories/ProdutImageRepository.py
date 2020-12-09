from app.Dto.ProductImageDto import EditImageUrl, ListImageUrl, ImageUrlDetails, RegisterImageUrl
from app.models import ProductImage
from abc import abstractmethod, ABCMeta
from typing import List

from app.serializer import ProductImageSerializer


class ProductImageRepository(metaclass=ABCMeta):
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


class DjangoORMProductImageRepository(ProductImageRepository):
    def register_image(self, model: RegisterImageUrl):
        image = ProductImage()
        image.name = model.name
        image.file = model.file
        data = {
            'name': image.name,
            'file': image.file
        }
        serializer = ProductImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            saved = True
            return saved
        saved = False
        return saved

    def edit_image(self, image_id: int, model: EditImageUrl):
        image = ProductImage.objects.get(id=image_id)
        image.name = model.name
        image.file = model.file
        data = {
            'name': model.name,
            'file': model.file
        }
        serializer = ProductImageSerializer(image, data=data)
        if serializer.is_valid():
            serializer.save()
            saved = True
            return saved
        saved = False
        return saved

    def list_image(self) -> List[ListImageUrl]:
        images = ProductImage.objects.all()
        results: List[ListImageUrl] = []
        for result in images:
            item = ListImageUrl()
            item.file = result.file
            item.name = result.name
            results.append(item)
        return results

    def image_details(self, image_id: int) -> ImageUrlDetails:
        try:
            image = ProductImage.objects.get(id=image_id)
            result = ImageUrlDetails()
            result.file = image.file
            result.name = image.name
            return result
        except ProductImage.DoesNotExist as e:
            message = "Image dose not exit"
            print(message)
            raise e

    def delete(self, image_id: int):
        try:
            ProductImage.objects.get(id=image_id).delete()
        except ProductImage.DoesNotExist as e:
            message = "Image dose not exit"
            print(message)
            raise e

