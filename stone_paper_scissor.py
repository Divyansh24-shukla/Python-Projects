import random
while(1>0):
    print("Stone, Paper or Scissors Game.")
    Number = int(input('''Enter the number:
    1 for Stone, 
    2 for Scissor,
    3 for Paper\n'''))

    random_number = random.randint(1,3)
    if Number > 3:
        print("Please enter a Valid Number.")
    elif Number ==random_number:
        print("It's a Draw!")
                                            # Player Won
    elif Number ==1 and random_number == 2:
        print('''You Choose: Stone
    Computer Choose: Scissor
    YOU WON!''')
    elif Number == 2 and random_number == 3:
        print('''You Choose: Scissor
    Computer Choose: Paper
    YOU WON!''')
    elif Number == 3 and random_number == 1:
        print('''You Choose: Paper
    Computer Choose: Stone
    YOU WON!''')
                                            # Computer Won
    elif Number ==2 and random_number == 1:
        print('''You Choose: Scissor
    Computer Choose: Stone
    Computer WON!''')
    elif Number == 3 and random_number == 2:
        print('''You Choose: Paper
    Computer Choose: Scissor
    Computer WON!''')
    elif Number == 1 and random_number == 3:
        print('''You Choose: Stone
    Computer Choose: Paper
    Computer WON!''')
