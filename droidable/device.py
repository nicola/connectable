class Property(object):
    def __init__(self, device, dictionary):
        self.device = device
        if ('name'      in dictionary):   self.name = dictionary['name']
        if ('fields'    in dictionary): self.fields = dictionary['fields']

class Trigger(Property):
    def __init__(self, device, dictionary):
        super(Trigger, self).__init__(device, dictionary)
        
class Action(Property):
    def __init__(self, device, dictionary):
        super(Action, self).__init__(device, dictionary)
        

class Device(object):
    triggers = {}
    actions = {}
    def __init__(self, ID, dictionary = {}):
        self.ID = ID
        self.kind = dictionary['kind']
            
        if ('name'    in dictionary):     self.name = dictionary['name']
        if ('mac'     in dictionary):      self.mac = dictionary['mac']

        if ('triggers'in dictionary): self.triggers = map((lambda trigger: Trigger(self, trigger)), dictionary['triggers'])
        if ('actions' in dictionary):  self.actions = map((lambda action: Action(self, action)), dictionary['actions'])