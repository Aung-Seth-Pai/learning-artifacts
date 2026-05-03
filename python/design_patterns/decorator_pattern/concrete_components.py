from interfaces import BaseComponent

class ConcreteComponentA(BaseComponent):
    '''
    A Concrete Component provides an implementation of the Base Component
    interface. It defines the basic behavior that can be altered by
    decorators.
    '''
    def operation(self) -> str:
        return "Component A: I am result of basic operation."