print("hello world!")
#function and takes a password string as a inputs and returns sits SHA-256 hashed representation as a hexadecimal string
import hashlib
def hash_password(password):
 password_bytes = password.encode('utf-8')
 hash_object = hashlib.sha256(password_bytes)
 password_hash = hash_object.hexdigest()
 return password_hash
password = input("Input your password: ")
hashed_password = hash_password(password)
print(f"Your hashed password is: {hashed_password}") 

#A Python program that defines a function to generate random passwords of a specified length. The
function takes an optional parameter length, which is set to 8 by default. If no length is specified by the
user, the password will have 8 characters


import random
import string
def generate_password(length=8):
all_characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all_characters) for i in range(length))
 return password
password_length_str = input("Input the desired length of your password:")
if password_length_str:
 password_length = int(password_length_str)
else:
 password_length = 8
password = generate_password(password_length)
print(f"Generated password is: {password}") 
