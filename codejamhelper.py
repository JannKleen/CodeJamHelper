class CodeJamHelper():
	def __init__(self,inputList):
		self.inputList = inputList

	def getCaseCount(self):
		return int(self.inputList[0].strip())
		
	def getInputList(self):
		return self.inputList[1:]
		
	def getInputTuples(self,tupleDesc):
		inputTuples = []
		for listPos in xrange(1,len(self.inputList),len(tupleDesc)):
			tmp = []
			for tuplePos in xrange(0,len(tupleDesc)):
				tmp.append(tupleDesc[tuplePos](self.inputList[listPos+tuplePos]))
			inputTuples.append(tuple(tmp))
		return inputTuples
		
	def getOutputList(self,solutionList):
		for i in xrange(0,len(solutionList)):
			solutionList[i] = "Case #%d: %s"%(i+1,solutionList[i])
		return solutionList
			
