def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "User with such number not exist."
        except IndexError:
            return "User with such number or name not exist"

    return inner

def upsert_contact(args, contacts):
    name, phone = args
    contacts[name] = phone

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(*args):
    upsert_contact(*args)
    return "Contact added."

@input_error
def change_contact(*args):
    upsert_contact(*args)
    return "Contact updated."

@input_error
def get_contacts_phonenumber(name, contacts):
    contact = contacts[name[0].lower()]
    print(contact)

@input_error
def get_all_contacts(contacts):
    for key, value in contacts.items():
        print(f"{key}: {value}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contacts_phonenumber(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()