import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors Game!")

    while True:
        user_choice = input("\nChoose rock, paper, or scissors (or 'exit' to end): ").lower()

        if user_choice == 'exit':
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"\nScore - You: {user_score}  Computer: {computer_score}")

    print("Thanks for playing!")

if __name__ == "__main__":
    rock_paper_scissors_game()
