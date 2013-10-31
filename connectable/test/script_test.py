from connectable.script import Script
from connectable.device import Device
from connectable.device import Trigger
import unittest

class ScriptTests(unittest.TestCase):
    def test_init(self):
        
        deviceA = Device("DeviceA", {
            'kind': "race/family",
        })
        
        dictionary = {}
        dictionary['triggers'] = {
            'trigger1': Trigger(deviceA,{
                'name': "The trigger 1",
                'fields': {
                    "this-is-a-field": 10
                }    
            })
        }
        dictionary['actions'] = {}
        script = Script("script1", dictionary)
        
        self.assertEqual(script.conditions_hash, "race/family/DeviceA:trigger1&this-is-a-field=10")
        self.assertEqual(script.conditions_tree, {'race/family': {'DeviceA': {'trigger1': {'this-is-a-field': 10}}}})

    def main():
        unittest.main()

        if __name__ == '__main__':
            main()
