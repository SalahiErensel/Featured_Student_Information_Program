#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## import random

#Opening the Student class 
class Student:
    
    def __init__(self,firstname,lastname,birth_date,gender,major):
        self.student_number=random.randint(1,100000)
        self._firstname=firstname
        self._lastname=lastname
        self._birth_date=birth_date
        self._gender=gender
        self._major=major
        
    #Student Details
    def display_detail(self):
        print("Student Number : ",self.student_number)
        print("First name : " , self._firstname)
        print("Last name : " , self._lastname)
        print("Birth Date : " , self._birth_date)
        print("Gender : " , self._gender)
        print("Major : " , self._major)
    
    #getter method for firstname
    def get_firstname(self):
        return self._firstname

    #getter method for lastname
    def get_lastname(self):
        return self._lastname

    #getter method for birth_date
    def get_birth_date(self):
        return self._birth_date

    #getter method for gender 
    def get_gender(self):
        return self._gender
    
    #getter method for major
    def get_major(self):
        return self._major

    #setter method for firstname
    def set_firstname(self, firstname):
        self._firstname=firstname

    #setter method for lastname
    def set_lastname(self, lastname):
        self._lastname=lastname

    #setter method for birth_date
    def set_birth_date(self, birth_date):
        self._birth_date=birth_date
    
    #setter method for gender
    def set_gender(self, gender):
        self._gender=gender

    #setter method for major
    def set_major(self, major):
        self._major=major

    def __str__(self):
        return f"{firstname,lastname,birth_date,gender,major}"

#Creating array and displayin menu with choices
student=[]
while True:
    print("Choose any option 1-8 from the menu: ")
    print("\n1.Write the contents in student array to a file ")
    print("\n2.Read a student's data from a file and fill student array with this information")
    print("\n3.Add a new student")
    print("\n4.Show all students")
    print("\n5.Show all students who are 22 years old or more")
    print("\n6.Update a student with entering student number")
    print("\n7.Delete a student with entering student number")
    print("\n8.Quit from the program")

    choice=int(input())

    #writing the student information to a file
    if choice==1:
        with open("empty.txt","w") as f:
            for data in student:
                f.write("%s" %data)

    #reading student information from the file 
    elif choice==2:
        file=open("student.txt","r")
        for line in file:
            firstname,lastname,birth_date,gender,major=line.split(",")
            from_file=Student(firstname,lastname,birth_date,gender,major)
            student.append(from_file)
    
    #adding a new student to array
    elif choice==3:
        firstname,lastname,birth_date,gender,major=map(str,input("Please enter student details:Name,Last Name,Birthdate in Years,Gender,Major").split(","))
        from_file=Student(firstname,lastname,birth_date,gender,major)
        student.append(from_file)

    #showing all students
    elif choice==4:
        for from_file in student:
            from_file.display_detail()

    #showing students who are 22 years old or more
    elif choice==5:
        for from_file in student:
            if int(from_file.get_birth_date())<2000:
                from_file.display_detail()

    #updating a student record
    elif choice==6:
        std_number=int(input("Please enter the student number for update"))
        for from_file in student:
            if from_file.student_number==std_number:
                firstname,lastname,birth_date,gender,major=map(str,input("Please enter student information:").split(","))
                from_file.set_firstname(firstname)
                from_file.set_lastname(lastname)
                from_file.set_birth_date(birth_date)
                from_file.set_gender(gender)
                from_file.set_major(major)
    
    #deleting a student record
    elif choice==7:
        n=int(input("Please enter the student number for deleting:"))
        for from_file in student:
            if from_file.student_number==n:
                temp=from_file
        student.remove(temp)

    #Quit from the program
    elif choice==8:
        break
        
    else:
        break


# In[ ]:




