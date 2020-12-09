from dependency_injector import containers, providers
from typing import Callable
from app.repositories.CustomerRepository import CustomerRepository, DjangoORMCustomerRepository
from app.services.CustomerManagementService import CustomerManagementService, DefaultCustomerManagementService
from app.services.ProductImageManagementService import ProductImageManagementService, \
    DefaultProductImageManagementService
from app.repositories.ProdutImageRepository import ProductImageRepository, DjangoORMProductImageRepository
from app.repositories.CategoryReopsitory import CategoryRepository, DjangoORMCategoryRepository
from app.services.CategoryManagementService import CategoryManagementService, DefaultCategoryManagementService
from app.repositories.ProductReopsitory import DjangoORMProductRepository, ProductRepository
from app.services.ProductManagementService import ProductManagementService, DefaultProductManagementService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    customer_repository: Callable[[], CustomerRepository] = providers.Factory(
        DjangoORMCustomerRepository
    )
    customer_management_service: Callable[[], CustomerManagementService] = providers.Factory(
        DefaultCustomerManagementService,
        repository=customer_repository
    )
    product_image_repository: Callable[[], ProductImageRepository] = providers.Factory(
        DjangoORMProductImageRepository
    )
    product_image_management_service: Callable[[], ProductImageManagementService] = providers.Factory(
        DefaultProductImageManagementService,
        repository=product_image_repository
    )
    category_repository: Callable[[], CategoryRepository] = providers.Factory(
        DjangoORMCategoryRepository
    )
    category_management_service: Callable[[], CategoryManagementService] = providers.Factory(
        DefaultCategoryManagementService,
        repository=category_repository
    )
    product_repository: Callable[[], ProductRepository] = providers.Factory(
        DjangoORMProductRepository
    )
    product_management_service: Callable[[], ProductManagementService] = providers.Factory(
        DefaultProductManagementService,
        repository=product_repository
    )


app_service_provider = Container()
