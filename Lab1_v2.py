import re

from resorces import File, Lexem

class Lex():
	def __init__(self):
		self.f = open(File)
		self.inputStr = self.f.read()
		self.dictionary = {"int":"init", "void":"void", "+":"plus",
			"-":"minus", "*":"mul", "/":"div", "(":"open1", "{":"open2", ")": "close1",
			 "}":"close2", ";":"endLine", "==":"EQ", "!":"not", "<":"less", ">":"great",
			 "<=":"LE", ">=":"GE", "name":None, "=":"add", "!=":"NE", "num":"const"}
		self.outArr = self.inputStr.split('\n')
		self.outArr = [x for x in self.outArr if x]
		self.outMas = []

	def lexer(self):
		"""Лексический анализ"""
		for s in self.outArr:
		#	s = re.sub(pattern, '', s)
			keyWord = ''
			for i in range(len(s)):
				if (s[i] not in (" ", "\t")):
					keyWord += s[i]
				if (keyWord == ""):
					continue
				if (keyWord.isdigit()):
					if (i < len(s) - 1 and (s[i + 1]) not in (" ", "\t") and (s[i + 1]) not in self.dictionary):
						continue
					else:
						token=Lexem(keyWord,"num")
						self.outMas.append(token)
						keyWord = ''
						continue
				if keyWord in self.dictionary:
					if (i < len(s) - 1):
						if (s[i] == s[i+1] == "/"):
							break
						elif (s[i] in [">", "<", "=", "!"] and s[i + 1] == "="):
							continue
					token=Lexem(keyWord,self.dictionary[keyWord])
					self.outMas.append(token)
					keyWord = ''
				elif (i < len(s) - 1 and s[i + 1] in self.dictionary or i >= len(s) - 1 or s[i] in (" ", "\t")):
				#	dictionary["name"].value = keyWord
					token = Lexem(keyWord, "ID")
					self.outMas.append(token)#Добавление имеи переменной
					keyWord = ''#косяк с присвоением + not equals