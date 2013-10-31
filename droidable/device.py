class Device(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path

class InputDevice(Device):
    def __init__(self, name, path):
        super(InputDevice, self).__init__(name, path);
        
class OutputDevice(Device):
    def __init__(self, name, path):
        super(InputDevice, self).__init__(name, path);