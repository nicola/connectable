from droidable.device import Device
from droidable.collection import Collection

import unittest

class CollectionTests(unittest.TestCase):
    def test_add(self):
        collection = Collection()
        self.added = []
        def add(ID): self.added.append(ID)
        collection.onAdded += add
        collection.add({"ID": '1', "test": "su"})
        element1 = collection.get('1')
        self.assertEqual(element1['ID'], '1')
        self.assertEqual(self.added, ['1'])
        
        collection.add({"ID": '2'})
        element2 = collection.get('2')
        self.assertEqual(element2['ID'], '2')
        self.assertEqual(self.added, ['1','2'])
        
    def test_remove(self):
        collection = Collection()
        def remove(ID): self.removed = ID
        collection.onRemoved += remove
        collection.add({"ID": '1', "test": 2})
        collection.remove('1')
        self.assertFalse('1' in collection.collection())

def main():
    unittest.main()

if __name__ == '__main__':
    main()
