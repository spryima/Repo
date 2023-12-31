from datetime import datetime
from collections import UserDict
import re
from exceptions_classes import NoSuchPhone, InvalidFormat

class Field():
    def __init__(self, value) -> None:
        self.__value = ""
        self.value = value

    def __str__(self) -> str:
        return self.value if self.value else "N/A"


class Name(Field):
    @property
    def value(self):    
        return self.__value
    
    @value.setter
    def value(self, value):
        if re.search(r"[a-zA-Z]", value):
            self.__value = value
        else:
            raise InvalidFormat(f"Invalid name format. Use at least 1 letter, please")


class Phone(Field):
    @property
    def value(self):
       return self.__value

    @value.setter
    def value(self, value):
        if value:
            if len(value) == 10:
                self.__value = value
            else:
                raise InvalidFormat(f"Invalid Phone format. Use 10 digits, please")
    def __repr__(self) -> str:
        return self.value

class Birthday(Field):
    @property
    def value(self):
        return self.__value.strftime("%d.%m.%Y")

    @value.setter
    def value(self, bday):  
        if re.match(r"[0-3][0-9][.|\\|/|-](([0][1-9])|([1][0-2]))[.|\\|/|-]\d{4}",bday):
            self.__value = datetime.strptime(f"{bday[0:2]}-{bday[3:5]}-{bday[-4:]}", "%d-%m-%Y")
        else:
            raise InvalidFormat(f"Invalid Birthday format. Use -> dd.mm.yyyy")


class Contact():
    def __init__(self, name_obj: Name, phone_obj: Phone = "", birthday_obj: Birthday = "") -> None:
        self.name = name_obj
        self.phone = [phone_obj] if phone_obj else []
        self.birthday = birthday_obj if birthday_obj else ""
        
    def add_phone(self, phone_obj: Phone):
        if phone_obj.value not in [phone_obj.value for phone_obj in self.phone]:
            self.phone.append(phone_obj)

    def add_birthday(self, birthday_obj: Birthday):
        self.birthday = birthday_obj

    def change_phone(self, old_phone: str, new_phone: str):
        if old_phone in [phone_obj.value for phone_obj in self.phone]:
            self.phone.append(Phone(new_phone))
            for index, ph_obj in enumerate(self.phone):
                if ph_obj.value == old_phone:
                    self.phone.pop(index)
        else:
            raise NoSuchPhone("Contact {self.name.value} doesn't have such number")

    def change_birthday(self, birthday: str):
        self.birthday.value = birthday
        
    def __repr__(self) -> str:
        return "Name: {:<10} Phone: {:<15} Birthday: {}".format(
            self.name.value,
            ", ".join(str(ph) for ph in self.phone),
            self.birthday if self.birthday == "" else self.birthday.value,
        )


class AddressBook(UserDict):
    def add_contact(self, rec_obj: Contact):
        self.data[rec_obj.name.value] = rec_obj
    
    def change_name(self, old_name: str, new_name: str):
        self.data[old_name].name.value = new_name
        self.data[new_name] = self.data[old_name]
        del self.data[old_name]

    def delete(self, name: str):
            del self.data[name]
    
    def delete_all(self):
        self.data.clear()


