from connectable.device import Trigger
from connectable.device import Action


# [familydevice]
#     [device]
#         [trigger/action]
#             fieldsObj
# familydevice/device:value:fieldsHash


class Script:
    def __init__(self, ID, dictionary):
        # TODO accept also objects
        self.ID = ID
        self.triggers = dictionary['triggers']
        self.actions = dictionary['actions']
        self.generate_conditions()
    
    def generate_conditions (self):
        conditions_tree = {}
        for trigger_name, trigger in self.triggers.iteritems():
            
            if (trigger.device.kind not in conditions_tree):
                conditions_tree[trigger.device.kind] = {}
            if (trigger.device.ID not in conditions_tree[trigger.device.kind]):
                conditions_tree[trigger.device.kind][trigger.device.ID] = {}

            conditions_tree[trigger.device.kind][trigger.device.ID][trigger_name] = trigger.fields

        self.conditions_tree = conditions_tree