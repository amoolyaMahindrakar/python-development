class Stuinfo:
    def __init__(self,name,rollnumber,math,phy,chem)  :
        self.name=name
        self.rollnumber=rollnumber   
        self.math=math
        self.phy=phy
        self.chem=chem
#method to find average
    def avg(self)   :
        return((self.math+self.phy+self.chem)/3)
        
#method to find grades
    def grade(self):
        avg=self.avg()
        if(avg>=90):
            return("Grade A")
        if(avg>=80):
            return("Grade B")
        if(avg>=70):
            return("Grade C")
        if(avg>=60):
            return("Grade D")
        else:
            return("Fail")
#method to display student's performance
    def display(self):
        print("Name:",self.name)
        print("Roll number:",self.rollnumber)
        print("Maths:",self.math)
        print("Physics:",self.phy)
        print("Chemistry:",self.chem)
        print("Average:",self.avg())
        print("Grade:",self.grade())
#a list to store object attributes of students
students=[]

n=int(input("Enter number of students in class:"))

for i in range(n):
    print("\nEnter details of Student",i+1)

    name=input("Enter name:")
    rollnumber=int(input("Enter rollnumber:"))
    math=int(input("Enter math marks:"))
    phy=int(input("Enter phy marks:"))
    chem=int(input("Enter chem marks:"))

    student=Stuinfo(name,rollnumber,math,phy,chem)
    students.append(student)
#to find topper from the students
topper=students[0]
for student in students:
    if(student.avg()>topper.avg()):
        topper=student

print("/n----TOPPER---")
topper.display()

#to find class average
total=0
for student in students:
    total=total+student.avg()
class_avg=total/len(students)

print("/nClass average:",class_avg)

#to find students above class average
print("/n---Students above class average---")

for student in students:
    if student.avg()>class_avg:
        print(student.name)





