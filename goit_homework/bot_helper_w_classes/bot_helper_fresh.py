from datetime import date, datetime
from collections import UserDict


class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def __str__(self):
        return str(self.value)


class Birthday(Field):
    def __init__(self, birthday):
        self._value = None
        self.value = birthday

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, bday):
        if bday:
            try:
                self._value = datetime.strptime(f"{bday[0:2]}-{bday[3:5]}-{bday[-4:]}", "%d-%m-%Y")
            except (TypeError, ValueError):
                print("Wrong data format")


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, phone_value):
        self._value = None
        self.value = phone_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, ph_value):
        if len(ph_value) == 10 and ph_value.isdigit():
            self._value = ph_value
        else:
            raise ValueError("Number is not valid")


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name if isinstance(name, Name) else Name(name)
        self.phones = [phone] if phone else []
        self.birthday = birthday if isinstance(birthday, Birthday) else Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday.value:
            today = date.today()
            m = self.birthday.value.month
            d = self.birthday.value.day
            dlta = date(today.year, m, d) - today
            if dlta.days >= 0:
                return dlta.days
            dlta = date(today.year + 1, m, d) - today
            return dlta.days
        else:
            print("No date of birth for this contact")
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

    def __repr__(self):
        return "\n{0}, birthday: {1}, phones: {2}".format(
            self.name.value,
            self.birthday.value,
            '; '.join(p.value for p in self.phones)
        )


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        self.index = 0

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
            return print(f"{name} was successfully deleted")
        return print(f"{name} was not found in address book")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            items = list(self.data.values())
            result = items[self.index: self.index + 2]
            self.index += 2
            return result
        else:
            self.index = 0
            raise StopIteration
