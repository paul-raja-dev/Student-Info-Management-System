def main():
    while True:
        print('\n1. Add student' 
        '\n2. View students' 
        '\n3. Update student' 
        '\n4. Delete student' 
        '\n5. Search student' 
        '\n6. Exit')
        choice=int(input('Enter the choice'))
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
            break
        else:
            print('Please Enter from the choice')

main()