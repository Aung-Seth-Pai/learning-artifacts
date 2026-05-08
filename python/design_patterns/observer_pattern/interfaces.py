'''
Abstract interfaces for the Observer design pattern
'''

import abc
from abc import abstractmethod

class Observable(abc.ABC):
    '''Abstract interface for observable publisher objects'''
    @abstractmethod
    def add(self, observer):
        ''' Add an observer to the list of subscribers '''
        pass
    @abstractmethod
    def remove(self, observer):
        ''' Remove an observer from the list of subscribers '''
        pass
    @abstractmethod
    def notify(self):
        ''' Notify all observers about a change in state using callback '''
        pass

class Observer(abc.ABC):
    '''Abstract interface for observer subscriber objects'''
    @abstractmethod
    def update(self, subject):
        ''' callback method to update observer state '''
        pass