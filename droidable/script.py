from droidable.device import Trigger
from droidable.device import Action


# [familydevice]
#     [device]
#         [trigger/action]
#             [fieldsHash]
# familydevice/device:value:fieldsHash


class Script:
    triggers = {}
    actions = {}
    conditions_hash = ""
    conditions_tree = {}
    def __init__(self, dictionary):
        # TODO accept also objects
        self.triggers = dictionary['triggers']
        self.actions = dictionary['actions']
        self.generate_conditions()
    
    def generate_conditions (self):
        conditions_hash = ""
        conditions_tree = {}
        for trigger_name, trigger in self.triggers.iteritems():
            conditions_hash = trigger.device.kind + "/" + trigger.device.ID + ":" + trigger_name
            conditions_tree[trigger.device.kind] = {}
            conditions_tree[trigger.device.kind][trigger.device.ID] = {}
            conditions_tree[trigger.device.kind][trigger.device.ID][trigger_name] = trigger.fields
            for (field_name, field) in trigger.fields.iteritems():
                conditions_hash = conditions_hash + "&" + field_name + "=" + str(field)
        
        self.conditions_hash = conditions_hash
        self.conditions_tree = conditions_tree