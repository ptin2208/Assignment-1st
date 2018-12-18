class StudentCard:
 __studentCardList = []
 def __init__(self, studentID, studentName):
  self.__studentID = studentID
  self.__studentName = studentName
  self.__balance = 0
  StudentCard.__studentCardList.append(self)

 def getStudentName(self):
  return self.__studentName
	
 def getBalance(self):
  return (self.__balance)

 def getStudentID(self):
  return self.__studentID
    
 def setBalance(self, newBalance):
  self.__balance = newBalance
	
 @staticmethod
 def getStudentCard(studentID):
  for ind in StudentCard.__studentCardList:
   if ind.getStudentID() == studentID:
    return ind
