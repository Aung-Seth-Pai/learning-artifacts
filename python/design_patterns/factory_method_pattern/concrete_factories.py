from factory_interface import Creator
from product_interface import Product
from concrete_products import ConcreteProductA, ConcreteProductB, ConcreteProductC

class ConcreteCreatorA(Creator):
    def create_product(self, product_set: str = "premium") -> Product:
        if product_set == "premium":
            return ConcreteProductA(mode="advanced")
        elif product_set == "basic":
            return ConcreteProductA(mode="basic")
        else:
            # raise an error for undefined product sets
            raise ValueError(f"Unknown product set: {product_set}")

class ConcreteCreatorB(Creator):
    def create_product(self, product_set: str = "standard") -> Product:
        if product_set == "standard":
            return ConcreteProductB(variant="standard")
        elif product_set == "deluxe":
            return ConcreteProductB(variant="deluxe")
        else:
            raise ValueError(f"Unknown product set: {product_set}")

class ConcreteCreatorC(Creator):
    def create_product(self, product_set: str = "modern") -> Product:
        if product_set == "modern":
            return ConcreteProductC(style="modern")
        elif product_set == "classic":
            return ConcreteProductC(style="classic")
        else:
            raise ValueError(f"Unknown product set: {product_set}")