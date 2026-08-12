#===================================
#Project Name : Student management system
# Devloped by : Shaik Fayaz Vali
# Verision :1.0
#=====================================
import json
import os
students = []
if os.path.exists("students.json"):
     file = open("students.json", "r")
     students = json.load(file)
     file.close()
 # Load Data code will go here


while True:
    print(" Student management system started successfully")
    print("==============================")
    print(" STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1.Add Student")
    print("2.View Student")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Save Data")
    print("7.Exit")
    
    choice = input("Enter your choice:")
    
    
    if choice =="1":
        print("=======ADD STUDENT======")
        Student_id = input("Enter Student ID:")
        Student_name = input("Enter Student Name:")
        Student_age = input("Enter Student Age:") 
        Student_branch = input("Enter Student Branch:")
        gender = input("Enter Student Gender:")
        mobile_number = input("Enter Mobile Number:")
        student_email = input("Enter Student Email:")
        student_address = input("Enter Student Address:")
        native_place = input("Enter Native Place:")
        college_name = input("Enter College Name:")
        college_address = input("Enter College Address:")
        
        student = {
            "Student ID":  Student_id,
            "Student Name": Student_name,
            "Student Age": Student_age,
            "Student Branch": Student_branch,
            "Gender": gender,
            "Mobile Number": mobile_number,
            "Student Email": student_email,
            "Student Address": student_address,
            "Native Place": native_place,
            "College Name": college_name,
            "College Address": college_address
             }
        students.append(student)
    elif choice == "2":
        print("======VIEW STUDENT======")
            
        for student in students:
            print("Student ID :",student["Student ID"])
            print("Student Name:",student["Student Name"])
            print( "Student Age:" , student[ "Student Age"])
            print( "Student Branch:",student[ "Student Branch"])
            print( "Gender:",student[ "Gender"])
            print( "Mobile Number:" ,student[ "Mobile Number" ])
            print( "Student Email:" ,student[ "Student Email" ])
            print( "Student Address:",student[ "Student Address"])
            print("Native Place:" ,student[   "Native Place" ])
            print("College Name:",student["College Name"])
            print(  "College Address:" ,student[  "College Address" ])
        
    elif choice == "3":
        print("======SEARCH STUDENT======")
        Search_id = input("Enter Student ID to search:")
        found = False
        for student in students:
             if student["Student ID"] == Search_id:
                 print("Student ID :",student["Student ID"])
                 print("Student Name:",student["Student Name"])
                 print( "Student Age:" , student[ "Student Age"])
                 print( "Student Branch:",student[ "Student Branch"])
                 print( "Gender:",student[ "Gender"])
                 print( "Mobile Number:" ,student[ "Mobile Number" ])
                 print( "Student Email:" ,student[ "Student Email" ])
                 print( "Student Address:",student[ "Student Address"])
                 print("Native Place:" ,student[   "Native Place" ])
                 print("College Name:",student["College Name"])
                 print(  "College Address:" ,student[  "College Address" ])
                 found = True
                 break
        if found == False:
            print("student not found")


    elif choice == "4":
        print("======UPDATE STUDENT======")
        Update_id = input("Enter Student ID to update:")#ask the user which student id to update
        found = False
        for student in students:
            if student["Student ID"] == Update_id:
                 student["Student Name"] = input("Enter New Student Name: ")
                 student["Student Age"] = input("Enter New Student Age: ")
                 student["Student Branch"] = input("Enter New Student Branch: ")
                 student["Gender"] = input("Enter New Gender: ")
                 student["Mobile Number"] = input("Enter New Mobile Number: ")
                 student["Student Email"] = input("Enter New Student Email: ")
                 student["Student Address"] = input("Enter New Student Address: ")
                 student["Native Place"] = input("Enter New Native Place: ")
                 student["College Name"] = input("Enter New College Name: ")
                 student["College Address"] = input("Enter New College Address: ")
                 print("Student Updated Successfully")
                 found = True
                 break
        if found == False:
            print("student not found")

    elif choice == "5":
        print("======DELETE STUDENT======")
        delete_id = input("Enter the Student ID to Delete:") #Ask the user which Student ID to delete.
        found = False  #found starts as False. It changes to True only if the student is found. Otherwise, it stays False. 
        for student in students: #Check every student one by one.
            if student["Student ID"] == delete_id:
                students.remove(student)
                print("student deleted successfully")
                found = True
                break
        if found == False:
            print("student not found")


    elif choice == "6":
        print("======SAVE DATA======")   
        file = open("students.json", "w")
        json.dump(students,file,indent=2)
        file.close()
        print("Data saved successfully")


    elif choice == "7":
        print("=======EXIT STUDENT=======")
        print("Thank you for using student management system")
        break

     
   