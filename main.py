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

def search_student():
    print('-----------------Search Student----------------------')
    find_no=input('Enter the register number of the student to find : ')
    with open('data.txt','r') as f:
        data=f.readlines()
        for line in data:
            if line.startswith(find_no):
                roll_no,name,marks=line.split(',')
                print('Student Found : ')
                print(f'Register No : {roll_no}')
                print(f'Name of the student : {name}')
                print(f'Marks Scored : {marks}')
                break
        else:
            print('Student Record Not Found')
            
def update_student():
    print('-----------------Update Student----------------------')
    reg_no=input('Enter the register no of the student to update Details : ')
    with open('data.txt','r') as f:
        data=f.readlines()
        update_data=[]
        for line in data:
            if line.startswith(reg_no):
                roll_no,name,marks=line.split(',')
                print('Student Found and current details : ')
                print(f'\nName : {name}'
                      f'\nMarks : {marks}'
                      f'\n------------------------------------')
                print('TO UPDATE'
                      f'\n Name -> 1'
                      f'\n Marks -> 2')
                choice=int(input('Enter the field : '))
                if choice==1:
                    new_name=input('Enter the new name : ')
                    formatted_name=reg_no+','+new_name+','+marks+'\n'
                    update_data.append(formatted_name)
                    
                elif choice==2:
                    new_marks=input('Enter the new marks : ')
                    formatted_marks=reg_no+','+name+','+new_marks+'\n'
                    update_data.append(formatted_marks)
                else:
                    print('Please Enter the Vaild Choice')
                
            else:
                update_data.append(line)
    with open('data.txt','w') as f:
        f.writelines(update_data)

def delete_student():
    print('---------------------Deleting the Entitiy--------------------')
    reg_no=input('Enter the register number of the student to delete : ')
    with open('data.txt','r') as f:
        data=f.readlines()
        updated_data=[]
        for line in data:
            if line.startswith(reg_no):
                continue
            else:
                updated_data.append(line)
        with open('data.txt','w') as f:
            f.writelines(updated_data)

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