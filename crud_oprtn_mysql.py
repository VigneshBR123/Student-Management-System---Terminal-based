import mysql.connector as conn

connection = conn.connect(
    user = 'xxxxxx',
    host = 'xxxxxx',
    database = 'studentsdb',
    password = 'xxxxx'
)

cur = connection.cursor(dictionary=True)

print('\nStudent Management System\n')

# To add new records

def add_record():

    cur.execute('select max(Register_No) from students_records;')

    all_records = cur.fetchall()

    reg_no = all_records[0]['max(Register_No)']

    if reg_no == None:

        reg_no = 1

    else:

        reg_no += 1

    print(f'Register No: {reg_no}')

    name = input('Enter the name: ')

    age = input('Enter the age: ')

    student_class = input('Enter the class: ')

    native = input('Enter the native: ')

    cur.execute(f"insert into students_records (Register_No, Name, Age, Class, Native) values ({reg_no},'{name}',{age},'{student_class}','{native}');")

    print('Successfully data updated in student records....\n')

def edit_record():

    reg_no = int(input('Enter the register no: '))

    status = view_record(reg_no)

    if status:

        print(f'Register No: {reg_no}')

        name = input('Enter the name: ')

        age = input('Enter the age: ')

        student_class = input('Enter the class: ')

        native = input('Enter the native: ')

        cur.execute(f"update students_records set Name = '{name}', Age = {age}, Class = '{student_class}', Native = '{native}' where Register_No = {reg_no};")

def display_all_records():

    cur.execute('select * from students_records;')

    records = cur.fetchall()

    if len(records) >= 1:

        for i in range(len(records)):

            print()

            for j,k in records[i].items():

                print(f'{j} : {k}')

            print()

    else:

        print('\n No student records found \n')        

def view_record(reg_no = None):

    if reg_no == None:

        reg_no = int(input('Enter the register number to view: '))

    cur.execute(f'select * from students_records where Register_no = {reg_no};')

    record = cur.fetchall()

    if len(record) > 0:

        print()

        for i,j in record[0].items():

            print(f'{i} : {j}')

        print()

        return True
        
    else:

        print('Record not found\n')

        return False

def delete_record():

    reg_no = int(input('Enter the register no: '))

    status = view_record(reg_no)

    if status:

        confirm = input('Are you sure to delete [y - yes | n - no]: ')

        if confirm == 'y':

            cur.execute(f'delete from students_records where Register_No = {reg_no};')

            print(f'Record with register number {reg_no} was deleted successfully.')

choice = ''

while choice != 'x':
    
    print('[a - add new profile | e - edit profile | da - display all profiles | v - view profile | d - delete profile] | x- exit')
    choice = input('Choice the option: ')

    if choice == 'a':

        add_record()

    elif choice == 'e':

        edit_record()

    elif choice == 'da':

        display_all_records()

    elif choice == 'v':

        view_record()

    elif choice == 'd':

        delete_record()

    elif choice == 'x':

        print('\nExisting the system...')
        
        cur.close()

        connection.commit()

    else:

        print('Please enter a valid option')