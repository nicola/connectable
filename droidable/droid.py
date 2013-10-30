from droidable.hook import EventHook
from droidable.iocollection import InputCollection
from droidable.iocollection import OutputCollection
    
class Droid:
    """Creates a droid"""
    _inputs = InputCollection()
    _outputs = OutputCollection()
    
    def inputs(self):
        return _inputs._collection;

    def outputs(self):
        return _inputs._collection;
    
    def __init__(self, name):
        self.name = name