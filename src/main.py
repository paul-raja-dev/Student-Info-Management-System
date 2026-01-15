import students
import subjects
import marks

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
            print('-------------------')
            print('Delete student')
            print('-------------------')
            student_id=int(input('Enter the Student id to Update : '))
            students.delete_student(student_id)
            print('Student Enter Deleted Successfully........')
        else:
            print('Enter the correct chocie... ')
 

def subject():
        print(""" 
            1 -> Add Subject
            2 -> View the Available Subject
            3 -> Search Subject
            4 -> Update Subject
            5 -> Delete Subject
            """)
        choice=int(input('Enter your choice : '))
        if choice==1:
            course_code=input('Enter the Course Code : ')
            course_name=input('Enter the Course Name : ')
            credits=int(input('Enter the Credits : '))
            subjects.add_subject((course_code,course_name,credits))
            print('Course added successfully')
            
        elif choice==2:
            print('-----------------------------')
            print('View the Existing Subjects ')
            print('-----------------------------')
            data=subjects.view_subject()
            for line in data:
                print(line)
            print('\n End of the Table ')

        elif choice==3:
            print('-----------------------------')
            print('Search the Subject ')
            print('-----------------------------')
            sub_id=int(input('Enter the Subject ID : '))
            info=subjects.search_subject(sub_id)
            if info:
                print(f"""
                         Subject ID : {info[0]['subject_id']}
                         Subject Code : {info[0]['subject_code']}
                         Subject Name : {info[0]['subject_name']}
                         Subject Credits : {info[0]['credits']}
                       """)
            else:
                print('Subject Not Found')


        elif choice==4:
            print('-----------------------------')
            print('Update Subject ')
            print('-----------------------------')
            sub_id=int(input('Enter the subject ID : '))
            info=subjects.search_subject(sub_id)
            if info:
                 print('Subject Found And Current Details : ')
                 print(f"""
                         Subject ID : {info[0]['subject_id']}
                         Subject Code : {info[0]['subject_code']}
                         Subject Name : {info[0]['subject_name']}
                         Subject Credits : {info[0]['credits']}
                       """)
                 
                 print(""" 
                        1 -> Update Course_code
                        2 -> Update Course_name
                        3 -> update Credits
                        """)
                 choice=int(input('Entet Your Choice : '))
                 if choice==1:
                     updated_code=input('Enter the New Course Code : ')
                     subjects.update_subject('subject_code',(updated_code,sub_id))
                     print('Subject Updated Successfully')
                 elif choice==2:
                     updated_name=input('Enter the New Course Name : ')
                     subjects.update_subject('subject_name',(updated_name,sub_id))
                     print('Subject Updated Successfully')
                 elif choice==3:
                     updated_credits=input('Enter the New Credits : ')
                     subjects.update_subject('credits',(updated_credits,sub_id))
                     print('Subject Updated Successfully')

                 else:
                     print('Please Enter The Vaild Choice...')
            else:
                print('Course Not Found..')

        elif choice==5:
            print('-----------------------------')
            print('Delete Subject ')
            print('-----------------------------')
            sub_id=int(input('Enter the Subject ID to Delete : '))
            subjects.delete_subject(sub_id)
            print('Subject Deleted Success..')

        else:
            print('Please Enter the valid choice')


def mark():
        print(""" 
            1 -> Add Marks
            2 -> View the Available Marks
            3 -> View Marks By Student ID
            4 -> Update Marks 
            5 -> Delete Marks By Student ID 
            """)
        choice=int(input('Enter Your choice : '))
        if choice==1:
            student_id=int(input('Enter the student ID : '))
            subject_id=int(input('Enter the subject ID : '))
            sub_marks=int(input('Enter the marks scored : '))
            grade=input('Enter the Grade : ')
            marks.add_marks((student_id,subject_id,sub_marks,grade))
            print('Subject Added successfully')
        elif choice==2:
            print('-----------------------------')
            print('View the available marks..')
            print('-----------------------------')
            data=marks.view_marks()
            for line in data:
                print(line)
            print('\n End of the Table ')         
        elif choice==3:
            student_id=int(input('Enter the Student ID : '))
            info=marks.search_student_s_id(student_id)
            if info:
               print(info)
            else:
                print('Marks Not Found')        
        elif choice==4:
            mark_id=int(input('Enter the Subject ID : '))
            info=marks.search_student(mark_id)
            if info:
               print(f""" Exisiting DATA :
                         Marks ID : {info[0]['marks_id']}
                         Student ID : {info[0]['student_id']}
                         Subject ID : {info[0]['subject_id']}
                         Marks Scored : {info[0]['marks']}
                         Grade Obtained : {info[0]['grade']}
                       """)
               
            else:
                print('Marks Not Found')        

            
        elif choice==5:
            print('-----------------------------')
            print('Delete Student By Student ID ')
            print('-----------------------------')
            student_id=int(input('Enter the student ID : '))
            info=students.search_student(student_id)
            if info:
                marks.delete_student(student_id)
                print('Marks Entry Deleted Success..')
            else:
                print('Marks Entry Not Found...')
        else:
            print('Pleae enter the valid Choice..')

    

def main():
    while True:
        print("""\n  
                      STUDENT MANAGEMENT SOFTWARE 
                    -------------------------------
                 1 -> Students Table
                 2 -> Subject Table
                 3 -> marks Table
                 4 -> Exit Menu""")
        choice=int(input('Enter You Choice : '))
        if choice==1:
            student()
        elif choice==2:
            subject()
        elif choice==3:
            mark()
        elif choice==4:
            break
        else:
            print('Please enter the correct choice...')

main()