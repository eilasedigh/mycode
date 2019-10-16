#!/usr/bin/env python3

round=0
answer= " "
while round<3 and answer !="Brian":
    round+=1
    print('Finish the movie title,"Monday Python\'s The life of -------"')
    answer=input("Your guess-->")

    if answer == 'Brian':
        print('Correct')
        break
    elif answer.lower() == 'shrubbery':
        print(' You gave the super secret answer!')
        break
    elif round == 3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")


