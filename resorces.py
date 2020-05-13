import re

File = "Text1.txt"

pattern = re.compile(r'\s+')
num = re.compile(r'[0-9]+(?!\.)')

#itDigitDouble = re().compile(r'^[0-9]+(\.)[0-9]+')

def itdigit_Int(string):
	db = float(string)
	integ = int(db)
	return db == integ

def itdigi_Castom(word):
	result = re.search(r"-?[0-9]+", word)
#	print (result.group(0), word, result.group(0) == word)
	return result.group(0) == word

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            db = float(string)
            return True
        except ValueError:
            return db == int(db)

class Lexem:
	def __init__(self, value, Type):
		self.Type = Type
		self.value = value
	def __repr__(self):
		return "('{value}'|'{Type}')".format(Type = self.Type, value = self.value)

class Node:
	def __init__(self, typeN, content = None, name = None):
		self.typeN = typeN
		self.content = content
		self.name = name
		self.indent = ''
	def __repr__(self):
		S = "({Type}'|'{name}')".format(Type = self.typeN, name = self.name)
		if (not self.content):
			return S
		else:
			for x in self.content:
				x.indent = '\t' + self.indent
				S += "\n"+ x.indent + x.__repr__()
		return S
		

"""	def __repr__(self):
		if not self.content:
			pass
		else:
			for x in content:
				print (x)
			return print(self.content)
"""