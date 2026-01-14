import students
def student():
        print(""" 
            1 -> Add student
            2 -> View the Available Students
            3 -> Update the Existing Date
            """)
        
        choice=int(input('Enter your choice : '))

        if choice==1:
            reg_no=input('Enter the register no : ')
            name=input('Enter the Full Name of the student : ')
            e_mail=input('Enter the E-mail of the student : ')
            dob=input('Enter the DOB in the format YYYY-MM-DD : ')
            gender=input('Enter the Gender of the student(M/F) : ')
            values=(reg_no,name,e_mail,dob,gender)
            students.add_student(values)
            print('Student Entry Successfull.....')

        elif choice==2:
            print('\nViewing the Database......\n')
            data=students.view_student()
            for value in data:
                print(value)
            print('\nxxxx----End of the Table----xxxx\n')
            print('\nData has Been fetched......\n')
         
        elif choice==3:
            pass
        else:
            print('Enter the correct chocie... ')
 




def main():
    while True:
        print("""\n            STUDENT MANAGEMENT SOFTWARE 
                 1 -> Students Table
                 2 -> Subject Table
                 3 -> marks Table
                 4 -> Exit Menu""")
        choice=int(input('Enter You Choice : '))
        if choice==1:
            student()
        elif choice==2:
            subjects()
        elif choice==3:
            marks()
        elif choice==4:
            break
        else:
            print('Please enter the correct choice...')

main()