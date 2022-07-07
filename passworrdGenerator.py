import random

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("----------PyPassword Generator----------\n".center(100))

no_char=int(input("Number of characters required in your password\n"))
no_dig=int(input("Number of digits required in your password\n"))
no_sym=int(input("Number of symbols required in your password\n"))

passList=[] #Defining an empty list

for i in range(0,no_char):
    passList.append(random.choice(characters))
for i in range(0,no_dig):
    passList.append(random.choice(digits))
for i in range(0,no_sym):
    passList.append(random.choice(symbols))

random.shuffle(passList) #Random shuffling of list
print("".join(passList))
