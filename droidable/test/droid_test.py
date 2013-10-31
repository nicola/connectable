from droidable.device import Device
from droidable.device import DeviceCollection

import unittest

class InputCollectionTests(unittest.TestCase):
    def test_add(self):
        inputs = DeviceCollection()
        self.added = []
        def add(name): self.added.append(name)
        inputs.onAdded += add
        inputs.add('sensors/bluetooth', 'path1')
        input1 = inputs.get('sensors/bluetooth')
        self.assertEqual(input1.path, 'path1')
        self.assertEqual(self.added, ['sensors/bluetooth'])
        
        inputs.add(Device('sensors/wifi', 'path2'))
        input2 = inputs.get('sensors/wifi')
        self.assertEqual(input2.path, 'path2')
        self.assertEqual(self.added, ['sensors/bluetooth','sensors/wifi'])
        
    def test_remove(self):
        inputs = DeviceCollection()
        def remove(name): self.removed = name
        inputs.onRemoved += remove
        inputs.add('sensors/bluetooth', 'path')
        inputs.remove('sensors/bluetooth')
        self.assertFalse('sensor/rangefinder' in inputs.collection())

def main():
    unittest.main()

if __name__ == '__main__':
    main()
