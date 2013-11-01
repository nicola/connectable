from connectable.hook import EventHook
from connectable.collection import Collection
from connectable.script import Script

def deepupdate(original, update):
    """
    Recursively update a dict.
    Subdict's won't be overwritten but also updated.
    """
    for key, value in original.iteritems(): 
        if not key in update:
            update[key] = value
        elif isinstance(value, dict):
            deepupdate(value, update[key]) 
    return update

class Droid:
    """Creates a droid"""
        
    def __init__(self, name = ""):
        self._devices = {}
        self._scripts = {}
        self.conditions_tree = {}
        self.conditions_hashes = {}
    
        # Grouped by kind
        self._triggers = {}
        self._actions = {}
        self.generate_conditions()
        
    def add_device (self, device):
        self._devices[device.ID] = device

    def add_script (self, script):
        self._scripts[script.ID] = script
        self.generate_conditions()
        
    def generate_conditions(self):
        self.conditions_hashes = {}
        self.conditions_tree = {}
        for (script_name, script) in self._scripts.iteritems():
            self.conditions_hashes[script.conditions_hash] = script.actions
            self.conditions_tree = deepupdate(self.conditions_tree, script.conditions_tree)
        
    def run():
        print "Droid running"
        
        for script in self._scripts: 
            pass            