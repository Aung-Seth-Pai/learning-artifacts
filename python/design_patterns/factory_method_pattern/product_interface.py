from abc import ABC, abstractmethod

class Product(ABC):
    '''Product Interface defining the methods for products'''
    @abstractmethod
    def product_name(self) -> str:
        pass
    @abstractmethod
    def product_description(self) -> str:
        pass
    @abstractmethod
    def product_price(self) -> float:
        pass