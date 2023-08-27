# Дуже часто люди у своїх повідомленнях не ставлять великі літери, особливо це стало 
# масовим явищем в еру мобільних. пристроїв. Розробіть функцію capital_text, яка прийматиме 
# на вхід рядок з текстом і повертатиме рядок з відновленими великими літерами.
# Функція повинна:
# зробити великою першу літеру в рядку, попри прогалини
# зробити великою першу літеру після точки, попри прогалини
# зробити великою першу літеру після знака оклику, попри прогалини
# зробити великою першу літеру після знака питання, попри прогалини

def capital_text(s):
    check_next_letter = True
    ls = list(s)
    for i, char in enumerate(ls):        
        if char in ('!','?','.'):
            check_next_letter = True
        if check_next_letter and char.isalpha():
            ls[i] = char.upper()
            check_next_letter = False
    s = ''.join(ls)
    return s


#                        Ще один варіант за допомогою регулярних виразів
# import re

# def capital_text(s):
#     def make_upper(match):
#         return match.group(0).upper()
#     s = re.sub(r'(^\w|\.\s*\w|\!\s*\w|\?\s*\w)', make_upper, s)
#     return s

s = 'привіт! люди як справи.все добре?     чи ні? '
print(capital_text(s))
    
    
    
        
    
        
    
    
        
            
            
                
            
                
        
    