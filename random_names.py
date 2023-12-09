import random

list_of_names = ["George", "Lisa", "Eugene", "Mark", "Charlotte"]
num_of_names = len(list_of_names)
random_choice = random.randint(0, num_of_names - 1)
random_name = list_of_names[random_choice]

print(f"{random_name} you pay today!")