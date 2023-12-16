from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, value):
        if not (len(value) == 10):
            raise ValueError("Invalid phone number format")
        self.value = value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, current_phone, new_phone):
        for idx, phone in enumerate(self.phones):
            if phone.value == current_phone:
                self.phones[idx] = Phone(new_phone)

    def delete_phone(self, current_phone):
        self.phones = [phone for phone in self.phones if phone.value != current_phone]

    def find_phone(self, current_phone):
        for phone in self.phones:
            if phone.value == current_phone:
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
