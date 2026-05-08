from interfaces import Observable, Observer

class Publisher(Observable):
    '''
        Concrete implementation of an observable publisher
        in this, the publisher maintains a list of observers 
        and notifies them of changes in its internal state data
    '''
    def __init__(self):
        self._observers = [] # List of observer subscribers
        self._data = None # Internal state data

    def add(self, observer: Observer):
        ''' Add an observer to the list of subscribers '''
        if observer not in self._observers:
            self._observers.append(observer) 

    def remove(self, observer: Observer):
        ''' Remove an observer from the list of subscribers '''
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        ''' Notify all observers about a change in state using callback '''
        for observer in self._observers:
            observer.update(self)

    def set_data(self, data):
        ''' Set internal state data and notify observers '''
        self._data = data
        self.notify() # notify will be called whenever we set new data

    def get_data(self):
        ''' Get current internal state data '''
        return self._data
    
    # the following methods are for better debugging and testing
    # they are not strictly necessary for the Observer pattern
    def __str__(self): 
        return f"Publisher({self._data})"
    def __repr__(self): 
        return self.__str__()
    def __eq__(self, other):
        if isinstance(other, Publisher):
            return self._data == other._data
        return False
    def __hash__(self):
        return hash(self._data)
