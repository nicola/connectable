class Property(object):
    def __init__(self, dictionary):
        if ('name'      in dictionary):   self.name = dictionary['name']
        if ('fields'    in dictionary): self.fields = dictionary['fields']

class Trigger(Property):
    def __init__(self, dictionary):
        super(Trigger, self).__init__(dictionary)
        
class Action(Property):
    def __init__(self, dictionary):
        super(Action, self).__init__(dictionary)
        

class Device(object):
    def __init__(self, ID, dictionary = {}):
        self.ID = ID
            
        if ('name'    in dictionary):     self.name = dictionary['name']
        if ('mac'     in dictionary):      self.mac = dictionary['mac']
        if ('type'    in dictionary):     self.type = dictionary['type']
        if ('triggers'in dictionary): self.triggers = map((lambda el: Trigger(el)), dictionary['triggers'])
        if ('actions' in dictionary):  self.actions = map((lambda trigger: Action(el)), dictionary['actions'])