# Реалізуйте функцію get_credentials_users(path), яка повертає список 
# рядків із бінарного файлу, створеного в попередньому завданню, де:

# path – шлях до файлу.
# Формат файлу:

# andry:uyro18890D
# steve:oppjM13LL9e
# Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте 
# список рядків із файлу та поверніть його з функції get_credentials_users 
# у наступному форматі:

# ['andry:uyro18890D', 'steve:oppjM13LL9e']
# Вимоги:

# Використовуйте менеджер контексту для читання з файлу

def get_credentials_users(path):
    users_credentials = []
    with open(path, 'rb') as file:
        while True:
            line = file.readline()
            if not line:
                break
            users_credentials.append(line.decode())
    for i in range(len(users_credentials)):
        users_credentials[i] = users_credentials[i].replace('\n', '')
    return users_credentials
    



path = '/Users/sp/Docs/Projects/autoperevirka/Module 6/test.txt'
print(get_credentials_users(path))