from droidable.iocollection import IOCollection
import unittest

class IOCollectionTests(unittest.TestCase):
    def test_add(self):
        inputs = IOCollection()
        def add(name): self.added = name
        inputs.onAdded += add
        inputs.add('sensors/bluetooth', 'path')
        
        self.assertEqual(inputs.get('sensors/bluetooth'), 'path')
        self.assertEqual(self.added, 'sensors/bluetooth')
        
    def test_remove(self):
        inputs = IOCollection()
        def remove(name): self.removed = name
        inputs.onRemoved += remove
        inputs.add('sensors/bluetooth', 'path')
        inputs.remove('sensors/bluetooth')
        self.assertFalse('sensor/rangefinder' in inputs.collection())

def main():
    unittest.main()

if __name__ == '__main__':
    main()
