import random
heads = int(input("How many people are there?\n"))
name_list = []
for i in range(0, heads):
    Names = input("Enter the Names.")
    name_list.append(Names)

print(name_list)

final = random.choice(name_list)

print(final,"will pay the bill!")
 