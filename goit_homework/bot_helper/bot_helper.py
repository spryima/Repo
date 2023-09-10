def green_print(text):
    print(f'\033[92m{text}\033[0m')


def red_print(text):
    print(f'\033[91m{text}\033[0m')


def input_error(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            red_print("Give me name and phone, please.")
        except KeyError:
            red_print("There is no such name in contact list")
        except IndexError:
            red_print("Enter user name and phone number")
        return 
    return inner


def parser(message):
    for key in command_list:
        m = message.lower()
        if m.startswith(key): # searching for prefix with command
            return key, message[len(key):].strip().split(" ") # return command (key) and following list of arguments
    for exit_command in exit_commands:
        if message.startswith(exit_command):
            return exit_command, []
    return message.lower(), []


@input_error
def change(edited_contact):
    contact_list[edited_contact[0]] = edited_contact[1]
    green_print(f"{edited_contact[0]}'s number was successfully changed to {edited_contact[1]}")


@input_error    
def phone(person_name):
    print(contact_list[person_name[0]])


@input_error
def add(new_contact):
    if new_contact[0] in contact_list:
        return red_print(f"Contact {new_contact[0]} is already exists")
    contact_list[new_contact[0]] = new_contact[1]
    return green_print(f"New contact: {new_contact[0]} - {new_contact[1]} was added successfully")


def show_all(_):
    output = []
    for person, phone in contact_list.items():
        output.append(f"{person} - {phone}")
    return "\n".join(output)


exit_commands = ("exit", "close", "good bye")
contact_list = {}
command_list = {
    "hello": lambda _: green_print("How can I help you?"),
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all,
    }

def main():
    message = ""
    green_print("""Hello, I'm Bot-Helper. I'm here to help you with calendar and contacts.
These are common Bot commands:
    hello                   - just type it :)
    add                     - add New Contact
    change                  - change phone number of existing contact
    phone                   - show phone number of Contact
    show all                - show all Contacts
    good bye, close, exit   - any of this stop Bot
Let's start!
          """)
    
    while True:
        message = input("   >>> ").strip()
        command, args = parser(message)

        if command in exit_commands:
            break
        elif command in command_list:
            response = command_list[command](args)
            if response:
                print(response)
        else:
            red_print("Unknown command. Try again.")

    green_print("Good Bye!")
if __name__ == "__main__":
    main()
