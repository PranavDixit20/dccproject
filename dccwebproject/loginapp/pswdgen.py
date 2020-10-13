import random
import string

# maximum length of password needed
# this can be changed to suit your password length
def passGen(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str
