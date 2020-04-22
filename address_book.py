import json

address_book_file = 'data.json'     #   file containing your data

with open(address_book_file, 'r') as readfile:
    address_book = json.load(readfile)                   #   Opening of data.json

status = False

user_key = input('Input name to get phone number:\n')

for name in address_book[0]['address']:     #   Loop through address_book
    if user_key in name:
        print(name[user_key])   #   Prints value of [user_key] if it exists
        status = True


if status == False:     #   if phone [user_key] doesn't exists
    print('\nname', '"'+user_key+'"','isn\'t registered\n')     #   Ex. of output:   name Oleh isn't registered 
    choice_of_adding_name = input('Input "new" if you want to add new name to register\n\
If you don\'t want to add new name, print "exit":\n')
    
    if choice_of_adding_name == 'new':
        new_name = input('Input new name:\n')
        new_phone_number = input('Input new number:\n')     #   Creating of new data


        with open(address_book_file, 'w') as writefile:
            target = address_book[0]['address']
            new_info = {new_name:new_phone_number}
            target.append(new_info)
            json.dump(address_book, writefile, indent=4)     #   Putting into data.json new data

    elif choice_of_adding_name != 'exit':   #   if command == exit: stop executing
        raise NameError('Wrong command')    #   Raises NameError if command isn't neither 'new' nor 'exit'