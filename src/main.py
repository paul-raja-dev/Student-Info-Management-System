import students
def student():
        print(""" 
            1 -> Add student
            2 -> View the Available Students
            3 -> Search student
            4 -> Update student
            5 -> Delete student
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
            print('-------------------')
            print('Search Student')
            print('-------------------')
            student_id=int(input('Enter the Student id to Search : '))
            info=students.search_student(student_id)
            if info:
                print('Student Found')
                print(f"Register No : {info[0]['register_number']}")
                print(f"Name : {info[0]['full_name']}")
                print(f"E-Mail : {info[0]['e_mail']}")
                print(f"Gender : {info[0]['gender']}")
                dob=info[0]['date_of_birth']
                print(f"Date Of Birth : {dob.strftime('%d-%m-%Y')}")

            else:
                print('Student Not Found')


        elif choice==4:
            print('-------------------')
            print('Update student')            
            print('-------------------')
            student_id=int(input('Enter the Student id to Update : '))
            info=students.search_student(student_id)
            if info:
                print('Student Found')
                print(f"Register No : {info[0]['register_number']}")
                print(f"Name : {info[0]['full_name']}")
                print(f"E-Mail : {info[0]['e_mail']}")
                print(f"Gender : {info[0]['gender']}")
                dob=info[0]['date_of_birth']
                print(f"Date Of Birth : {dob.strftime('%d-%m-%Y')}")
                print("""   1 -> Update Register No
                            2 -> Update Name
                            3 -> update E-mail
                            4 -> update Gender
                            5 -> Update Date of Birth """)
                choice=int(input('Enter Your choice : '))
                if choice==1:
                    updated_regno=input('Enter the new register number : ')
                    students.update_student('register_number',updated_regno,student_id)
                    print('Student register number updated success...')
                elif choice==2:
                    updated_name=input('Enter the new name : ')
                    students.update_student('full_name',updated_name,student_id)
                    print('Student register number updated success...')
                elif choice==3:
                    updated_email=input('Enter the new E-mail : ')
                    students.update_student('e_mail',updated_email,student_id)
                    print('Student register number updated success...')
                elif choice==4:
                    updated_gender=input('Enter the new Gender(M/F) : ')
                    students.update_student('gender',updated_gender,student_id)
                    print('Student register number updated success...')
                elif choice==5:
                    updated_dob=input('Enter the new DOB(YYYY-MM-DD) : ')
                    students.update_student('date_of_birth',updated_dob,student_id)
                    print('Student register number updated success...')
                else:
                    print('Enter the vaild choice....')
            else:
                print('Student Not Found')

        elif choice==5:
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