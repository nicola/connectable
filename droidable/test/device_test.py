from droidable.device import Device
import unittest

class DeviceTests(unittest.TestCase):
    def test_init(self):
        device = Device('1', {'kind': 'family/child'})
        self.assertEqual(device.ID, '1')
        self.assertEqual(len(device.triggers), 0)
        
        device = Device('1', {'kind': 'family/child', 'name': "Device name",'triggers':[{'name':'trigger1', 'fields':[]}, {'name':'trigger2', 'fields':[]}]})
        self.assertEqual(device.name, "Device name")
        self.assertEqual(len(device.triggers), 2)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
