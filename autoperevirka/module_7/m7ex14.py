# Напишіть функцію to_indexed(source_file, output_file), яка зчитуватиме вміст файлу, додаватиме 
# до прочитаних рядків порядковий номер і зберігати їх у такому вигляді у новому файлі.

# Кожний рядок у створеному файлі повинен починатися з його номера, двокрапки та пробілу, 
# після чого має йти текст рядка з вхідного файлу.

# Нумерація рядків іде від 0.

def to_indexed(source_file, output_file):
    lines = []
    count = 0
    with open(source_file, "r") as file:
        while True:
            line = file.readline()            
            if not line:
                break
            lines.append(f"{count}: {line}")
            count += 1
    with open(output_file, "w") as file:
        for line in lines:
            file.write(line)