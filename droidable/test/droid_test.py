from droidable.droid import Droid
import unittest

class DroidTests(unittest.TestCase):

    def test_add_input(self):
            
        a = Droid()
        def onInputAdded (input): self.onInputAddedValue = input;
        a.onInputAdded += onInputAdded
        a.add_input("sensor/rangefinder", "rangefinder")
        inputs = a.inputs();

        self.assertEqual(inputs['sensor/rangefinder'], 'rangefinder')
        self.assertEqual(self.onInputAddedValue, 'sensor/rangefinder')

    def test_remove_input(self):
        a = Droid()
        def onInputRemoved (input): self.onInputRemovedValue = input;
        a.onInputRemoved += onInputRemoved
        a.remove_input("sensor/rangefinder")
        
        self.assertFalse('sensor/rangefinder' in a.inputs())
        self.assertEqual(self.onInputRemovedValue, 'sensor/rangefinder')

def main():
    unittest.main()

if __name__ == '__main__':
    main()
