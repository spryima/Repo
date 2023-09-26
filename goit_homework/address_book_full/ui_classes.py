import os
from abc import abstractmethod, ABC
from ab_classes import (
    Phone, 
    Birthday, 
    Name, 
    Contact, 
    AddressBook,
    )

class BaseUserInterface(ABC):
    @abstractmethod
    def ask_question_input(self):
        pass

    @abstractmethod
    def show_all_contacts(self):
        pass

    @abstractmethod
    def show_help(self):
        pass

    @abstractmethod
    def show_message(self):
        pass

    @abstractmethod
    def show_start_message():
        pass

class ConsoleUserInterface(BaseUserInterface):
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

delete all                          - delete Address Book
"""
    
    @staticmethod
    def green_print(text):
        print(f'\033[92m{text}\033[0m', end="")
    
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def ask_question_input(self, message):
        answer = input(message)
        return answer

    def show_all_contacts(self, ab_obj: AddressBook):
        for rec in ab_obj.values():
            print(rec)

    def show_help(self):
        print(self.help_message)
    
    def show_message(self, message):
        print(message)

    def show_start_message(self):
        ConsoleUserInterface.clear_screen()
        ConsoleUserInterface.green_print('                 "ADDRESS BOOK"')
        print()
        ConsoleUserInterface.green_print("help  ")
        print("- to get more information  about commands")