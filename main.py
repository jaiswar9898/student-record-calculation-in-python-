
class Student():
      def __init__(self,name,roll,mark):
           self.roll = roll 
           self.name = name 
           self.mark = mark
      def inputscore(self):
          return self.mark

      def rollnum(self):
          return self.roll

      def __str__(self):
          return self.name + ' | ' + str(self.rollnum()) +' | '+ str(self.inputscore())

def Mark(rec, name, roll, mark):
    rec.append(Student(name,roll,mark))
    return rec 
RecData = []
x='y'
while x == 'y':
      rolln = input('roll number: ')
      name = input("name of student: ")
      roll = input("Marks:")
      RecData = Mark(RecData, name,roll,rolln)
      x = input("another student? y/n :")

n=1
for data in RecData:
    print(n,'.',data)
    n=n+1 
