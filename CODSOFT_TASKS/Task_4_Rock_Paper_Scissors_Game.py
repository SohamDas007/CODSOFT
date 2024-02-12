import random
from unittest import result
def is_user_choice():
    user_choice=input("Please choose rock, paper, or scissors:").lower()
    while user_choice not in ["rock","paper","scissor"]:
        print("Not Applicable. Please choose rock, paper, or scissors.")
        user_choice=input("Please choose rock, paper, or scissors:").lower()
    return (user_choice)
def is_comp_choice():
    return random.choice(["rock","paper","scissor"])
def winner(user_choice,comp_choice):
    if user_choice==comp_choice:
        return "The Game is a tie."
    elif(user_choice == 'rock' and comp_choice == 'scissors') or \
        (user_choice == 'scissors' and comp_choice == 'paper') or \
        (user_choice == 'paper' and comp_choice == 'rock'):
        return 'Congratulations!!You Have Won the Game'
    else:
        return("You Have Lost the Game. Better Luck Next Time")
def show_result(user_choice,comp_choice,result):
    print(f"\nYour Choice {user_choice}.")
    print(f"\nComputer's Choice {comp_choice}.")

    if result=="The Game is a tie.":
        print("The Game is a tie.")
    elif result=='Congratulations!!You Have Won the Game':
        print('Congratulations!!You Have Won the Game')
    else:
        print("You Have Lost the Game. Better Luck Next Time")
def play():
    score_user=0
    score_comp=0
    while True:
        user_choice=is_user_choice()
        comp_choice=is_comp_choice()
        result=winner(user_choice,comp_choice)
        show_result(user_choice,comp_choice,result)

        if result=='Congratulations!!You Have Won the Game':
            score_user+=1
        elif result=='You Have Lost the Game. Better Luck Next Time':
            score_comp+=1
        print(f"\nCurrent Scores - You: {score_user}, Computer: {score_comp}")
        repeat=input("\nDo you want to play the game again? (yes/no): ").lower()

        if repeat!='yes':
            print("You Have Exited. Thank You For Playing.")
            break

if __name__=="__main__":
    print("Dear User!! Welcome to Rock-Paper-Scissors Game!")
    play()