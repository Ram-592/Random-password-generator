# Random password generator

import random
print("Welcome to random password generator!")

letters=("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
numbers= ("1234567890")
symbols=("!@#$$%^&")
num_of_letters=int(input("How many letters you want in your password?\n"))
num_of_numbers=int(input("How many numbers you want in your password?\n"))
num_of_symbols=int(input("How many symbols you want in your password?\n"))
password=""
print("Here are your random passwords: ")
for i in range (num_of_letters):
    char=random.choice(letters)
    password+=char
for i in range(num_of_numbers):
    char=random.choice(numbers)
    password+=char
for i in range(num_of_symbols):
    char=random.choice(symbols)
    password+=char

password_list = list(password)
random.shuffle(password_list)
shuffled_password=''.join(password_list)
print(shuffled_password)
