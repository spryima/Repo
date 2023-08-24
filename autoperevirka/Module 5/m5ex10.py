import re


def find_word(text, word):
    dict = {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
    }
    if word in text:
        word_match = re.search(word, text)
        dict['first_index'], dict['last_index'] = word_match.span()
        dict['result'] = True
        return dict
    else:
        return dict
    
print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.","Python"))