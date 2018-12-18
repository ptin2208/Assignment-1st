from StudentCard import StudentCard

class MainShopCharger:
 __insertedStudentCard = None

 @staticmethod
 #get inserted card
 def insertStudentCard(studentID):
  MainShopCharger.__insertedStudentCard = StudentCard.getStudentCard(studentID)
  
 @staticmethod
 def chargeMoney(money):
  #card is inserted
  if not MainShopCharger.__insertedStudentCard is None:
   temp = MainShopCharger.__insertedStudentCard.getBalance() + money
   #balance is enough
   if temp > 0:
    MainShopCharger.__insertedStudentCard.setBalance(MainShopCharger.__insertedStudentCard.getBalance() + money)
    MainShopCharger.printBalance()
    return
   #balance is not enough
   else:
    print('残高は足りません')
    print(str(-temp) + 'が不足である')
    return
  #card is not inserted
  else: 
   print('学生証が挿入されていません')
   return

 @staticmethod			
 def printBalance():
  print("残高を表示します");
  print("学生名:" + MainShopCharger.__insertedStudentCard.getStudentName());
  print("残高:" + str(MainShopCharger.__insertedStudentCard.getBalance()));
  return

 def main():
  studentCard1 = StudentCard(0, 'tut')  #add card 1 to list
  studentCard2 = StudentCard(1, 'tenpaku')  #add card 2 to list
  studentCard1.setBalance(1000) #set card 1 balance to 1000

  from MainShopCharger import MainShopCharger as a
 
  a.chargeMoney(200)    #error card is not inserted
    
  a.insertStudentCard(0)    #StudentID = 0 card is inserted
		
  a.chargeMoney(1000)   #balance = 2000
		
  a.chargeMoney(-300)   #balance = 1700
		
  a.insertStudentCard(1)    #StudentID = 1 card is inserted
		
  a.chargeMoney(500)    #balance = 500
		
  a.chargeMoney(-1000)  #error account balance is not enough
	
 if __name__ == '__main__' :
  import sys
  main()

