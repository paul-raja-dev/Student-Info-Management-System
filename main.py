def add_student():
    print('--------------Addition of new student------------------')
    reg_no=input('Enter the register number of the new student : ')    
    name=input('Enter the name of the new student : ')
    marks=input('Enter the marks of the student : ')
    data=['\n',reg_no,',',name,',',marks]
    with open('data.txt','a') as f:
        f.writelines(data)


def view_student():
    print('---------------Viewing the database------------------')
    with open('data.txt','r') as f:
        data=f.read()
        print(data)


def main():
    while True:
        print('\n1. Add student' 
        '\n2. View students' 
        '\n3. Update student' 
        '\n4. Delete student' 
        '\n5. Search student' 
        '\n6. Exit')
        choice=int(input('Enter the choice : '))
        if choice==1:
            add_student()
        elif choice==2:
            view_student()
        elif choice==3:
            update_student()
        elif choice==4:
            delete_student()
        elif choice==5:
            search_student()
        elif choice==6:
            print('Exiting from the software ...')
            print('Exited successfully')
            break
        else:
            print('Please Enter from the choice')

main()