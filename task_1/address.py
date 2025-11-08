from collections import UserDict


class Field:
    def __init__(self, value):
        self.validate(value)
        self.value = value

    def __str__(self):
        return str(self.value)

    def validate(self, value):
        pass

    def set(self, value):
        self.value = value

    def get(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    def validate(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("incalidValie")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.get() == old_phone:
                phone.set(new_phone)

    def find_phone(self, phone_to_find):
        for phone in self.phones:
            if phone.get() == phone_to_find:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]

    def delete(self, name):
        self.data.pop(name)
