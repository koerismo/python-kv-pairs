class Pair:
	def __init__(self,key,values):
		self.key=key
		if isinstance(values,list):self.values=values
		else:self.values=[values]
	def __getitem__(self,key):
		if isinstance(key,int):return self.values[key]
		if not isinstance(key,str):raise TypeError('__getitem__ in Pair: Key must be int or str!')
		return[x for x in self.values if x.key==key]
	def __delitem__(self,key):del self.values[key]
	def __repr__(self):
		if len(self.values)==0:return f"Pair(key={self.key})"
		if len(self.values)==1:return f"Pair(key={self.key},value={self.values[0]})"
		return f"Pair(key={self.key},values={self.values})"
