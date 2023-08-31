message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

for ch in message:
    if  ch.islower():
        pos = ord(ch) - ord('a')
        new_char = chr((pos + offset ) % 26 + ord('a')) 
        encoded_message += new_char        
    elif ch.isupper():
        pos = ord(ch) - ord('A')
        new_char = chr((pos + offset ) % 26 + ord('A')) 
        encoded_message += new_char
    else:
        encoded_message += ch

print(encoded_message)