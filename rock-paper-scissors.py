import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def display_scores():
    print(f"\nScores:\nYou: {user_score} | Computer: {computer_score}")

def play_round():
    global user_score, computer_score
    user_choice = input("\nChoose rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "win":
        print("You win this round!")
        user_score += 1
    elif result == "lose":
        print("You lose this round!")
        computer_score += 1
    else:
        print("It's a tie!")

    display_scores()

def main():
    print("=== Welcome to Rock-Paper-Scissors Game ===")

    while True:
        play_round()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing! Final Scores:")
            display_scores()
            break

if __name__ == "__main__":
    main()
