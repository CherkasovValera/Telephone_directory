def user_command():                                              ## Ф, которую запрашивает контроллер для цифры юзера
    num = int(input("Input \n 1. If You want to find a contact \n 2. If You want to create a new contact \n 3. If You want to see all contacts:   \n 4. If You want to close the programm: \n"))
    if 0 < num < 5:
        return num
    else:
        print("Incorrect number! The programm will be closed.")
        return 4

# # print(user_command())


def find_contact():
    find_me = input('Input contacts firstname: ')
    return find_me



def create_contact():
    new_contact = {'secondname': input('Input Secondname or press "enter" in case if you do not want to add it: ')}
    new_contact['name'] =  input('Input Firstname: ')
    while new_contact['name'] == '':
        new_contact['name'] =  input('Input Firstname: ')
    new_contact['lastname'] = input('Input Lastname or press "enter" in case if you do not want to add it: ')
    new_contact['phone_number'] = int(input('Input phone number without + sign: '))
    print(type(new_contact.get('phone_number')))
    #while new_contact.get('phone_number') == :
        #new_contact['phone_number'] = input('Input phone number without "+" sign: ')
    new_contact['comment'] = input('Leave a comment here or press "enter" in case if you do not need it: ')
    return new_contact

#print(create_contact())





from tabulate import tabulate                                       ## Таблица для вывода всех контактов

data = [{"id": "0000001", "secondname": "Писарев", "name": "Николай", "lastname": None, "phone_number": None, "comment": "Something"}, {"id": "0000002", "secondname": "Писарев", "name": "Николай", "lastname": None, "phone_number": None, "comment": "Abra-Cadabra"}]

def print_all_contacts(data):
    data_to_print = []

    for i in range(len(data)):
        data_to_print.append(list(data[i].values()))
       

    col_names = ["", "Firstname", "Lastname", "Middlename", "Phone number", "Comment"]

    print(tabulate(data_to_print, headers=col_names, tablefmt="fancy_grid", showindex="never"))

# #print_all_contacts(data)
