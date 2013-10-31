from droidable.hook import EventHook

class Device(object):
    def __init__(self, dictionary, path = None):
        if (path is not None):
            self.device = self.name = dictionary;
            self.path = path
            
        if ('name'    in dictionary):     self.name = dictionary['name']
        if ('mac'     in dictionary):      self.mac = dictionary['mac']
        if ('type'    in dictionary):     self.type = dictionary['type']
        if ('triggers'in dictionary): self.triggers = dictionary['triggers']
        if ('actions' in dictionary):  self.actions = dictionary['actions']
        
class DeviceCollection(object):
    onAdded = EventHook()
    onRemoved = EventHook()

    def __init__(self, collection = {}):
        self._collection = collection

    def get(self, name):
        return self._collection[name];

    def add(self, device, path = None):
        if (path is not None): device = Device(device, path)
        self._collection[device.name] = device
        self.onAdded.fire(name=device.name)

    def remove(self, name):
        del self._collection[name]
        self.onRemoved.fire(name=name)

    def collection(self):
        return self._collection