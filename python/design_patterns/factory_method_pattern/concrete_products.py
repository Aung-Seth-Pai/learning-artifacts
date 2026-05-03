from product_interface import Product

class ConcreteProductA(Product):
    def __init__(self, mode: str = "basic"):
        self.mode = mode
    def product_name(self) -> str:
        return "Concrete Product A"
    def product_description(self) -> str:
        return f"Product A running in {self.mode} mode"
    def product_price(self) -> float:
        return 29.99 if self.mode == "basic" else 59.99


class ConcreteProductB(Product):
    def __init__(self, variant: str = "standard"):
        self.variant = variant
    def product_name(self) -> str:
        return "Concrete Product B"
    def product_description(self) -> str:
        return f"Product B of {self.variant} variant"
    def product_price(self) -> float:
        return 49.99 if self.variant == "standard" else 79.99


class ConcreteProductC(Product):
    def __init__(self, style: str = "modern"):
        self.style = style
    def product_name(self) -> str:
        return "Concrete Product C"
    def product_description(self) -> str:
        return f"Product C with {self.style} style"
    def product_price(self) -> float:
        return 39.99 if self.style == "modern" else 69.99