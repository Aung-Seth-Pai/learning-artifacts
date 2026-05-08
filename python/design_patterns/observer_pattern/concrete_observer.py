from interfaces import Observer

class Subscriber(Observer):
    '''
        Concrete implementation of an observer subscriber
        in this, the subscriber maintains a reference to the publisher
        and updates its internal state when notified of changes in the publisher's state
        the reference to publisher is not necessary but is useful allowing the subscriber
        to subscribe and unsubscribe itself from the publisher
    '''
    def __init__(self, name, publisher):
        ''' Initialize subscriber with a name and reference to publisher '''
        self._name = name
        self._publisher = publisher
        self._state = None # Internal state of the subscriber
        publisher.add(self) # Automatically subscribe to the publisher upon creation
    def update(self, subject):
        ''' callback method to update observer state '''
        self._state = subject.get_data()
        print(f"Subscriber {self._name} received update: {self._state}")
    def get_state(self):
        ''' Get current state of the subscriber '''
        return self._state
    def unsubscribe(self):
        ''' Unsubscribe from the publisher '''
        self._publisher.remove(self)
    def subscribe(self):
        ''' Subscribe to the publisher '''
        self._publisher.add(self)

    # the following methods are for better debugging and testing
    # they are not strictly necessary for the Observer pattern
    def __str__(self):
        return f"Subscriber({self._name})"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        ''' Check equality based on name '''
        if isinstance(other, Subscriber):
            return self._name == other._name
        return False
    def __hash__(self):
        ''' Hash based on name : this allows usage in sets and as dict keys '''
        return hash(self._name)