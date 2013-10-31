from droidable.droid import Droid
from droidable.device import Device

import unittest

class DroidTests(unittest.TestCase):
    def test_init(self):
        droid = Droid()
        deviceA = Device("DeviceA", {
            'kind': "family/name",
            'triggers': {'trigger1'}
        })
        droid.add_device(deviceA)
        

def main():
    unittest.main()

if __name__ == '__main__':
    main()
