import random 

print("...rock...")
print("...paper...")
print("...scissors...")

p1_score = 0
p2_score = 0

while True:
    print(f"\nPlayer 1 Score: {p1_score} | Player 2 Score: {p2_score}\n")

    player1 = input("(enter Player 1's choice): ").lower()
    # player2 = input("(enter Player 2's choice): ")
    player2 = random.choice(["rock", "paper", "scissors"])

    print(f"Player 2 chose {player2}!")

    print("SHOOT!")

    if player1 == "rock" and player2 == "paper":
        print("player2 wins")
        p2_score += 1 
    elif player1 == "rock" and player2 == "scissors":
        print("player1 wins")
        p1_score += 1 
    elif player2 == "rock" and player1 == "paper":
        print("player1 wins") 
        p1_score += 1 
    elif player2 == "rock" and player1 == "scissors":
        print("player2 wins")
        p2_score += 1 
    elif player1 == "paper" and player2 == "scissors":
        print("player2 wins")
        p2_score += 1 
    elif player2 == "paper" and player1 == "scissors":
        print("player1 wins")   
        p1_score += 1 
    elif (player1 == "rock" and player2 == "rock") or (player1 == "paper" and player2 == "paper") or (player1 == "scissors" and player2 == "scissors"):
        print("nobody wins")   
    else:
        print("something went wrong")
    
    if p1_score > 2:
        print("Player 1 wins!")
        print(f"\nPlayer 1 Score: {p1_score} | Player 2 Score: {p2_score}\n")
        break
    elif p2_score > 2:
        print("Player 2 wins!")
        print(f"\nPlayer 1 Score: {p1_score} | Player 2 Score: {p2_score}\n")
        break
