from connectable.droid import Droid
from connectable.device import Device
from connectable.device import Trigger
from connectable.script import Script

import unittest

class DroidTests(unittest.TestCase):
    def test_init(self):
        droid = Droid()
        deviceA = Device("DeviceA", {
            'kind': "family/name",
            'triggers': {'trigger1'}
        })
        scriptA = Script("ScriptA", {
            'triggers': {
                'trigger1' : Trigger(deviceA, {
                    'fields': {'field1': {"val": 2}}     
                })
            },
            'actions': {}
        })
        droid.add_device(deviceA)
        droid.add_script(scriptA)
        

def main():
    unittest.main()

if __name__ == '__main__':
    main()