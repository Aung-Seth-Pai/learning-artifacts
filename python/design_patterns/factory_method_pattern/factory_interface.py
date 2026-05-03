from abc import ABC, abstractmethod
from product_interface import Product

class Creator(ABC):
    @abstractmethod
    def create_product(self, product_set: str="default") -> Product:
        """ must be implemented by subclasses and return a Product instance """
        pass

    def sample_operation(self, product_set: str="default") -> str:
        product = self.create_product(product_set)
        return (f"Product Name: {product.product_name()}\n"
                f"Description: {product.product_description()}\n"
                f"Price: ${product.product_price():.2f}")

