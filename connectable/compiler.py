from connectable.device import Device
from connectable.device import Trigger
from connectable.device import Action

class Compiler:
    """Get a connector and links the device to the scripts"""
    def __init__(self, connector):
        self.connector = connector
        
    def link_from_object(self, prop):
        """Linking function: From a device object return the one in _devices"""
        # TODO check if property exists
        if (prop.device.kind in self.connector._devices and prop.device.ID in self.connector._devices[prop.device.kind]):
            return self.connector._devices[prop.device.kind][prop.device.ID]
        else:
            return False

    def link_from_string(self, prop_name, prop):
        """Linking function: From an id or kind return the closest corresponding one in _devices"""
        device = self.connector.device_with_ID(prop.device)
        if (device):
            if (isinstance(prop, Trigger) and prop_name in device.triggers): return device
            if (isinstance(prop, Action) and prop_name in device.actions): return device
        
        if (prop.device in self-connector._devices):
            # check in family
            for device in self.connector._devices[prop.device]:
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