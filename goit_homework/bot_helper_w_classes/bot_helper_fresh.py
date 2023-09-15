from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    ...

class Phone(Field):
    def __init__(self, phone_value):
        if not self.is_valid_number(phone_value):
            raise ValueError("Phone number is not valid")
        super().__init__(phone_value)

    def is_valid_number(self, value):
        return True if len(value) == 10 else False
            

class Record:
    def __init__(self, name_value):
        self.name = Name(name_value)
        self.phones = []

    def add_phone(self, number):
        phone_obj = Phone(number)
        self.phones.append(phone_obj)
    
    def remove_phone(self, number):
        if number in self.phones:
            self.phones.remove(number)
            print(f"Number was successfully deleted")
        else:
            print(f"{self.name.value} don't have such number")

    def edit_phone(self, old_number, new_number):
        try:
            index = self.phones.index(old_number)
            self.phones[index] = new_number
        except ValueError:
            print(f"{self.name.value} doesn't have such number")

    def find_phone(self, number):
        if number in self.phones:
            return number
        print(f"{self.name.value} doesn't have such number")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
              
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
            return print(f"{name} was successfully deleted")
        return print(f"{name} was not found in address book")



