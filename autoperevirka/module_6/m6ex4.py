# Реалізуйте функцію add_employee_to_file(record, path), яка у файл (параметр 
# path - шлях до файлу) буде додавати співробітника (параметр record) у вигляді 
# рядка "Drake Mikelsson,19".

# Вимоги:

# параметр record - співробітник у вигляді рядка виду "Drake Mikelsson,19"
# кожен запис у файл має починатися з нового рядка.
# необхідно щоб стара інформація у файлі теж зберігалася, тому при роботі 
# з файлом відкрийте файл у режимі 'a', додайте співробітника record у 
# файл і закрийте його 

# ми поки що не використовуємо менеджер контексту with

def add_employee_to_file(record, path):
    file = open(path, 'a')    
    file.write(record + '\n')
    file.close()


path = '/Users/sp/Docs/Projects/autoperevirka/Module 6/test.txt'
record = 'Drake Mikelsson,19'
add_employee_to_file(record, path)