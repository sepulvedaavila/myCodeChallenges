#Binary conversion

#binascii.b2a_uu(data)

import binascii

col = [0111001, 01100101, 01101111, 01101010, 01110011, 01101111, 01101111, 01110010] 
for el in col:
    print binascii.b2a_uu(str(el))
