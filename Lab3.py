from MathLogic import MathLogic

from resorces import itdigi_Castom, is_digit, itdigit_Int

import sys

class Semantic:
	def __init__(self):
		self.exprDict = {}
	def Run(self, Node):
		if (Node.typeN == "InitZ"):
			#Блок объявления переменной
			if (Node.content[0].typeN == "ID"):
				self.exprDict[Node.content[0].name] = None	#Занести переменную в словарь
				return
			elif (Node.content[0].typeN == "Add"):
				N = Node.content[0]	#занести переменную в словарь, если в объявлении идет присвоение. (Add.content = (Name, math))
				self.exprDict[N.content[0].name] = None
		elif (Node.typeN == "Add"):
			#Блок присвоение значения
			if (Node.content[0].name not in self.exprDict):
				self.ErrorMess("This expr is not define")
			expr = None
			math_L = Node.content[1]	
			n = len (math_L.content)
			count = []
			for i in range(n):
				if (math_L.content[i].typeN == "ID"):
					expr = math_L.content[i].name
					if (expr not in self.exprDict or self.exprDict[expr] == None):
						self.ErrorMess("Expr is nod define")
					count.append(self.exprDict[expr])
					continue
				count.append(math_L.content[i].name)
			try:
				ML = MathLogic(count)
				ML.S0()
			except:
				self.ErrorMess("Math.error. Wrong Type")
			if (ML.finRes == 'Error'):
				self.ErrorMess("Math.error. Zero error.")
			elif (not itdigit_Int(str(ML.finRes))):	#Переменная должна быть целым числом
				self.ErrorMess("Math.error. This is not Int.")
			else:
				self.exprDict[Node.content[0].name] = ML.finRes
			return
		if (not Node.content):	#Возврат, если у узла нет потомков
			return
		for nd in Node.content:
			self.Run(nd)
	def ErrorMess(self, mes):
		print ("Semantic Error:{mes}".format(mes = mes))
		sys.exit(1)