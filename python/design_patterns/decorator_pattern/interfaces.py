from abc import ABC, abstractmethod

class BaseComponent(ABC):
    '''
    The base Component interface defines the basic operations that can be
    altered by decorators.
    '''
    @abstractmethod
    def operation(self) -> str:
        pass
