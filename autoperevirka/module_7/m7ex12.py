# Реалізуйте функцію file_operations(path, additional_info, start_pos, count_chars), 
# яка додає додаткову інформацію в файл на шляху path з параметра additional_info, і 
# після цього повертає рядок з позиції start_pos довжиною count_chars.

# Вимоги:

# функція повинна відкривати файл за допомогою with за шляхом path в режимі додавання інформації
# записувати в кінець файлу рядок additional_info
# після запису функція має відкрити той самий файл для читання
# прочитати та повернути рядок з позиції start_pos завдовжки count_chars за допомогою функції seek.
# Важливо: для проходження завдання необхідно використовувати менеджер контексту with, методи seek, write та read.


def file_operations(path, additional_info, start_pos, count_chars):
    try:
        with open(path, "a") as file:
            file.write(additional_info)
            file.seek(start_pos)
            return file.read(count_chars)
    except IndexError:
        return ""
        
    
        
        