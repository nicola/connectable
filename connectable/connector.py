from connectable.hook import EventHook
from connectable.collection import Collection
from connectable.device import Device
from connectable.device import Trigger
from connectable.device import Action
from connectable.script import Script
from connectable.compiler import Compiler

class Connector:
    """A `connector` connects through `script`s `connectable`'s triggers and actions"""
        
    def __init__(self, name = ""):
        """Constructor"""
        self._compiler = Compiler(self)
        self._devices = {}
        self._scripts = {}
    
        # Grouped by kind
        self._triggers = {}
        self._actions = {}
        
    def add_device (self, device):
        """Adds a device"""
        if (device.kind not in self._devices):
            self._devices[device.kind] = {}

        self._devices[device.kind][device.ID] = device
        
    def device_with_ID(self, ID):
        """Check amongst all the device, one with ID=ID"""
        for (device_family_name, device_family) in self._devices.iteritems():
            if (ID in device_family):
                return device_family[ID]
            else:
                return False

    def add_script (self, script):
        """Adds a script"""

        self._compiler.link_connectables(script)
        self._scripts[script.ID] = script
        self.generate_conditions()
    
    # DEPRECATED
    def generate_conditions_by_family(self):
        
        conditions_tree = {}
        
        for (script_name, script) in self._scripts.iteritems():
            for trigger_name, trigger in script.triggers.iteritems():
                if (trigger.device.kind not in conditions_tree):
                    conditions_tree[trigger.device.kind] = {}
                if (trigger.device.ID not in conditions_tree[trigger.device.kind]):
                    conditions_tree[trigger.device.kind][trigger.device.ID] = {}
                if (trigger_name not in conditions_tree[trigger.device.kind][trigger.device.ID]):
                    conditions_tree[trigger.device.kind][trigger.device.ID][trigger_name] = {}
            
                conditions_tree[trigger.device.kind][trigger.device.ID][trigger_name][script_name] = trigger.fields
        self.conditions_tree = conditions_tree
        
    def generate_conditions(self):
        """Generates a tree with all the trigger conditions"""
        conditions_tree = {}
        
        for (script_name, script) in self._scripts.iteritems():
            conditions_tree[script_name] = script.conditions_tree

        self.conditions_tree = conditions_tree

        
    def run():
        print "Connector running"
        
        for script in self._scripts: 
            pass            