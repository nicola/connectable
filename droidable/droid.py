from droidable.hook import EventHook
from droidable.collection import Collection

class Droid:
    """Creates a droid"""
    _devices = Collection()
    _scripts = Collection()
        
    def __init__(self, name):
        pass
        
    def add_device (self, device):
        _devices.add(device)