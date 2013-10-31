from droidable.hook import EventHook
from droidable.collection import Collection
from droidable.script import Script

class Droid:
    """Creates a droid"""
    _devices = {}
    _scripts = {}
    _conditions_tree = {}
    conditions_hashes = {}
    
    # Grouped by kind
    _triggers = {}
    _actions = {}
        
    def __init__(self, name = ""):
        self.generate_conditions()
        
    def add_device (self, device):
        self._devices[device.ID] = device

    def add_script (self, script):
        pass
        
    def generate_conditions(self):
        for script in self._scripts.iteritems():
            self.conditions_hashes[script.conditions_hash] = script
        
    def run():
        print "Droid running"
        
        for script in self._scripts: 
            pass            