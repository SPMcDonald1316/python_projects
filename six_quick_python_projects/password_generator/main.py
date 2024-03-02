import random

print('''Password Generator
==================''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&()<>?,.0123456789'

num_of_passwords = int(input('Enter number of passwords to be created: '))
password_length = int(input('Enter the length of created passwords: '))

print('''
Passwords
---------''')

for pwd in range(num_of_passwords):
  password = ''
  for char in range(password_length):
    password += random.choice(chars)
  print(password)

print()