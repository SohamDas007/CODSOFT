#importing random and string library
import random
import string

#Taking the User Input to specify the length of the characters
len=int(input("Enter the Length of the Password:"))

#Assigning the digits, letters and symbols
chars=string.ascii_letters
chars+=string.digits
chars+=string.punctuation

#Initialising the Password Variable
password=""

#For Loop for adding characters using random library
for i in range(len):
    nxt_char=random.choice(chars)
    password+=nxt_char

#Display the Password
print("Dear User! Your New Password is:", password)