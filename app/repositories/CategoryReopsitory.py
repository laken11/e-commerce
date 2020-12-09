from app.serializer import CategorySerializer
from app.models import Category
from app.Dto.CategoryDto import CategoryDetailDto, EditCategoryDto, ListCategoryDto, RegisterCategoryDto
from typing import List
from abc import ABCMeta, abstractmethod


class CategoryRepository(metaclass=ABCMeta):
    @abstractmethod
    def register_category(self, model: RegisterCategoryDto):
        """Register Category Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_category(self, category_id: int, model: EditCategoryDto):
        """Edit Category Object"""
        raise NotImplementedError

    @abstractmethod
    def list_category(self) -> List[ListCategoryDto]:
        """List Category Object"""
        raise NotImplementedError

    @abstractmethod
    def category_details(self, category_id: int) -> CategoryDetailDto:
        """Return Category Object"""
        raise NotImplementedError

    @abstractmethod
    def get_category(self, name: str):
        """Return Category Object"""
        raise NotImplementedError

    @abstractmethod
    def get_super_category(self) -> List[ListCategoryDto]:
        """Return Category Object"""
        raise NotImplementedError

    @abstractmethod
    def get_sub_category(self, parent_id: int):
        """Return category object"""
        raise NotImplementedError


class DjangoORMCategoryRepository(CategoryRepository):
    def register_category(self, model: RegisterCategoryDto):
        try:
            parent = Category.objects.get(name=model.parent)
            parent_id = parent.id
            data = {
                "name": model.name,
                "parent": parent_id
            }
            serializer = CategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                saved = True
                return saved
            saved = False
            return saved
        except Category.DoesNotExist:
            data = {
                "name": model.name,
                "parent": ""
            }
            serializer = CategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                saved = True
                return saved
            saved = False
            return saved

    def edit_category(self, category_id: int, model: EditCategoryDto):
        try:
            category = Category.objects.get(id=category_id)
            data = {
                "name": model.name,
                "parent": model.parent
            }
            serializer = CategorySerializer(category, data=data)
            if serializer.is_valid():
                serializer.save()
                saved = True
                return saved
            saved = False
            return saved
        except Category.DoesNotExist as e:
            message = "Category dose not exit"
            print(message)
            raise e

    def list_category(self) -> List[ListCategoryDto]:
        categorys = Category.objects.all()
        result: List[ListCategoryDto] = []
        for record in categorys:
            item = ListCategoryDto()
            item.parent = record.parent
            item.name = record.name
            result.append(item)
        return result

    def category_details(self, category_id: int) -> CategoryDetailDto:
        try:
            category = Category.objects.get(id=category_id)
            result = CategoryDetailDto()
            result.name = category.name
            result.parent = category.parent
            return result
        except Category.DoesNotExist as e:
            message = "Category dose not exit"
            print(message)
            raise e

    def get_category(self, name: str) -> CategoryDetailDto():
        try:
            category = Category.objects.get(name=name)
            result = CategoryDetailDto()
            result.name = category.name
            result.parent = category.parent
            result.id = category.id
            return result
        except Category.DoesNotExist as e:
            raise e

    def get_super_category(self) -> List[ListCategoryDto]:
        try:
            categorys = Category.objects.filter(parent_id__isnull=True)
            result: List[ListCategoryDto] = []
            for category in categorys:
                item = ListCategoryDto()
                item.name = category.name
                item.parent = category.parent
                item.id = category.id
                result.append(item)
            return result
        except Category.DoesNotExist:
            return []

    def get_sub_category(self, parent_id: int) -> List[ListCategoryDto]:
        try:
            categorys = Category.objects.filter(parent_id=parent_id)
            result: List[ListCategoryDto] = []
            for category in categorys:
                item = ListCategoryDto()
                item.id = category.id
                item.name = category.name
                item.parent = category.parent
                item.id = category.id
                result.append(item)
            return result
        except Category.DoesNotExist:
            return []

