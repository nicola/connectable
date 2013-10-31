from droidable.hook import EventHook
from droidable.collection import Collection
from droidable.script import Script

class Droid:
    """Creates a droid"""
    _devices = Collection()
    _scripts = Collection()
    
    # Grouped by kind
    _triggers = {}
    _actions = {}
        
    def __init__(self, name = ""):
        pass
        
    def add_device (self, device):
        _devices.add(device)

    def add_script (self, script):
        _scripts.add(script)
        
    def run():
        print "Droid running"
        
        for script in _scripts: 
            pass            