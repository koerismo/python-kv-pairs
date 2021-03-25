# Pairs class v2

class Pair:
    ''' A class to handle key/value pairs. '''
    def __init__(self, key, values):
        self.key = key
        if isinstance(values, list):
            self.values = values
        else:
            self.values = [values]

    # Retrieve property from Pair

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.values[key]
        if not isinstance(key, str):
            raise TypeError('__getitem__ in Pair: Key must be int or str!')
        
        return [x for x in self.values if x.key == key]
    
    # Delete items from the Pair

    def __delitem__(self,key):
        del self.values[key]

    # Represent Pair in string form
    
    def __repr__(self):
        if len(self.values) == 0:
            return f'Pair(key={self.key})'
        if len(self.values) == 1:
            return f'Pair(key={self.key},value={self.values[0]})'
        return f'Pair(key={self.key},values={self.values})'
