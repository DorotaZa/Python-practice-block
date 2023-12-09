line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]

position = input("Show me where do you want to put your treasure?\n")
letter = position[0].lower() #in case the user writes the capital letter
abc = ["a", "b", "c"]
letter_index = abc.index(letter) #checking if input matches 3 letters to choose from
#print(letter_index)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X" #number_index first, because we look at the map vertically first

print(f"{line1}\n{line2}\n{line3}")
#print(map)
