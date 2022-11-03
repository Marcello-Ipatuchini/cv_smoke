import random
import string

# generate a random string
randstring = ''.join(random.sample(string.ascii_letters, 16))
print(randstring+'@fake.mail')