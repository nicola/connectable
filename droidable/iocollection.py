from droidable.hook import EventHook

class IOCollection(object):
    onAdded = EventHook()
    onRemoved = EventHook()
    
    def __init__(self, collection = {}):
        self._collection = collection
        
    def get(self, name):
        return self._collection[name];
        
    def add(self, name, path):
        self._collection[name] = path
        self.onAdded.fire(name=name)
        
    def remove(self, name):
        del self._collection[name]
        self.onRemoved.fire(name=name)
        
    def collection(self):
        return self._collection

class InputCollection(IOCollection):
    def __init__(self, collection = {}):
        super(InputCollection, self).__init__(collection)
        
class OutputCollection(IOCollection):
    def __init__(self, collection = {}):
        super(OutputCollection, self).__init__(collection)