# Напишіть функцію real_len, яка підраховує та повертає довжину 
# рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

# Для перевірки правильності роботи функції real_len їй будуть 
# передані наступні рядки:

# 'Alex\nKdfe23\t\f\v.\r'
# 'Al\nKdfe23\t\v.\r'

def real_len(text):
    count = 0
    check_list = ["\n", "\f", "\r", "\t", "\v"]
    for num in text:
        if num in check_list:
            count += 1
    return len(text) - count


string = "Alex\nKdfe23\t\f\v.\r" # Рядок для перевірки

print("Довжина рядка без спец символів:", real_len(string))
print("Довжина рядка з спец символами:", len(string))