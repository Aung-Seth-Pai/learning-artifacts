from interfaces import BaseComponent

class DecoratorComponent(BaseComponent):
    '''
    The base Decorator in follows the same interface as the other
    components. The primary purpose of this class is to define the wrapping
    interface for all concrete decorators. The default implementation of the
    wrapping code might include a field for storing a wrapped component and
    the means to initialize it.    
    '''
    def __init__(self, component: BaseComponent) -> None:
        '''Initialize the decorator with a component to wrap'''
        self._component = component

    def operation(self) -> str:
        '''Delegate the operation to the wrapped component we provided in constructor'''
        return self._component.operation()
    

class ConcreteDecoratorA(DecoratorComponent):
    '''
    A Concrete Decorator that adds responsibilities to the component
    dynamically.
    '''
    def operation(self) -> str:
        '''Extend the operation of the wrapped component'''
        # run base operation and get result
        base_result = self._component.operation()
        # perform decorator logic
        len_count = len(base_result) 

        return f"{base_result}\n \
            Behaviour added by : {self.__class__.__name__} with strlen = {len_count}"

class ConcreteDecoratorB(DecoratorComponent):
    '''
    Another Concrete Decorator that adds different responsibilities to
    the component dynamically.
    '''
    def operation(self) -> str:
        '''Extend the operation of the wrapped component'''

        # below two are interchangable since super() calls parent's method
        # base_result = self._component.operation()
        base_result = super().operation()
        
        space_count = base_result.count(' ')

        return f"{base_result}\n \
            Additional Behaviour added by : {self.__class__.__name__} with {space_count} spaces"