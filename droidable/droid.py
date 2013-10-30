from droidable.hook import EventHook
    
class Droid:
    """Creates a droid"""
    _inputs = {}
    _outputs = {}
    onInputAdded = EventHook()
    onInputRemoved = EventHook()
    onOutputAdded = EventHook()
    onOutputRemoved = EventHook()
    
    def __init__(self):
        print "hello\n"

    # Inputs
    def add_input(self, name, path):
        """Add input to the list"""
        self._inputs[name] = path;
        self.onInputAdded.fire(input=name)
    
    def remove_input(self, name):
        """Remove input from the list"""
        del self._inputs[name]
        self.onInputRemoved.fire(input=name)
        
    def inputs(self):
        """Return current inputs"""
        return self._inputs
        
    # Outputs
    def add_output(self, name, path):
        """Add output to the list"""
        self._output[name] = path;
        self.onOutputAdded.fire(input=name)

    def remove_output(self, name):
        """Remove output from the list"""
        del self._inputs[name]
        self.onOutputRemoved.fire(input=name)
    
    def outputs(self):
        """Return current outputs"""
        return self._outputs