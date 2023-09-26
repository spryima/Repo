import re
from ui_classes import ConsoleUserInterface
import json
from pathlib import Path
from ab_classes import (
    Phone, 
    Birthday, 
    Name, 
    Contact, 
    AddressBook,
    )


def input_error(func):
    def wrapper(ui, *args):
        try:
            return func(ui, *args)
        except Exception as e:
            ui.show_message(e)
    return wrapper


@input_error
def add_command(ui, name, *args):

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
    ui.show_message(f"Add success")


def parser(text):
    for cmd, kwds in command_list.items():
        for kwd in kwds:
            if text.lower().startswith(kwd):
                return cmd, text[len(kwd):].strip().split(" ")
    return unknown_command, []


def unknown_command(ui, *args):
    ui.show_message("Unknown command")


def exit_command(ui, *_):  
    contacts = []
    for rec in address_book.values():
        contacts.append(
            {
            "name": rec.name.value,
            "phone": [phone.value for phone in rec.phone],
            "birthday": rec.birthday if rec.birthday == "" else rec.birthday.value,
            }
        )       

    current_dir = Path(__file__).resolve().parent
    with open(current_dir / "contacts.json", "w") as fh:
        json.dump(contacts, fh)
    ui.show_message(f"Good bye!")
    

def find_command(ui, name):
    ui.show_message("\n".join(str(rec) for rec in address_book.values() if name in str(rec)))

@input_error
def change_command(ui, name, *args):
    if name in address_book:
        rec = address_book[name]
        if re.search(r"[a-zA-z]", args[0]):
            address_book.change_name(name, args[0])
        elif args[0].isdigit():
            rec.change_phone(args[0], args[1])
        else:
            rec.change_birthday(args[0])
        ui.show_message(f"Change success")
    else:
        ui.show_message(f"No such contact in Address Book")


def show_all_command(ui, *_):
    ui.show_all_contacts(address_book)
    

def delete_all_command(ui, *_):
    final_check = ui.ask_question_input(f"\033[91mDo you really want to Delete Address Book?\033[0m  Y/n >> ")
    if final_check.lower() == "y":
        address_book.delete_all()
        ui.show_message("Address Book has been deleted.")
    else:
        ui.show_message("Operation cancelled.")

@input_error
def delete_command(ui, name):
    if name in address_book:
        address_book.delete(name)
        ui.show_message(f"Contact {name} was deleted successfully")
    else:
        ui.show_message(f"No such contact in Address Book")
    

def help_command(ui, *_):
    ui.show_help()


address_book = AddressBook()
command_list = {
    add_command: ("add", "+"),
    find_command: ("find",),
    change_command: ("change",),
    show_all_command: ("show all", "show"),
    delete_all_command: ("delete all",),
    delete_command: ("delete", "del"),
    help_command: ("help",),
    exit_command: ("exit", "quit", "good buy"),
}

def main():
    ui = ConsoleUserInterface()
    # json Address Book import 
    current_dir = Path(__file__).resolve().parent
    path_to_json = Path(current_dir / "contacts.json")
    if path_to_json.is_file():
        with open(path_to_json, "r") as fh:
            records = json.load(fh)
            for json_rec in records:
                contact_obj = Contact(Name(json_rec["name"]))
                contact_obj.birthday = Birthday(json_rec["birthday"]) if json_rec["birthday"] else ""
                contact_obj.phone = [Phone(phone) for phone in json_rec["phone"]] if json_rec else []
                address_book.add_contact(contact_obj)

    ui.show_start_message()

    while True:
        message = ui.ask_question_input("   >>> ").strip()

        cmd, data = parser(message)

        response = cmd(ui, *data)
        if response:
            ui_console.show_message(response)
        
        if cmd == exit_command:  
            break


if __name__ == "__main__":
    main()
