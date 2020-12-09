class User:
    first_name: str
    last_name: str
    email: str
    username: str


class RegisterCustomerDto:
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str
    username: str
    address: str
    phone: str
    country: str
    state: str


class EditCustomerDto:
    id: int
    first_name: str
    last_name: str
    email: str
    username: str
    address: str
    phone: str
    country: str
    state: str


class ListCustomerDto:
    user: int
    address: str
    phone: str
    country: str
    state: str


class CustomerDetails:
    first_name: str
    last_name: str
    email: str
    username: str
    address: str
    phone: str
    country: str
    state: str
    user: int