from resorces import itdigi_Castom, is_digit, itdigit_Int

class MathLogic:
	def __init__(self, Mass):
		self.mass = Mass
		self.chek = 0
		self.i = 0
		self.list = []
		self.stk = []
		self.finRes = ""

	def F1(self, ms):#???
		"""Длинна массива равна нулю"""
		return len(ms) == 0
	
	def F2(self, ms):
		"""Текущая стока принадлежит ко множеству ("+", "-", "*", "/", "(", ")")"""
		S = ms[self.i] #????
		if (S in ("+", "-", "*", "/", "(", ")")):
			return True
		else:
			return False
		
	def F3(self, S):
		"""Текущая строка - это )"""
		return S ==")"
	
	def sch(self, S):
		"""Подсчет приоритетов мат операторов
		Если оператор -- * или / => 2
		Иначе => 1"""
		if (S in ("*", "/")):
			return 2
		else:
			return 1
		
	def F4(self):
		"""Сравнение приоритет текущей операции с приоритетом операции верхнего элемента стека"""
		S1 = self.mass[self.i]
		if (len(self.stk) == 0):
			return False
		S2 = self.stk[len(self.stk) - 1]
		a1 = self.sch(S1)
		a2 = self.sch(S2)
		if (S2 in ("(", ")") or S1 in ("(", ")")):
			return False
		if (a2 >= a1):
			return True
		else:
			return False
	
	def F5(self):
		"""Проверка при делении на ноль"""
		sd = self.list[self.i]
		S = self.stk[len(self.stk) - 1]
		if (S == "0" and sd == "/"):
			return True
		return False
	
	def S0(self):
		"""Запуск автомата"""
		if (self.chek == 0):
			self.chek += 1
			self.S1()
		
	def S1(self):
		"""Начало вычислений"""
		self.i = 0

		if (self.F1(self.mass)):
			self.S5()
		elif (not self.F2(self.mass)):
			self.S2()
		elif (self.F4()):
			self.S4()
		else:
			self.S3()
		
	def S2(self):
		"""Поместить строку в выходной список"""
		S = self.mass[self.i]
		self.list.append(S)
		del self.mass[self.i]

		if (self.F1(self.mass)):
			self.S5()
			return
		S = self.mass[self.i]
		if (not self.F2(self.mass) and not self.F1(self.mass)):
			self.S2()
		elif (self.F2(self.mass) and not self.F1(self.mass) and not self.F4()):
			self.S3()
		else:
			self.S4()
		
	def S3(self):
		"""Поместить строку в стек"""
		S = self.mass[self.i]
		self.stk.append(S)
		del self.mass[self.i]
		S = self.stk[len(self.stk) - 1]

		if (self.F3(S)):
			self.S6()
		elif (self.F1(self.mass)):
			self.S5()
		elif (not self.F2(self.mass)):
			self.S2()
		elif (self.F4()):
			self.S4()
		else:
			self.S3()
		
	def S4(self):
		"""Поместить строку в стек с выталкиванием"""
		S = self.stk.pop()
		self.list.append(S)
		S = self.mass[self.i]
		del self.mass[self.i]
		self.stk.append(S)

		S = self.stk[len(self.stk) - 1]
		if (self.F3(S)):
			self.S6()
		elif (self.F1(self.mass)):
			self.S5()
		elif (not self.F2(self.mass)):
			self.S2()
		elif (self.F4()):
			self.S4()
		else:
			self.S3()
		
	def S5(self):
		"""Создать новый стек"""
		n = len(self.stk)
		while (n > 0):
			S = self.stk.pop()
			self.list.append(S)
			n-=1

		if (self.F1(self.list)):
			self.S10()
		elif (not self.F2(self.list)):
			self.S7()
		elif (self.F5()):
			self.S8()
		else:
			self.S9()
		
	def S6(self):
		"""Перенести из стека все строки До ("""
		S = ''
		while (True):
			S = self.stk.pop()
			if (S not in ("(", ")")):
				self.list.append(S) 
			if (S == "("):
				break

		if (self.F1(self.mass)):
			self.S5()
		elif (self.F2(self.mass)):
			if (self.F4()):
				self.S4()
			else:
				self.S3()
		elif (not self.F2(self.mass)):
			self.S2()
	
	def S7(self):
		"""Поместить строку в стек"""
		S = self.list[self.i]
		del self.list[self.i]
		self.stk.append(S)

		if (self.F1(self.list)):
			self.S10()
		elif (not self.F2(self.list)):
			self.S7()
		elif (self.F5()):
			self.S8()
		else:
			self.S9()
		
	def S8(self):
		"""Ошибка при делении на ноль"""
		self.finRes = "Error"
		self.S0()
	
	def S9(self):
		"""Промежуточное вычисление"""
		sd = self.list[self.i]
		del self.list[self.i]
		a1 = float(self.stk.pop())
		a2 = float(self.stk.pop())
		fin = ""
		if (sd == "*"):
			a1 = a1 * a2
		elif (sd == "/"):
			a1 = float(a2 / a1)
		elif (sd == "+"):
			a1 = a2 + a1
		elif (sd == "-"):
			a1 = a2 - a1
		fin = str(a1)
		
		self.stk.append(fin)

		if (self.F1(self.list)):
			self.S10()
		elif (not self.F2(self.list)):
			self.S7()
		elif (self.F5()):
			self.S8()
		else:
			self.S9()
		
	def S10(self):
		"""Результат вычисления"""
		self.finRes = self.stk[0]
		if (DoublInt(self.finRes)):
			self.finRes = int(float(self.finRes))
			self.finRes = str(self.finRes)
	#	print (DoublInt(self.finRes))
		self.S0()

def DoublInt(dbInt):
	try:
		db = float(dbInt)
		intr = int(db)
		return (db == intr)
	except:
		return False