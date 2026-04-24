from itertools import product
from datamodels.product import Product
from datamodels.cart import Cart
from datamodels.user import User

from faker import Faker
import random


class Payload:
    faker = Faker()
    categories = ["electronis", "furniture", "books", "beauty"]

    def product_payload(self) -> Product:
        title = self.faker.unique.catch_phrase()
        price = float(self.faker.pricetag().replace("$", "").replace(",", ""))
        description = self.faker.sentence()
        image_url = "https://i.pravatar.cc/100"
        category = random.choice(self.categories)
        return Product(title, description, price, image_url, category)

    def user_payload(self) -> User:
        email = self.faker.unique.email()
        username = self.faker.user_name()
        password = self.faker.password()

        firstname = self.faker.first_name()
        lastname = self.faker.last_name()

        city = self.faker.city()
        street = self.faker.street_name()
        number = random.randint(1, 9999)
        zipcode = self.faker.postcode()

        lat = str(self.faker.latitude())
        long = str(self.faker.longitude())

        phone = self.faker.phone_number()

        return User( email, username, password, firstname, lastname,  city, street,  number, zipcode,  lat, long, phone)

    def cart_payload(self) -> Cart:
        user_id = random.randint(1, 10)
        date = self.faker.date()
        products = [
            {
                "productId": random.randint(1, 20),
                "quantity": random.randint(1, 5)
            }
        ]
        return Cart(user_id, date, products)
