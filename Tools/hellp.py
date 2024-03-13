import random
import string

print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)         # 0123456789

print(random.random())       # it returns a random float between 0 and 1
print(random.randint(5, 10)) # it returns a random integer between 5 and 10

def random_user_id():
    letters = string.ascii_letters
    digits = string.digits
    random_value = random.random()
    return "Hello"

print(random_user_id())      # Hello
print(random.choice(range(10, 101)))  # it chooses a random element from the range [10, 101)
