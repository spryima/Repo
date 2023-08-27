# Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) 
# для знаходження слова, що шукається в рядку ребуса.

# Параметри функції:

# riddle - рядок із зашифрованим словом.
# word_length – довжина зашифрованого слова.
# start_letter - літера, з якої починається слово (мається на увазі, що до початку 
# слова літера не зустрічається в рядку).
# reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому. 
# Для значення True слово зашифроване у зворотньому порядку, наприклад, у рядку 
# 'mi1rewopret' зашифроване слово 'power'.
# Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути 
# пустий рядок.


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if start_letter in  riddle: 
        letter_index = riddle.index(start_letter)
        if reverse:
            return riddle[letter_index : letter_index - word_length : -1]
        else:
            return riddle[letter_index : letter_index+word_length]
    return ''

#                     Альтернативний варіант
# def solve_riddle(riddle, word_length, start_letter, reverse=False):
#     try:
#         letter_index = riddle.index(start_letter)
#         if reverse:
#             return riddle[letter_index : letter_index - word_length : -1]
#         else:
#             return riddle[letter_index : letter_index + word_length]
#     except ValueError:
#         return ''


print(solve_riddle('qwerpasbcdefg', 4, 's', True))