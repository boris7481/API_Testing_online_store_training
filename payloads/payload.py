from itertools import product
from datamodels import product

from faker import Faker
import random


class Payload:
    faker = Faker()
    categories = ["electronis", "furniture", "books", "beauty"]

    def product_payload(self) -> product:
        title = self.faker.unique.catch_phrase()
        price = float(self.faker.pricetag().replace("$", "").replace(",", ""))
        description = self.faker.sentence()
        image_url = "https://i.pravatar.cc/100"
        category = random.choice(self.faker.categories)
        return product(title, price, description, image_url, category)
