from droidable.hook import EventHook
from droidable.device import InputDevice
from droidable.device import OutputDevice

class IOCollection(object):
    onAdded = EventHook()
    onRemoved = EventHook()
    
    def __init__(self, collection = {}):
        self._collection = collection
        
    def get(self, name):
        return self._collection[name];
        
    def add(self, device):
        self._collection[device.name] = device
        self.onAdded.fire(name=device.name)
        
    def remove(self, name):
        del self._collection[name]
        self.onRemoved.fire(name=name)
        
    def collection(self):
        return self._collection

class InputCollection(IOCollection):
    def __init__(self, collection = {}):
        super(InputCollection, self).__init__(collection)
    
    def add(self, device, path = None):
        if (path is not None): device = InputDevice(device, path)
        IOCollection.add(self, device)
        
class OutputCollection(IOCollection):
    def __init__(self, collection = {}):
        super(OutputCollection, self).__init__(collection)
        
    def add(self, device, path = None):
        if (path is not None): device = OutputDevice(device, path)
        IOCollection.add(self, device)