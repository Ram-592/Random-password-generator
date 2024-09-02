# Random password generator

import random
print("Welcome to random password generator!")

randomChars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$$%^&"

num_of_password=int(input("Please enter the number of passwords to be generated: "))

password_length=int(input("Please enter the length of the password needed: "))

print("Here are your random passwords: ")

for i in range(num_of_password):
    password=""
    for j in range(password_length):
        password=password+random.choice(randomChars)
    print(password)