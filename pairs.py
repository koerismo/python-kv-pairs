class Pair:
    ''' Pair( key, value(s) ) :  A class that handles key/value pairs nicely. '''
    def __init__(self,key:str,values):
        self.key = key
        if not isinstance(values, list):
            self.__values = [values]
        else:
            self.__values = values

    def __getitem__(self,key):
        ''' Pair()( key:int/str ) :  Retrieve a KeyList of Pairs with matching keys. '''
        # If int, use directly
        if isinstance(key,int):
            return self.__values[key]
        # If string, filter
        keyfilter = lambda x:x.key == key
        return KeyList(filter(keyfilter,self.__values),self)

    def __repr__(self):
        if len(self.__values) == 1:
            return f'Pair(key={self.key},value={self.__values[0]})'
        return f'Pair(key={self.key},values={self.__values})'

    @property
    def value(self):
        ''' Pair().value :  Retrieve the pair\'s value. Shortcut for Pair().values[0] '''
        return self.__values[0]

    @value.setter
    def value(self,val):
        ''' Pair().value = ... :  Set the pair\'s value. Shortcut for Pair().values[0] = ...'''
        self.__values[0] = val

    @property
    def values(self):
        return self.__values




class KeyList:
    ''' KeyList( items, parent) :  An internal class that handles key/value pair lists within key/value pairs. '''
    def __init__(self, items:list, parent:Pair):
        self.__items = list(items)
        self.__parent = parent
    
    def __getitem__(self, itm):
        return self.__items[itm]

    def __setitem__(self, itm, val):
        self.__items[itm] = val
        self.__parent.__values[itm] = val
        
    def __delitem__(self, itm):
        del(self.__items[itm])
        del(self.__parent.__values[itm])

    def __repr__(self):
        return str(self.__items)
