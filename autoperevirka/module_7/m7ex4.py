def is_integer(s):
    s = str(s).strip()
    if len(s) > 0 and s.isdigit():
        return True
    elif (s[:1] == '+' or '-') and s[1:].isdigit():
        return True
    return False


print(is_integer( -34 ))
        
    