import ast

f1 = open('C:/Python/student_mgnt_system/student_records.txt','a+')

f1.seek(0)

# accessing the file in read mode

all_data = []

for i in f1:

    i = i.rstrip('\n\n')

    if i != '':

        i = ast.literal_eval(i)

        all_data.append(i)

print('Student Management System')

# Function to add a new record

def search_record(reg_no):

    isfound = False

    for i in range(len(all_data)):

        if all_data[i][0] == reg_no:

            isfound =  True

            return all_data.index(all_data[i])
        
    if not isfound:

        print('\nRecord not found\n')

        return -1

def add_record():

    # Register number - following the last register number
    
    if len(all_data) == 0:

        register_no = 1

    else:

        register_no = len(all_data) + 1

    print(f'Register No: {register_no}')

    name = input('Enter the name: ')

    age = input('Enter the age: ')

    student_class = input('Enter the class: ')

    native = input('Enter the native: ')

    new_records = [register_no,name,age,student_class,native]

    all_data.append(new_records)

def edit_record():
    
    reg_no = int(input('Enter the register number to edit: '))

    index = search_record(reg_no)

    if index != -1:

        view_record(reg_no)

        print('Enter the data to edit (leave as bank to keep unchanged):')

        print(f'Register No: {reg_no}')

        name_e = input('Enter the name: ')

        age_e = input('Enter the age: ')

        student_class_e = input('Enter the class: ')

        native_e = input('Enter the native: ')

        print()

        if name_e == '':

            name_e = all_data[index][1]

        if age_e == '':

            age_e = all_data[index][2]

        if student_class_e == '':

            student_class_e = all_data[index][3]

        if native_e == '':

            native_e = all_data[index][4]

        edited_records = [reg_no, name_e, age_e, student_class_e, native_e]

        all_data[index] = edited_records

def display_all_records():
    
    print('\nAll Student Records:')

    for i in all_data:

        print(i)

    print(f'Total Records: {len(all_data)}')
    print()

def view_record(reg_no=None):
        
    if reg_no == None:
    
        reg_no = int(input('Enter the register number to view: '))

    index = search_record(reg_no)

    if index != -1:

        record = all_data[index]

        print(f'\nRegister Number: {record[0]}')
        print(f'Name: {record[1]}')
        print(f'Age: {record[2]}')
        print(f'Class: {record[3]}')
        print(f'Native Place: {record[4]}\n')

def delete_record():
    
    reg_no = int(input('Enter the register number to delete: '))

    index = search_record(reg_no)

    if index != -1:

        view_record(reg_no)

        confirm = input('\nAre you sure to delete the record [yes|no]: ')

        if confirm == 'yes':

            all_data.pop(index)

            print('Reacord was deleted...\n')

option = ''

while option != 'x':

    print('[a - add new profile | e - edit profile | da - display all profiles | v - view profile | d - delete profile] | x- exit')
    option = input('Choice the option: ')

    if option == 'a':

        add_record()

    elif option == 'e':

        edit_record()

    elif option == 'da':

        display_all_records()

    elif option == 'v':

        view_record()

    elif option == 'd':

        delete_record()

    elif option == 'x':

        print('\nExisting the system...')

        f1.seek(0)
        f1.truncate()

        for i in all_data:

            i = str(i)

            f1.write(f'{i}\n\n')

    else:

        print('Please enter a valid option')

f1.close()