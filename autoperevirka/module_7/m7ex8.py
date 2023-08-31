# В арифметичному виразі лексемами є: оператори, числа та дужки. Операторами у нас будуть такі 
# символи: *, /, - та +. Оператори та дужки легко виділити у рядку — вони складаються з одного 
# символу і ніколи не є частиною інших лексем. Числа виділити складніше, оскільки ці лексеми 
# можуть складатися з кількох символів. Тому будь-яка безперервна послідовність цифр — це одна 
# числова лексема.

# Напишіть функцію, яка приймає параметр рядок, що містить математичний вираз, і перетворює 
# його в список лексем. Кожна лексема має бути або оператором, або числом, або дужкою.

# Приклад:

# "2+ 34-5 * 3" => ['2', '+', '34', '-', '5', '*', '3']
# З метою спрощення вважаємо, що числа можуть бути тільки цілими, і вхідний рядок завжди 
# міститиме математичний вираз, що складається з дужок, чисел та операторів.

# Зверніть увагу, що лексеми можуть відокремлюватися один від одного різною кількістю прогалин, 
# а можуть і не відокремлюватися зовсім. Прогалини не є лексемами та до підсумкового списку потрапити не повинні.


def token_parser(s):
    s = s.replace(" ", "")
    rslt = []
    count = 0
    for i, ch in enumerate(s):
        if ch.isdigit() and count == 0:
            while s[i : i + count + 1].isdigit() and i + count < len(s):
                count += 1
            rslt.append(s[i: i + count])
        elif not ch.isdigit():
            rslt.append(ch)
            count = 0
    return rslt
    



s = "(2+ 34)-5 -765* 3"
print(token_parser(s))    
    
    
        
                
                