from abc import abstractmethod, ABCMeta
from app.repositories.CategoryReopsitory import CategoryRepository
from typing import List
from app.Dto.CategoryDto import EditCategoryDto, CategoryDetailDto, ListCategoryDto, RegisterCategoryDto


class CategoryManagementService(metaclass=ABCMeta):
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
    def get_sub_category(self, parent_id: int) -> List[ListCategoryDto]:
        """Return category object"""
        raise NotImplementedError


class DefaultCategoryManagementService(CategoryManagementService):
    repository: CategoryRepository

    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def register_category(self, model: RegisterCategoryDto):
        return self.repository.register_category(model)

    def edit_category(self, category_id: int, model: EditCategoryDto):
        return self.repository.edit_category(category_id, model)

    def list_category(self) -> List[ListCategoryDto]:
        return self.repository.list_category()

    def category_details(self, category_id: int) -> CategoryDetailDto:
        return self.repository.category_details(category_id)

    def get_category(self, name: str):
        return self.repository.get_category(name)

    def get_super_category(self) -> List[ListCategoryDto]:
        return self.repository.get_super_category()

    def get_sub_category(self, parent_id: int) -> List[ListCategoryDto]:
        return self.repository.get_sub_category(parent_id)
