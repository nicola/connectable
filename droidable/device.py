class Device(object):
    def __init__(self, ID, dictionary):
        self.ID = ID
        if (path is not None):
            self.device = self.name = dictionary;
            self.path = path
            
        if ('name'    in dictionary):     self.name = dictionary['name']
        if ('mac'     in dictionary):      self.mac = dictionary['mac']
        if ('type'    in dictionary):     self.type = dictionary['type']
        if ('triggers'in dictionary): self.triggers = dictionary['triggers']
        if ('actions' in dictionary):  self.actions = dictionary['actions']