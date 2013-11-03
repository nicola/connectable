from connectable.hook import EventHook
from connectable.collection import Collection
from connectable.device import Device
from connectable.device import Trigger
from connectable.device import Action
from connectable.script import Script

class Connector:
    """A `connector` connects through `script`s `connectable`'s triggers and actions"""
        
    def __init__(self, name = ""):
        """Constructor"""
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

    def link_from_object(self, prop):
        """Linking function: From a device object return the one in _devices"""
        # TODO check if property exists
        if (prop.device.kind in self._devices and prop.device.ID in self._devices[prop.device.kind]):
            return self._devices[prop.device.kind][prop.device.ID]
        else:
            return False

    def link_from_string(self, prop_name, prop):
        """Linking function: From an id or kind return the closest corresponding one in _devices"""
        device = self.device_with_ID(prop.device)
        if (device):
            if (isinstance(prop, Trigger) and prop_name in device.triggers): return device
            if (isinstance(prop, Action) and prop_name in device.actions): return device
        
        if (prop.device in self._devices):
            # check in family
            for device in self._devices[prop.device]:
                if (isinstance(prop, Trigger) and prop_name in device.triggers): return device
                if (isinstance(prop, Action) and prop_name in device.actions): return device
                
        # TODO error raised to be improved
        raise

    def link_connectable(self, prop_name, prop):
        """Linking function: returns a device in _devices given the reference in a Script"""
        if (isinstance(prop.device, Device)):
            return self.link_from_object(prop)
            
        # TODO what about dictionaries?

        return self.link_from_string(prop_name, prop)
            
    def link_connectables(self, script):
        """Linking functions: connects connectable to the script"""
        for trigger_name, trigger in script.triggers.iteritems():
            trigger.device = self.link_connectable(trigger_name, trigger)
            
        for action_name, action in script.triggers.iteritems():
            action.device = self.link_connectable(action_name, action)
        

    def add_script (self, script):
        """Adds a script"""

        self.link_connectables(script)
        self._scripts[script.ID] = script
        self.generate_conditions()
        
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