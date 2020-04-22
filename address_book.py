import json


address_book_file = 'data.json'     #   file containing your data

with open(address_book_file, 'r') as readfile:
    address_book = json.load(readfile)                   #   Opening of data.json

status = False

user_key = input('Input name to get phone number:\n')


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
    
    if choice_of_adding_name == 'new':
        new_name = user_key     #   Creating of new address_book member with [user_key] name
        new_phone_number = input('Input new number:\n')     #   Creating of new data

        def CheckValidation(new_phone_number):
            CheckValidationStatus = True
            if len(new_phone_number) == 10:     #   Check if new_phone_number contains 10 chars
                for char in new_phone_number:   #   Loop through each char of new_phone_number
                    if ord(char) >= 48 and ord(char) <= 57:     #   Check if each char is a digit (0-9)
                        pass
                    else:
                        CheckValidationStatus = False       #   Returns False if at least one of chars isn't a digit (0-9)
            else:
                CheckValidationStatus = False       #   Returns False if len(new_phone_number) != 10
            return CheckValidationStatus


        if CheckValidation(new_phone_number):       #   If CheckValidation() returns True:
            with open(address_book_file, 'w') as writefile:
                target = address_book[0]['address']
                new_info = {new_name:new_phone_number}
                target.append(new_info)
                json.dump(address_book, writefile, indent=4)     #   Putting into data.json new data
                print('New user succesfully added')

        else:                                       #   If CheckValidation() returns False:
            print('Invalid phone number')           

    elif choice_of_adding_name != 'exit':   #   if command == exit: stop executing
        raise NameError('Wrong command')    #   Raises NameError if command isn't neither 'new' nor 'exit'