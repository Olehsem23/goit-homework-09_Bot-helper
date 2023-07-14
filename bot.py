# Бот-помічник. Розпізнає команди, що вводяться з клавіатури, і відповідає відповідно до введеної команди.
address_book = {}  # Словник з користувачами та їхніми телефонами.


def input_error(func):  # Декоратор. Обробляє помилки при вводі.
    def wrapper(*args):
        try:
            return func(*args)
        except KeyError:
            return f"No user with name {args[0]}"
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name and phone'
    return wrapper


@input_error
def hello_user():  # Відповідь на команду 'Hello'
    return "Hello! How can I help you?"


@input_error
def add_command(*args):  # Додаємо користувача з номером до словника користувачів
    name = args[0]
    phone = args[1]
    address_book[name] = phone
    return f"Contact {name} with phone {phone} was added successfully"


@input_error
def change_command(*args):  # Заміна телефона для користувача.
    # name, phone = args
    name = args[0]
    phone = args[1]
    old_phone = address_book[name]
    address_book[name] = phone
    return f'{name} has new number: {phone} . Old number: {old_phone}'


@input_error
def show_all():  # Видрукувати весь список імен і телефонів зі словника address_book.
    if len(address_book) == 0:  # Якщо словник порожній.
        return 'Address book is now empty. Please add some users'
    else:
        result = ''
        print(f'There are {len(address_book)} users in address book')
        for name, phone in address_book.items():
            result += f'Name: {name} phone: {phone}\n'
        return result


@input_error
def phone_command(*args):  # Пошук телефона вибраного користувача.
    name = args[0]
    phone = address_book[name]
    return f'{name} has phone: {phone}'


def exit_command():  # Вихід з програми.
    return 'Bye. Have a nice day. See you next time.'


def unknown_command():  # Коли вводимо невідому команду.
    return 'Unknown command. Try again'


# COMMANDS - словник, де ключі - це функції, які викликаються при наборі відповідної команди з кортежу можливих команд.
COMMANDS = {
    hello_user: ('hello', 'hi', 'aloha', 'привіт'),
    add_command: ('new user', 'add', '+'),
    change_command: ('change phone for', 'change', 'зміни', 'замінити'),
    show_all: ('show all', 'all phones', 'addressbook', 'phonebook'),
    phone_command: ('show number', 'phone', 'number', 'show'),
    exit_command: ('bye', 'exit', 'end', 'close', 'goodbye')
}


def parser(text: str):  # Парсер команд
    for cmd, keywords in COMMANDS.items():
        for kwd in keywords:
            if text.lower().startswith(kwd):
                # print(cmd)
                data = text[len(kwd):].strip().split()
                # print(data)
                return cmd, data
    return unknown_command, []
                   

def main():  # Головна функція програми. Ввід команд.
    while True:
        user_input = input('Enter your command and args: ')

        cmd, data = parser(user_input)

        result = cmd(*data)

        print(result)  

        if cmd == exit_command:  # Вихід з бота
            break


if __name__ == "__main__":  # Точка входження
    main()
