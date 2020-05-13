class TALab3v2:
	def __init__(self, mass):
		self.mass = mass
		self.chek = 0
		self.i = 0
		self.n = 0
		self.err = False

	def F1(self):
		return (self.i < len(self.mass))
	
	def F2(self):
		S = self.mass[self.i]
		return (S == "open1")
	
	def F3(self):
		S = self.mass[self.i]
		if (self.i == len(self.mass) - 1):
			return False
		else:
			S = self.mass[self.i + 1]
			if (not self.F6(self.i + 1) and not S == "close1"):
				return True
			
		
		return False
	
	def F4(self):
		S = self.mass[self.i]
		return (S == "close1")
	
	def F5(self):
		S = self.mass[self.i]
		if (self.n < 0):
			return False
		
		if (self.i == len(self.mass) - 1):
			return True
		else:
			S = self.mass[self.i + 1]
			if (S == "close1" or self.F6(self.i + 1)):
				return True		
		
		return False
	
	def F6(self, j):
		S = self.mass[j]
		fn = False
		if (S in ("plus","minus","mul", "div")):
			fn = True
		return fn
	
	def F7(self):
		S = self.mass[self.i]
		if (self.i == 0 or self.i == len(self.mass) - 1):
			return False
		else:
			S = self.mass[self.i + 1]
			if (not S == "close1"and not self.F6(self.i + 1)):
				return True
			
		
		return False
	
	def F8(self):
		S = self.mass[self.i]
		b1 = (S == "num" or "ID")
		b2 = True
		if (self.i < len(self.mass) - 1):
			S = self.mass[self.i + 1]
			b2 = False
			b2 = self.F6(self.i + 1) or S == "close1"
		
		return b1 and b2
	
	def F9(self, error):
		return error == True
	
	def S0(self):
		if (self.chek == 0):
			self.chek+= 1
			self.S1()
		
	
	def S1(self):
		self.i = 0
		self.err = True
		self.n = 0
		if (not self.F1()):
			self.S6()
		elif (self.F2()):
			self.S2()
		elif (self.F4()):
			self.S3()
		elif (not self.F6(self.i) and self.F8() or (self.F6(self.i) and self.F7())):
			self.S4()
		elif (not self.F6(self.i) and not self.F8() or self.F6(self.i) and not self.F7()):
			
			self.S5()
		return
	
	def S2(self):
		self.n+= 1
		if (self.F3()):
			self.S4()
		else:
			self.S5()
		
	
	def S3(self):
		self.n-= 1
		if (self.F5()):
			self.S4()
		else:
			self.S5()
		
	
	def S4(self):
		self.i+= 1
		if (not self.F1()):
			self.S6()
		elif (self.F2()):
			self.S2()
		elif (self.F4()):
			self.S3()
		elif (not self.F6(self.i) and self.F8() or self.F6(self.i) and self.F7()):
			self.S4()
		elif (not self.F6(self.i) and not self.F8() or self.F6(self.i) and not self.F7()):	
			self.S5()
	
	def S5(self):
		self.err = False
		self.S6()
	
	def S6(self):
		if (not self.n == 0):
			self.err = False 

		if (self.F9(self.err)):
			self.err == True
		else:
			self.err = False