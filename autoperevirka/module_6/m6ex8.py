# Задано відомість абітурієнтів, які склали вступні іспити до університету. Структура 
# даних щодо абітурієнтів подана у вигляді наступного списку:

# [
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     },
# ]
# У кожному словнику цього списку записано прізвище абітурієнта — ключ name, код спеціальності, 
# на яку він поступив — ключ specialty, та отримані ним бали з окремих дисциплін — 
# ключі math (математика), lang ( українська мова) та eng (англійська мова)

# Розробіть функцію save_applicant_data(source, output), яка буде вказаний список із параметра 
# source зберігати у файл із параметра output

# Структура файлу для зберігання повинна бути наступною. У кожному новому рядку файлу повинні 
# бути записані через кому без прогалин прізвище абітурієнта, код спеціальності, на яку він 
# поступив, та отримані ним бали за окремими дисциплінами.

# Kovalchuk Oleksiy,301,175,180,155
# Ivanchuk Boryslav,101,135,150,165
# Karpenko Dmitro,201,155,175,185
# Вимоги:

# відкрийте файл output для запису, використовуючи менеджер контексту with та режим w.
# запис нового вмісту файлу output має бути або за допомогою методу writelines, або 
# використовувати метод write


def save_applicant_data(source, output):
    students = ''
    for student in source:
        students += '{},{},{},{},{}\n'.format(
            student['name'], 
            student['specialty'], 
            student['math'], 
            student['lang'], 
            student['eng'])
        print(students)

    with open(output, 'w') as file:
        file.write(students)


output = '/Users/sp/Docs/Projects/autoperevirka/Module 6/test.txt'
source = [{
            "name": "Kovalchuk Oleksiy",
            "specialty": 301,
            "math": 175,
            "lang": 180,
            "eng": 155,
    },
    {
            "name": "Ivanchuk Boryslav",
            "specialty": 101,
            "math": 135,
            "lang": 150,
            "eng": 165,
    },
    {
            "name": "Karpenko Dmitro",
            "specialty": 201,
            "math": 155,
            "lang": 175,
            "eng": 185,
    },]
save_applicant_data(source, output)