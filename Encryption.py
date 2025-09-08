import random
import string

char  = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)

key = char.copy()

random.shuffle(key)

# print(f"chars : {char}")
# print(f"keys :  {key}")

#Encryption
plain_text = input("Enter the input text :")
cipher_text = ""

for letter in plain_text:
    index = char.index(letter)
    cipher_text += key[index]
print(f"Original text :{plain_text}")
print(f"cipher text : {cipher_text}")

#Decryption
cipher_text = input("Enter the input text :")
plain_text = ""

for letter in plain_text:
    index = key.index(letter)
    plain_text += char[index]

print(f"cipher text : {cipher_text}")
print(f"Original text :{plain_text}")
