from resorces import Node

from MathLogic import MathLogic
from AnaliticMath import TALab3v2

import sys

class Syntax:

	def __init__(self, lexer):
		self.lexer = lexer
		self.index = 0
		self.ecxDict = {}

	def Void_dec(self):
		"""Определение начала программы"""
		content = []
		content.append(self.nVoid())
		self.index += 1
		content.append(self.nName())
		self.index += 1
		content.append(self.nHead())
		content.append(self.nBody())
		n = Node("Prog", content = content)
		return n

	def nVoid(self):
		"""Объявление процедуры"""
		i = self.index
		if (self.lexer[i].Type == "void"):
			n = Node(typeN = "void", name = "void")
		else:
			self.ErrorMess("Void is wrong")

		return n

	def nName(self):
		"""Имя переменной или процедуры"""
		i = self.index
		if (self.lexer[i].Type == "ID"):
			n = Node("ID", name = self.lexer[i].value)
		return n

	def nHead(self):
		"""Голова процедуры"""
		content = []
		count_oc = 0
		if (self.lexer[self.index].Type != "open1"):
			self.ErrorMess("Head is wrong")
		while (self.HasNexLex() and self.lexer[self.index].Type != "open2"):
			lex = self.lexer[self.index].Type
			if (lex == "open1"):
				count_oc += 1
			#	content.append(Node("open1", name = "("))
			elif (lex == "close1"):
				count_oc -= 1
			#	content.append(Node("close1", name = ")"))
			elif (lex == "init"):
				content.append(self.nInitZ())
			if (count_oc < 0 or count_oc == 0 and self.lexer[self.index + 1].Type != "open2"):
				self.ErrorMess("Head is wrong: {head}".format(head = lex))
			self.index += 1
		self.index += 1
		n = Node("head", content = content)
		return n

	def nBody(self):
		"""Тело процедуры"""
		content = []
		while (self.HasNexLex() and self.lexer[self.index].Type != "close2"):
			content.append(self.nLine())
			self.index += 1
		n = Node("Body", content = content)
		return n

	def nInitZ(self):
		"""Объявление переменной"""
		content = []
		if (self.lexer[self.index].Type == "init"):
			if (self.HasNexLex() and self.lexer[self.index + 1].Type == "ID"):
				self.index += 1

				if (self.HasNexLex() and self.lexer[self.index + 1].Type == "add"):
					self.index += 1
					content.append(self.nAdd())
				elif (not self.HasNexLex() and not (self.lexer[self.index + 1].Type  == "endLine")):
					self.ErrorMess("Init expr")
				else:
					content.append(self.nName())
					if (self.lexer[self.index + 1].Type not in ["endLine", "close1"]):
						self.ErrorMess("Math. Eror")
			else:
				self.ErrorMess("Init is wrong: ")
		n = Node("InitZ", content = content)
		return n

	def nMath(self):
		"""Матю операции"""
		content = []
		count_oc = 0
		math_list = []
		while(self.HasNexLex and self.lexer[self.index].Type in ("num", "ID", "plus", "minus", "mul", "div", "open1", "close1")):
			if (self.lexer[self.index].Type == "close1" and self.lexer[self.index + 1].Type == "open2"):
				break
			math_list.append(Node (self.lexer[self.index].Type, name = self.lexer[self.index].value))
			self.index+=1
		test = TALab3v2([x.typeN for x in math_list])
		test.S0()
		if (test.err == False):
			self.ErrorMess("Math.Error")
		n = Node("Math", content = math_list)
		return n

	def nLine(self):
		"""Анализ строки"""
		content = []
		while (self.HasNexLex() and self.lexer[self.index].Type != "endLine"):
			if (self.lexer[self.index].Type == "init"):
				content.append(self.nInitZ())
			elif (self.lexer[self.index].Type == "ID" and self.lexer[self.index + 1].Type == "add"):
				self.index += 1
				content.append(self.nAdd())
			else:
				self.ErrorMess("wrong Line")
			self.index += 1
		n = Node ("Line", content = content)
		return n

	def nAdd(self):
		"""Присвоение переменной значения"""
		content = []
		if (self.lexer[self.index - 1].Type == "ID"):
			self.index -= 1
			content.append(self.nName())
			self.index += 2
		else:
			self.ErrorMess("Add expr")
		if (self.HasNexLex() and self.lexer[self.index].Type in ("num", "ID", "plus", "minus", "mul", "div", "open1", "close1")):
			content.append(self.nMath())
		else:
			self.ErrorMess("Add expr")
		if (self.lexer[self.index].Type not in ["endLine", "close1"]):
			self.ErrorMess("Math. Eror")		
		n = Node("Add", content = content)
		return n
		
	def ErrorMess(self, Mess):
		"""Вывод информации обошибке"""
		print(self.index)
		print ('Parser error:', Mess)
		sys.exit(1)

	def HasNexLex(self):
		"""Проверка на наличие следующего элемента"""
		return self.index < (len(self.lexer) - 1)
