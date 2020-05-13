from Lab1_v2 import Lex
from MathLogic import MathLogic
from Lab2 import Syntax
from Lab3 import Semantic
from Lab4 import Lab4

import sys

from MathLogic import DoublInt

if __name__ == '__main__':	
	print(DoublInt("4.0"))
	lab_1 = Lex()
	lab_1.lexer()
	print ("Lab№1. Lexer")
	print (lab_1.outMas)

	print ("Lab№2. Parer")
	Sint_Log = Syntax(lab_1.outMas)
	Syntax_Tree = Sint_Log.Void_dec()
	print(Syntax_Tree)

	print ("Lab№3. Semantic")
	lab3 = Semantic()
	lab3.Run(Syntax_Tree)
	print(lab3.exprDict)

	print ("Lab№4. Generic")
	lab4 = Lab4()
	lab4.PrintProc(Syntax_Tree)
	print(lab4.OutString)