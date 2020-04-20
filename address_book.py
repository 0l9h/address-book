address_book = {
    'Oleg' : '0983528294',
    'Marshal' : '0673489292',
    'Vasya' : ' 0634901253',
}

user_key = input('Input name to get phone number:\n')

if user_key in address_book:
    print(address_book[user_key])   #   Prints phone number of [user_key] if it exists
else:
    print('name', '"'+user_key+'"','isn\'t registered')     #   Ex. of output: name Oleh isn't registered 