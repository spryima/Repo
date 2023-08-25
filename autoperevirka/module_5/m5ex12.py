import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        print(word)
        text = re.sub(r'\b{}\b'.format(word),'*' * len(word), text, re.IGNORECASE)
    return text


print(replace_spam_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0.,python', ['began', 'Python']))



