from models.player import Player



def computer_game(player, computer):

    if player.choice  == "rock" and computer.choice == "paper":
        result = f"{computer.name} wins by playing {computer.choice}" 

    elif player.choice  == "rock" and computer.choice == "scissors":
        result = f"{player.name} wins by playing {player.choice}" 

    elif player.choice  == "paper" and computer.choice == "rock":
        result = f"{player.name} wins by playing {player.choice}" 

    elif player.choice  == "paper" and computer.choice == "scissors":
        result = f"{computer.name} wins by playing {computer.choice}" 

    elif player.choice  == "scissors" and computer.choice == "rock":
        result = f"{computer.name} wins by playing {computer.choice}" 

    elif player.choice  == "scissors" and computer.choice == "paper":
        result = f"{player.name} wins by playing {player.choice}" 

    elif player.choice  == computer.choice:
        result = "It's a draw!"

    return result

def two_player_game(player1, player2):

    if player1.choice  == "rock" and player2.choice == "paper":
            result = f"{player2.name} wins by playing {player2.choice}" 

    elif player1.choice  == "rock" and player2.choice == "scissors":
        result = f"{player1.name} wins by playing {player1.choice}" 

    elif player1.choice  == "paper" and player2.choice == "rock":
        result = f"{player1.name} wins by playing {player1.choice}" 

    elif player1.choice  == "paper" and player2.choice == "scissors":
        result = f"{player2.name} wins by playing {player2.choice}" 

    elif player1.choice  == "scissors" and player2.choice == "rock":
        result = f"{player2.name} wins by playing {player2.choice}" 

    elif player1.choice  == "scissors" and player2.choice == "paper":
        result = f"{player1.name} wins by playing {player1.choice}" 

    elif player1.choice  == player2.choice:
        result = "It's a draw!"

    return result 