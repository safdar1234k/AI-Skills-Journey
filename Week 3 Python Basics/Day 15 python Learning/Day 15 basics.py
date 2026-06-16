#Variables
name = "safdar"
age ="20"
city = "Lakki Marwat"
print(name)
print(age)
print(city)
print("My name is ",name,"and I am ",age,"years old. I live in",city)

#If and elif and else statements

score = int(input("Enter your score:"))
if score >= 80:
    print("A Grade")
elif score >= 70:
    print("B Grade")
elif score >= 60:
    print("C Grade")
elif score >= 40:
    print("D Grade")
else:
    print("Fail")

#Loops
project_list = ["Zapier", "make.com", "Lead collection", "Task reminder"]
for project in project_list:
    print(project)

#Functions
def greet(name):
    print("Hello ",name,"! Welcome to the world of Safdar King")
greet("Newton")

#