import json

from colorama import init
from colorama import Fore, Back, Style
init()                            #     colorama setup

address_book_file = 'data.json'     #   file containing your data

with open(address_book_file, 'r') as readfile:
    address_book = json.load(readfile)                   #   Opening of data.json

status = False

user_key = input('Input name to get phone number:\n').title()


def Loop():
    for name in address_book[0]['address']:     #   Loop through address_book
        if user_key in name:
            print(name[user_key])   #   Prints value of [user_key] if it exists
            global status
            status = True

Loop()


if status == False:     #   if phone [user_key] doesn't exists
    print('\nname', '"'+user_key+'"','isn\'t registered\n')     #   Ex. of output:   name Oleh isn't registered 
    choice_of_adding_name = input('Input "new" if you want to add this name to register\n\
If you don\'t want to add this name, print "exit":\n')
    


    '''Here you can add new user'''

    if choice_of_adding_name == 'new':
        new_name = user_key    #   Creating of new address_book member with [user_key] name
        new_phone_number = input('Input new number:\n')     #   Creating of new data


        
        '''Here you can check either user printed correct information or not'''

        def CheckPhoneValidation(new_phone_number):
            CheckPhoneValidationStatus = True
            if len(new_phone_number) == 10:     #   Check if new_phone_number contains 10 chars
                for char in new_phone_number:   #   Loop through each char of new_phone_number
                    if ord(char) >= 48 and ord(char) <= 57:     #   Check if each char is a digit (0-9)
                        pass
                    else:
                        CheckPhoneValidationStatus = False       #   Returns False if at least one of chars isn't a digit (0-9)
                        print(Fore.RED+'Phone number should contain only 0-9 chars')
                        break
            else:
                CheckPhoneValidationStatus = False       #   Returns False if len(new_phone_number) != 10
                print(Fore.RED+'Phone number should contain 10 chars')
            return CheckPhoneValidationStatus


        def NameValidation(new_name):
            NameValidationStatus = True
            if len(new_name) >= 3:     #   Check if name is longer than 2 chars
                for char in new_name:   #   Loop through each char of new_name
                    if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):     #   Check if each char is a letter a-z/A-Z
                        pass
                    else:
                        NameValidationStatus = False       #   Returns False if at least one of chars isn't a letter a-z/A-Z
                        print(Fore.RED+'Name should contain only a-z/A-Z chars')
                        break
            else:
                NameValidationStatus = False       #   Returns False if len(new_name) < 3
                print(Fore.RED+'Name is too short')
            return NameValidationStatus



        '''Here, finally, if user printed correct information about new user,
        we add this to our address book'''

        if NameValidation(new_name) and CheckPhoneValidation(new_phone_number):       #   If both CheckPhoneValidation() and NameValidation(new_name) return True:
            with open(address_book_file, 'w') as writefile:
                target = address_book[0]['address']
                new_info = {new_name:new_phone_number}
                target.append(new_info)
                json.dump(address_book, writefile, indent=4)     #   Putting into data.json new data
                print(Back.GREEN+'New user succesfully added')

        else:                                       #   If CheckPhoneValidation() or NameValidation() returns False:
            print(Fore.RED+Style.BRIGHT+'Invalid data')           

    elif choice_of_adding_name != 'exit':   #   if command == exit: stop executing
        raise NameError('Wrong command')    #   Raises NameError if command isn't neither 'new' nor 'exit'




else:   #   if status == True


    '''Here you can delete user'''

    delete_command = input('Input "del" if you want to delete this name from address book:\n')
    if delete_command == 'del':
        try:
            i = 0
            for name in address_book[0]['address']:     #   Loop through address_book
                if user_key in name:
                    del address_book[0]['address'][i]       #   Deletes data about [user_key]
                i+=1

            with open('data.json', 'w') as data_file:
                json.dump(address_book, data_file, indent=4)    #   Dumps new data into .json file

            print(Back.RED+'User succesfully deleted')

        except:
            print(Fore.RED+'Error. Can\'t delete this user')