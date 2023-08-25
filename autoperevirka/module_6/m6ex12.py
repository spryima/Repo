# Функція get_credentials_users із попереднього завдання повертає нам 
# список рядків username:password:

# ['andry:uyro18890D', 'steve:oppjM13LL9e']
# Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі 
# data зазначений список, виконує кодування кожної пари username:password 
# у формат Base64 та повертає список із закодованими парами username:password у вигляді:

# ['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']

import base64


def encode_data_to_base64(data):
    data_base64_decoded = []
    for item in data:
        data_b = item.encode()
        data_base64 = base64.b64encode(data_b)
        data_base64_decoded.append(data_base64.decode())
    return data_base64_decoded


data = ['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']
print(encode_data_to_base64(data))
    
        