from dataclasses import dataclass

@dataclass
class User:
    email: str
    username: str
    password: str
    firstname: str
    lastname: str
    city: str
    street: str
    number: int
    zipcode: str
    lat: str
    long: str
    phone: str

