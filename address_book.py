
address_book = {
    'Oleg' : '0983528294',
    'Marshal' : '0673489292',
    'Vasya' : ' 0634901253',
}

user_key = input('Input name to get phone number:\n')

if user_key in address_book:
    print(address_book[user_key])   #   Prints phone number of [user_key] if it exists
else:
    print('\nname', '"'+user_key+'"','isn\'t registered\n')     #   Ex. of output: name Oleh isn't registered 
    choice_of_adding_name = input('Input "new" if you want to add new name to register\n\
If you don\'t want to add new name, print "exit":\n')
    
    if choice_of_adding_name == 'new':
        new_name = input('Input new name:\n')
        new_phone_number = input('Input new number:\n')
        address_book[new_name] = new_phone_number     #   Adding new person to address_book

    elif choice_of_adding_name != 'exit':
        raise NameError('Wrong command')