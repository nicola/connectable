

from connectable.connector import Connector
from connectable.device import Device
from connectable.device import Trigger
from connectable.script import Script

import unittest

class ConnectorTests(unittest.TestCase):
    deviceA = Device("DeviceA", {
        'kind': "familyA/name",
        'triggers': {'trigger1'}
    })
    deviceB = Device("DeviceB", {
        'kind': "familyB/name",
        'triggers': {'trigger1'}
    })

    script_one_trigger = Script("script_one_trigger", {
        'triggers': {
            'trigger1' : Trigger(deviceA, {
                'fields': {'field1': 1}     
            })
        },
        'actions': {}
    })
    script_two_trigger_same_device = Script("script_two_trigger_same_device", {
        'triggers': {
            'trigger1' : Trigger(deviceA, {
                'fields': {'field2': 2}     
            }),
            'trigger2' : Trigger(deviceA, {
                'fields': {'field2': 2}     
            })
        },
        'actions': {}
    })
    script_two_triggers_different_device = Script("ScriptC", {
        'triggers': {
            'trigger1' : Trigger(deviceA, {
                'fields': {'field2': 2}     
            }),
            'trigger2' : Trigger(deviceB, {
                'fields': {'field2': 2}     
            })
        },
        'actions': {}
    })
    
    scriptMultipleTriggers = Script("ScriptMultipleTrigger", {
        'triggers': {
            'first' : Trigger(deviceA, {
                'fields': { 'field1': 1, 'field2': 2}
            }),
            'second' : Trigger(deviceA, {
                'fields': { 'field3': 1, 'field4': 2}
            })
        },
        'actions': {
            
        }
    })
    
   
    # script
    #     .when("Device").has("event", "field1" == 3)
    #     .when("Device").has("event", "field1" == 3)
    #     .then()
    #     .select("Device").do("action", "parameter1", "parameter2")
    

    
    def test_init(self):
        droid = Connector()
    
    def test_add_device(self):
        droid = Connector()
        droid.add_device(self.deviceA)
        self.assertEqual(len(droid._devices), 1)

    def test_add_script_one_trigger(self):
        droid = Connector()
        droid.add_device(self.deviceA)
        droid.add_script(self.script_one_trigger)
        print droid._scripts
        self.assertEqual(len(droid._scripts), 1)
        print droid.conditions_tree
        self.assertEqual(droid.conditions_tree, {'script_one_trigger': {'familyA/name': {'DeviceA': {'trigger1': {'field1': 1}}}}})
        
    def test_add_script_two_trigger_same_device(self):
        droid = Connector()
        droid.add_device(self.deviceA)
        droid.add_script(self.script_two_trigger_same_device)
        print droid.conditions_tree
        self.assertEqual(droid.conditions_tree, {'script_two_trigger_same_device': {'familyA/name': {'DeviceA': {'trigger1': {'field2': 2}, 'trigger2': {'field2': 2}}}}})
        

    def test_add_script_two_triggers_different_device(self):
        droid = Connector()
        droid.add_device(self.deviceA)
        droid.add_device(self.deviceB)
        droid.add_script(self.script_two_triggers_different_device)
        print droid.conditions_tree
        self.assertEqual(droid.conditions_tree, {'ScriptC': {'familyA/name': {'DeviceA': {'trigger1': {'field2': 2}}}, 'familyB/name': {'DeviceB': {'trigger2': {'field2': 2}}}}})

  
def main():
    unittest.main()

if __name__ == '__main__':
    main()