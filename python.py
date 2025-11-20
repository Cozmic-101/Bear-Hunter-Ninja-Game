import random

def get_computer_choice():
    """Randomly selects the computer's choice."""
    choices = ["hunter", "bear", "ninja"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """Determines the winner based on game rules."""

    if player_choice == computer_choice:
        return "tie"

    winning_cases = {
        "hunter": "bear",   # Hunter shoots Bear
        "bear": "ninja",    # Bear eats Ninja
        "ninja": "hunter"   # Ninja kills Hunter
    }

    if winning_cases[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"

def play_game_with_score(max_score=3):
    """Main game loop with scoring & point system."""
    
    player_score = 0
    computer_score = 0

    player_points = 0
    computer_points = 0

    print("--- ⚔️ Bear, Hunter, Ninja: First to 3 Wins! ⚔️ ---")
    print("Rules: Bear eats Ninja, Hunter shoots Bear, Ninja kills Hunter.")
    print("Point System → Win: +2  | Tie: +1 each | Loss: 0")
    print("-" * 45)

    while player_score < max_score and computer_score < max_score:

        print(f"Score: You {player_score} - {computer_score} Computer")
        print(f"Points: You {player_points} - {computer_points} Computer")

        player_input = input("Enter your choice (Bear/Hunter/Ninja) or 'quit': ").lower().strip()

        if player_input == "quit":
            print(f"Game interrupted. Final Score: {player_score}-{computer_score}")
            print(f"Final Points: You {player_points} - {computer_points} Computer")
            return
        
        if player_input not in ["bear", "hunter", "ninja"]:
            print("Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()

        print(f"\nYou chose: {player_input.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(player_input, computer_choice)

        if result == "tie":
            print(">>> It's a TIE! +1 point each.")
            player_points += 1
            computer_points += 1

        elif result == "player":
            print(f">>> 🎉 You WIN! +2 points.")
            player_score += 1
            player_points += 2

        else:
            print(f">>> 🤖 Computer WINS! +2 points.")
            computer_score += 1
            computer_points += 2

        print("-" * 45)

    # End of match
    print("\n" + "#" * 40)
    if player_score == max_score:
        print(f"🎉 YOU WON THE MATCH {player_score}-{computer_score}!")
    else:
        print(f"🤖 COMPUTER WON THE MATCH {computer_score}-{player_score}!")
    print(f"Final Points → You {player_points} - {computer_points} Computer")
    print("#" * 40)


# Start game
if __name__ == "__main__":
    play_game_with_score(max_score=3)
