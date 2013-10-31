from droidable.hook import EventHook
from droidable.collection import Collection
from droidable.script import Script

class Droid:
    """Creates a droid"""
    _devices = Collection()
    _scripts = Collection()
    _conditions_tree = {}
    _conditions_hashes = {}
    
    # Grouped by kind
    _triggers = {}
    _actions = {}
        
    def __init__(self, name = ""):
        self.generate_conditions()
        
    def add_device (self, device):
        _devices.add(device)

    def add_script (self, script):
        _scripts.add(script)
        
    def generate_conditions(self):
        for script in _script.collection():
            print script.conditions_hash
        
    def run():
        print "Droid running"
        
        for script in _scripts: 
            pass            