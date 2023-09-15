from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass

class Phone(Field):
    def __init__(self, phone_value):
        if not self.is_valid_number(phone_value):
            raise ValueError("Phone number is not valid")
        super().__init__(phone_value)

    def is_valid_number(self, value):
        if not value.isdigit():
            return False
        return True if len(value) == 10 else False
            

class Record:
    def __init__(self, name_value):
        self.name = Name(name_value)
        self.phones = []

    def add_phone(self, number):
        phone_obj = Phone(number)
        self.phones.append(phone_obj)
    
    def remove_phone(self, number):
        for phone_obj in self.phones:
            if phone_obj.value == number:
                self.phones.remove(phone_obj)
                return print(f"Number was successfully deleted")
        print(f"{self.name.value} doesn't have such number")

    def edit_phone(self, old_number, new_number):
        for phone_obj in self.phones:
            if phone_obj.value == old_number:
                phone_obj.value = new_number
                return
        raise ValueError(f"{self.name} doesn't have such number")
            
    def find_phone(self, number):
        for phone_obj in self.phones:
            if phone_obj.value == number:
                return phone_obj
        print(f"{self.name} doesn't have such number")

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
