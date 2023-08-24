# Для закріплення матеріалу напишіть функцію find_all_words, яка шукає збіг слова в тексті. 
# Функція повертає список всіх знаходжень слова в параметрі word в тексті у вигляді будь-якого 
# написання, тобто, наприклад, можливі варіанти написання слова "Python" як pYthoN, pythOn, 
# PYTHOn і т.і. головне, щоб зберігався порядок слів, регістр не має значення.

# Підказка: функції модуля re приймають ще ключовий параметр flags і ми можемо визначити 
# нечутливість до регістру, надавши йому значення re.IGNORECASE

import re


def find_all_words(text, word):
    return re.findall(word, text, re.IGNORECASE)


print(find_all_words('pYthoN, pythOn, PYTHOn','python'))