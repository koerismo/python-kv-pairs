# python-kv-pairs
Two tiny classes that allow key/value structures to be formed, accessed, and modified easily.

![An image showing example usage](https://media.discordapp.net/attachments/307998594777219073/824446042736427019/unknown.png)

# Mini-docs
### `Pair`
*A class that holds a key and a value.*
#### Usage:
```py
>>> myVar = Pair('Key','Value')
>>> mySecondVar = Pair('Key', [ Pair('SubKey','Value1'), Pair('SubKey','Value2'), Pair('SpecialSubKey','Value3') ]) 
>>> myVar.key #Returns str
Key
>>> myVar.value #Returns any
Value
>>> mySecondVar.values #Returns list
[Pair(key=SubKey,value=Value1),Pair(key=SubKey,value=Value2),Pair(key=SpecialSubKey,value=Value3)]
>>> mySecondVar[0] #Returns Pair
Pair(key=SubKey,value=Value1)
>>> mySecondVar['SubKey'] #Returns KeyList
[Pair(key=SubKey,value=Value1),Pair(key=SubKey,value=Value2)]
>>> mySecondVar['SpecialSubKey'] #Returns KeyList
[Pair(key=SpecialSubKey,value=Value3)]
```
