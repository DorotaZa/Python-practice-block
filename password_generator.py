import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the Pyssword Generator!")
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_digits = int(input("How many digits would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like in your password?\n"))

#simple version
# password = ""
# for ch in range(1, num_of_letters + 1):
#     password += (random.choice(letters))
# print(password)
#
# for dig in range(1, num_of_letters + 1):
#     password += (random.choice(digits))
# print(password)
#
# for sym in range(1, num_of_letters + 1):
#     password += (random.choice(symbols))
# print(password)

#shuffled version
password_list = []
for ch in range(1, num_of_letters + 1):
    password_list.append(random.choice(letters))
print(password_list)

for dig in range(1, num_of_letters + 1):
    password_list.append(random.choice(digits))
print(password_list)

for sym in range(1, num_of_letters + 1):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")

