class CreateProductDto:
    name: str
    price: float
    description: str
    image_name: str
    category_name: str


class EditProductDto:
    name: str
    price: float
    description: str
    image_name: str
    category_name: str


class ListProductDto:
    id: int
    name: str
    price: float
    description: str
    category: int
    product_image: str


class ProductDetailsDto:
    id: int
    name: str
    price: float
    description: str
    category_name: str
    product_image: str
