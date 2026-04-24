from dataclasses import dataclass

@dataclass
class Product:
    title: str
    description: str
    price: float
    imaage: str
    category: str