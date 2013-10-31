from droidable.hook import EventHook
from droidable.iocollection import InputCollection
from droidable.iocollection import OutputCollection

class Droid:
    """Creates a droid"""
    _inputs = InputCollection()
    _outputs = OutputCollection()

    def run(self):
        
    
    def __init__(self, name):
        self.name = name