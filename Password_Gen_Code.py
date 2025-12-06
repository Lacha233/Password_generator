import random 
import string

length = int(input("Enter password length: "))
include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include special characters? (y/n): ").lower() == 'y'

characters = ""
if include_upper:
    characters += string.ascii_uppercase
if include_lower:
    characters += string.ascii_lowercase
if include_digits:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

if characters:
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)
else:
    print("No character set selected!")