import random
import string

def generate_random_str(randomlength):
    '''
    string.digits = 0123456789
    string.ascii_letters = 26个小写,26个大写
    '''
    str_list = random.sample(string.digits + string.ascii_letters,randomlength)
    random_str = ''.join(str_list)
    return random_str

print(generate_random_str(randomlength=62))  #randomlength最大取值为26*2+10=62

print(string.digits)
print(string.ascii_letters)