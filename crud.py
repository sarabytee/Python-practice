import sqlite3

def create_table(db_connection):
    sql = 'CREATE TABLE CAT (CAT_NAME text, CAT_AGE integer, CAT_WEIGHT real, CAT_BREED text, CAT_ACTIVE_STATUS text)'
    db_connection.execute(sql)
    print('Cat table created')


def drop_table(db_connection):
    sql = 'DROP TABLE IF EXISTS CAT'
    db_connection.execute(sql)
    print('Cat table dropped')


def select_all(db_connection):
    sql = 'SELECT * FROM CAT'
    try:
        result_set = db_connection.execute(sql)
        print('\nTable has the following rows: ')
        counter = 0
        for row in result_set:
            print(row)
            counter += 1
            if counter == 0:
                print('No rows found')
    except sqlite3.OperationalError:
        return


def select_row(db_connection):
    sql = 'SELECT * FROM CAT WHERE CAT_NAME = ?'
    CAT_NAME = input('Enter the cat name: (str)')

    tuple_of_value = (CAT_NAME,)

    result_set = db_connection.execute(sql, tuple_of_value)

    for row in result_set:
        print(row)          # could also just print a print statement b/c its just one input


def insert_row(db_connection):
    sql = 'INSERT INTO CAT (CAT_NAME, CAT_AGE, CAT_WEIGHT, CAT_BREED, CAT_ACTIVE_STATUS) VALUES (?,?,?,?,?)'

    CAT_NAME = input('Enter cat name: (str)')

    CAT_AGE = int(input('Enter cat age: (int)'))

    CAT_WEIGHT = float(input('Enter cat weight: (float)'))

    CAT_BREED = input('Enter cat breed: (str)')

    CAT_ACTIVE_STATUS = input('Enter cat active status: (str)')

    tuple_of_values = (CAT_NAME, CAT_AGE, CAT_WEIGHT, CAT_BREED, CAT_ACTIVE_STATUS)

    # db_connection,execute(sql(CAT_NAME, CAT_AGE, CAT_WEIGHT, CAT_BREED, CAT_ACTIVE_STATUS)) # ANOTHER WAY TO DO IT
    db_connection.execute(sql, tuple_of_values)
    db_connection.commit()
    print('row inserted successfully')


def update_row(db_connection):
    sql = 'UPDATE CAT SET CAT_WEIGHT=? WHERE CAT_NAME=?'
    #ask user for weight to be updated
    CAT_NAME = input('Which cat has an updated weight: (str)')

    #ask user for the new cat active status
    CAT_WEIGHT = float(input('Enter the new weight: (float)'))

    tuple_of_values = (CAT_WEIGHT, CAT_NAME)
    db_connection.execute(sql, tuple_of_values)
    db_connection.commit()
    print('Row has now been updated')

def delete_row(db_connection):
    sql = 'DELETE FROM CAT WHERE CAT_NAME=?'
    CAT_NAME = input('Enter the cat name you want to delete (str): ')
    tuple_of_value = (CAT_NAME,)
    db_connection.execute(sql, tuple_of_value)
    db_connection.commit()
    print('Row has been deleted')


def display_menu(db_connection):
  greeting = ('Enter S to start a new database\n'
            'Enter C to insert a new row\n'
            'Enter R to retrieve data\n'
            'Enter U to update a row\n'
            'Enter D to delete a row\n'
            'Enter Q to quit the program')

  print(greeting)

  while True:
    choice = input("What would you like to choose? ").upper()
    if choice == "S":
        drop_table(db_connection)
        create_table(db_connection)
    elif choice == "C":
        insert_row(db_connection)
    elif choice == "R":
        select_row(db_connection)
    elif choice == "U":
        update_row(db_connection)
    elif choice == "D":
        delete_row(db_connection)
    elif choice == "Q":
        break
    else:
        print("Hmm.. That doesnt seem to match one of the choices. Try again")
    select_all(db_connection)


def main():
    db_connection = sqlite3.connect('cat.db') # this creates a db file in python module
    display_menu(db_connection)
    db_connection.close()

main()