from droidable.hook import EventHook
from droidable.device import DeviceCollection

class Droid:
    """Creates a droid"""
    _devices = DeviceCollection()
    
    def plug(self):
        pass
    
    def unplug(self):
        pass
        
    def __init__(self, name):
        self.name = name