from connectable.hook import EventHook

class Collection(object):

    def __init__(self, collection = {}):
        self.onAdded = EventHook()
        self.onRemoved = EventHook()
        self._collection = collection

    def get(self, ID):
        return self._collection[ID];

    def add(self, obj):
        self._collection[obj['ID']] = obj
        self.onAdded.fire(ID=obj['ID'])

    def remove(self, ID):
        del self._collection[ID]
        self.onRemoved.fire(ID=ID)

    def collection(self):
        return self._collection