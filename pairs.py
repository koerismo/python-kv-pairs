# Pairs class v2

from typing import Generic, List, TypeVar, Union

V = TypeVar('V')

class Pair(Generic[V]):
    ''' A class to handle key/value pairs. '''
    def __init__(self, key: str, values: Union[V, List[V]]) -> None:
        self.key = key
        if isinstance(values, list):
            self.values = values
        else:
            self.values = [values]

    # Retrieve property from Pair

    def __getitem__(self, key: Union[str, int]):
        if isinstance(key, int):
            return self.values[key]
        if not isinstance(key, str):
            raise TypeError('__getitem__ in Pair: Key must be int or str!')
        
        return [x for x in self.values if isinstance(x, Pair) and x.key == key]
    
    # Delete items from the Pair

    def __delitem__(self, key: Union[str, int]) -> None:
        if isinstance(key, int):
            del self.values[key]
        if not isinstance(key, str):
            raise TypeError('__getitem__ in Pair: Key must be int or str!')

        for idx, x in enumerate(self.values):
            if isinstance(x, Pair) and x.key == key:
                del self.values[idx]

    # Represent Pair in string form
    
    def __repr__(self) -> str:
        if len(self.values) == 0:
            return f'Pair(key={self.key})'
        if len(self.values) == 1:
            return f'Pair(key={self.key},value={self.values[0]})'
        return f'Pair(key={self.key},values={self.values})'

    key: str
    values: List[V]
