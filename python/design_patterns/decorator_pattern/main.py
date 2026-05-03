from concrete_components import ConcreteComponentA
from decorators import ConcreteDecoratorA, ConcreteDecoratorB

def main():
    # Create concrete components
    base_object = ConcreteComponentA()

    # Create decorators
    a_decorated_base_obj = ConcreteDecoratorA(base_object)
    b_decorated_base_obj = ConcreteDecoratorB(base_object)
    
    # run with additional behavior from ConcreteDecoratorA
    print(a_decorated_base_obj.operation())
    # run with additional behavior from ConcreteDecoratorB
    print(b_decorated_base_obj.operation())

    print("\n----- Combining Multiple Decorators -----")

    # decorate the already decorated object with another decorator
    ab_decorated_base_obj = ConcreteDecoratorB(a_decorated_base_obj)
    print(ab_decorated_base_obj.operation())

    print("\n----- Combining Multiple Decorators in different order -----")
    # decorate the already decorated object with another decorator
    aba_decorated_base_obj = ConcreteDecoratorA(ab_decorated_base_obj)
    print(aba_decorated_base_obj.operation())

if __name__ == "__main__":
    main()

