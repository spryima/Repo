from ab_classes import (
    Phone, 
    Birthday, 
    Name, 
    Contact, 
    AddressBook, 
    )
import re


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            return e
    return wrapper


@input_error
def add_command(name, *args):

#  is name in AddressBook
    if name in address_book:
        rec = address_book[name]
    else:
        rec = Contact(Name(name))
        address_book.add_contact(rec) 

# is *args phone or birthday
    for arg in args:
        if arg.isdigit():
            phone_obj = Phone(arg)
            rec.add_phone(phone_obj)
        if  any(char in arg for char in ('\\', '.', '/', '-')):
            birthday_obj = Birthday(arg)
            rec.add_birthday(birthday_obj)
    return f"Add success"

def parser(text):
    for cmd, kwds in command_list.items():
        for kwd in kwds:
            if text.lower().startswith(kwd):
                return cmd, text[len(kwd):].strip().split(" ")
    return unknown_command, []


def unknown_command():
    return f"Unknown command"

def exit_command(*_):
    return f"Good bye!"
    

def find_command(val):
    for rec in address_book.values():
        if val in str(rec):
            print(rec)


@input_error
def change_command(name, *args):
    if name in address_book:
        rec = address_book[name]
        if re.search(r"[a-zA-z]", args[0]):
            address_book.change_name(name, args[0])
        elif args[0].isdigit():
            rec.change_phone(args[0], args[1])
        else:
            rec.change_birthday(args[0])
        return f"Change success"
    else:
        return f"No such contact in Address Book"


def show_all_command(*_):
    for rec in address_book.values():
        print(rec)


@input_error
def delete_command(name):
    if name in address_book:
        address_book.delete(name)
        return f"Contact {name} was deleted successfully"
    else:
        return f"No such contact in Address Book"
    

def help_command(*_):
    return help_message






help_message = """
                        List of all commands:
help   - show this list


add name [phone] [birthday]         - add New contact (phone and birthday are optional)
add Bill 0123456789 01.01.1987      - add New contact w phone and birthday
add Bill                            - add New contact
add Bill 0123456789                 - add New contact or add New Phone to contact
add Bill 01.01.1987                 - add New contact or add Birthday to contact


find name|number                    - find matches in user names or phone numbers
find ike                            - find all contacts matching "ike"
find 0934                           - find all contacts matching phone with "0934"


delete Bill
delete name                         - delete existing contact

show all                            - show all contacts in Address Book

change [name] [phone] [birthday]    - change name/phone/birthday 
change Bill Mike                    - change Bill to Mike
change Bill 1234567890 1111111111   - change Bill's phone number
change Bill 12.11.1987 01.11.1991   - change Bill's birthday
change Bill 1231231230              - delete Bill's 1231231230 number

remove phone - 
add phone - add phone to existing contact
birthday - show days to birthday 
"""
address_book = AddressBook()
command_list = {
    add_command: ("add", "+"),
    find_command: ("find",),
    change_command: ("change",),
    show_all_command: ("show all", "show"),
    delete_command: ("delete", "del"),
    help_command: ("help",),
    exit_command: ("exit", "quit", "good buy"),
}

def main():

    while True:
        message = input("   >>> ").strip()

        cmd, data = parser(message)

        response = cmd(*data)
        if response:
            print(response)
        
        if cmd == exit_command:  
            break



if __name__ == "__main__":
    main()
