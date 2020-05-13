class Lab4:
	def __init__(self):
		self.OutString = ""

	def Run(self, syntaxTree):
		for Node in syntaxTree.content:
			if (Node.typeN == "init"):
				if (Node.content[0].typeN == "ID"):
					self.OutString += "%{name}%\n".format(name = Node.content[0].name)
				elif (Node.content[0].typeN == "Add"):
					self.Run(Node)
					return
			elif (Node.typeN == "Add"):
				self.OutString += "%{name}% := {content}\n".format(name = Node.content[0].name,
						content = mathRun(Node.content[1]))
			if (Node.content):
				self.Run(Node)

	def PrintProc(self, syntaxTree):
		self.OutString = "PROCEDURE %{name}%\n".format(name = syntaxTree.content[1].name)
		self.Run(syntaxTree)
		self.OutString += "ENDPROC %{name}%".format(name = syntaxTree.content[1].name)


def mathRun(math):
	retStr = ""
	for m in math.content:
		if (m.typeN == "ID"):
			retStr += "%{name}% ".format(name = m.name)
		else:
			retStr += m.name + " "
	return retStr