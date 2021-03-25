class Pair:
	def __init__(A,key,values):
		B=values;A.key=key
		if isinstance(B,list):A.values=B
		else:A.values=[B]
	def __getitem__(B,key):
		A=key
		if isinstance(A,int):return B.values[A]
		if not isinstance(A,str):raise TypeError('__getitem__ in Pair: Key must be int or str!')
		return[C for C in B.values if C.key==A]
	def __delitem__(A,key):del A.values[key]
	def __repr__(A):
		if len(A.values)==0:return f"Pair(key={A.key})"
		if len(A.values)==1:return f"Pair(key={A.key},value={A.values[0]})"
		return f"Pair(key={A.key},values={A.values})"
	@property
	def value(self):return self.values[0]
	@value.setter
	def value(self,value):self.values[0]=value
