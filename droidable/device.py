class Property(object):
    def __init__(self, dictionary):
        if ('name'      in dictionary):   self.name = dictionary['name']
        if ('fields'    in dictionary): self.fields = dictionary['fields']

class Trigger(object):
    def __init__(self, dictionary):
        Property.__init__(self, dictionary);
        
class Action(object):
    def __init__(self, dictionary):
        Property.__init__(self, dictionary);
        

class Device(object):
    def __init__(self, ID, dictionary):
        self.ID = ID
        if (path is not None):
            self.device = self.name = dictionary;
            self.path = path
            
        if ('name'    in dictionary):     self.name = dictionary['name']
        if ('mac'     in dictionary):      self.mac = dictionary['mac']
        if ('type'    in dictionary):     self.type = dictionary['type']
        if ('triggers'in dictionary): self.triggers = Trigger(dictionary['triggers'])
        if ('actions' in dictionary):  self.actions = Action(dictionary['actions'])