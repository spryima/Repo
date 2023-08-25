# Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст 
# текстового файлу source, очищений від цифр.

# Вимоги:

# прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
# запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
# запис нового вмісту файлу output має бути одноразовий і використовувати метод write


def sanitize_file(source, output):
    from re import sub 
    with open(source, 'r') as fl_source:
        text = fl_source.read()

    text = sub(r'\d', '', text)

    with open(output, 'w') as fl_output:
        fl_output.write(text)


output = '/Users/sp/Docs/Projects/autoperevirka/Module 6/test.txt'
source = '/Users/sp/Docs/Projects/autoperevirka/Module 6/test.txt'
sanitize_file(source, output)
            
    
    