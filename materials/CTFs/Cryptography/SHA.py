# Python 3 code to demonstrate
# SHA hash algorithms.

import hashlib


str = "VeraCrypt"

# encoding GeeksforGeeks using encode()
# then sending to SHA1()
result = hashlib.sha1(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
