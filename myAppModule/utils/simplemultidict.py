class SimpleMultiDict(dict):
    def getlist(self, key):
        if not isinstance(self[key], list):
            return [self[key]]
        else:
            return self[key]
