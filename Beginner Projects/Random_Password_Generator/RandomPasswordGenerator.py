# Random Password Generator

import random
import string

stringforpass = string.ascii_letters+string.punctuation+string.digits

pass_len=8
randomPassword=""

for i in range(pass_len):
    randomPassword+=random.choice(stringforpass)

print("Random Password : ",randomPassword)    