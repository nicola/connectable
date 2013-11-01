from connectable.droid import Droid
from connectable.device import Device
from connectable.device import Trigger
from connectable.script import Script

import unittest

class DroidTests(unittest.TestCase):
    deviceA = Device("DeviceA", {
        'kind': "family/name",
        'triggers': {'trigger1'}
    })
    deviceB = Device("DeviceB", {
        'kind': "family/name",
        'triggers': {'trigger1'}
    })
    device_family_name2_A = Device("Device XYZ", {
        'kind': "family/name2",
        'triggers': {'trigger1'}
    })
    scriptA = Script("ScriptA", {
        'triggers': {
            'trigger1' : Trigger(deviceA, {
                'fields': {'field1': 1}     
            })
        },
        'actions': {}
    })
    scriptB = Script("ScriptB", {
        'triggers': {
            'trigger2' : Trigger(deviceA, {
                'fields': {'field2': 2}     
            })
        },
        'actions': {}
    })
    scriptC = Script("ScriptC", {
        'triggers': {
            'trigger2' : Trigger(deviceB, {
                'fields': {'field2': 2}     
            })
        },
        'actions': {}
    })
    scriptD = Script("ScriptC", {
        'triggers': {
            'trigger2' : Trigger(device_family_name2_A, {
                'fields': {'field2': 2}     
            })
        },
        'actions': {}
    })
    def test_init(self):
        droid = Droid()
    
    def test_add_device(self):
        droid = Droid()
        droid.add_device(self.deviceA)
        self.assertEqual(len(droid._devices), 1)

    def test_add_script_one(self):
        droid = Droid()
        droid.add_device(self.deviceA)
        droid.add_script(self.scriptA)
        print droid._scripts
        self.assertEqual(len(droid._scripts), 1)
        
        self.assertEqual(droid.conditions_hashes, {'family/name/DeviceA:trigger1&field1=1':{}})
        self.assertEqual(droid.conditions_tree, {'family/name': {'DeviceA': {'trigger1': {'field1': 1}}}})

    def test_add_script_multiple_same_device(self):
        droid = Droid()
        droid.add_device(self.deviceA)
        droid.add_script(self.scriptA)
        droid.add_script(self.scriptB)
        self.assertEqual(droid.conditions_hashes, {'family/name/DeviceA:trigger2&field2=2': {}, 'family/name/DeviceA:trigger1&field1=1': {}})
        self.assertEqual(droid.conditions_tree, {'family/name': {'DeviceA': {'trigger1': {'field1': 1}, 'trigger2': {'field2': 2}}}})

    def test_add_script_multiple_different_device_same_family(self):
        droid = Droid()
        droid.add_device(self.deviceA)
        droid.add_device(self.deviceB)
        droid.add_script(self.scriptA)
        droid.add_script(self.scriptB)
        droid.add_script(self.scriptC)
        self.assertEqual(droid.conditions_hashes, {'family/name/DeviceA:trigger2&field2=2': {}, 'family/name/DeviceA:trigger1&field1=1': {}, 'family/name/DeviceB:trigger2&field2=2': {}})
        print droid.conditions_tree
        self.assertEqual(droid.conditions_tree, {'family/name': {'DeviceA': {'trigger1': {'field1': 1}, 'trigger2': {'field2': 2}}, 'DeviceB': {'trigger2': {'field2': 2}}}})
        
    def test_add_script_multiple_different_device_different_family(self):
        droid = Droid()
        droid.add_device(self.deviceA)
        droid.add_device(self.deviceB)
        droid.add_device(self.device_family_name2_A)
        droid.add_script(self.scriptA)
        droid.add_script(self.scriptB)
        droid.add_script(self.scriptC)
        droid.add_script(self.scriptD)
        self.assertEqual(droid.conditions_hashes, {'family/name/DeviceA:trigger2&field2=2': {}, 'family/name2/Device XYZ:trigger2&field2=2': {}, 'family/name/DeviceA:trigger1&field1=1': {}})
        self.assertEqual(droid.conditions_tree, {'family/name2': {'Device XYZ': {'trigger2': {'field2': 2}}}, 'family/name': {'DeviceA': {'trigger1': {'field1': 1}, 'trigger2': {'field2': 2}}}})

def main():
    unittest.main()

if __name__ == '__main__':
    main()