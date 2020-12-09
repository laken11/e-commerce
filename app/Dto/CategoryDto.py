class RegisterCategoryDto:
    name: str
    parent: str


class EditCategoryDto:
    name: str
    parent: int


class CategoryDetailDto:
    id: int
    name: str
    parent: int


class ListCategoryDto:
    id: int
    name: str
    parent: int
