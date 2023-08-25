# The rgb function is incomplete. Complete it so that passing in RGB decimal 
# values will result in a hexadecimal representation being returned. Valid 
# decimal values for RGB are 0 - 255. Any values that fall out of that range 
# must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 
# will not work here.

# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"


def rgb(r, g, b):
    r = format(max(min(r, 255), 0), '02x')
    g = format(max(min(g, 255), 0), '02x')
    b = format(max(min(b, 255), 0), '02x')
    return f'{r.upper()}{g.upper()}{b.upper()}'



print(rgb(-20, 255, 155))


