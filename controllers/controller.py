from app import app
from flask import render_template, request, redirect
from models.player import Player
from random import randint




@app.route('/')
def index():
    return render_template('welcome.html', title="Home", game=game)

@app.route('/game')
def home():
    return render_template('index.html', title="Game", game=game)

@app.route('/game/<choice_1>/<choice_2>')
def game(choice_1, choice_2):

    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)

    if choice_1 == "rock" and choice_2 == "paper":
        result = f"{player_2.name} wins by playing {player_2.choice}" 

    elif choice_1 == "rock" and choice_2 == "scissors":
        result = f"{player_1.name} wins by playing {player_1.choice}" 

    elif choice_1 == "paper" and choice_2 == "rock":
        result = f"{player_1.name} wins by playing {player_1.choice}" 

    elif choice_1 == "paper" and choice_2 == "scissors":
        result = f"{player_2.name} wins by playing {player_2.choice}" 

    elif choice_1 == "scissors" and choice_2 == "rock":
        result = f"{player_2.name} wins by playing {player_2.choice}" 

    elif choice_1 == "scissors" and choice_2 == "paper":
        result = f"{player_1.name} wins by playing {player_1.choice}" 

    elif choice_1 == choice_2:
        result = "It's a draw!"

    return render_template('index.html', result=result, choice_1=choice_1, choice_2=choice_2, game=game)

@app.route('/play')
def new():
    return render_template('play.html')   
    
@app.route('/play', methods=['post'])
def computer():

    player_name = request.form['player_name']
    player_choice = request.form['player_choice']


    random_number = randint(1, 3)

    if random_number == 1:
        computer_choice = 'rock'
    elif random_number == 2:
        computer_choice = 'paper'
    elif random_number == 3:
        computer_choice = 'scissors'
    
    player = Player(player_name, player_choice)
    computer = Player("Computer", computer_choice)

    if player_choice  == "rock" and computer_choice == "paper":
        result = f"{computer.name} wins by playing {computer.choice}" 

    elif player_choice  == "rock" and computer_choice == "scissors":
        result = f"{player.name} wins by playing {player.choice}" 

    elif player_choice  == "paper" and computer_choice == "rock":
        result = f"{player.name} wins by playing {player.choice}" 

    elif player_choice  == "paper" and computer_choice == "scissors":
        result = f"{computer.name} wins by playing {computer.choice}" 

    elif player_choice  == "scissors" and computer_choice == "rock":
        result = f"{computer.name} wins by playing {computer.choice}" 

    elif player_choice  == "scissors" and computer_choice == "paper":
        result = f"{player.name} wins by playing {player.choice}" 

    elif player_choice  == computer_choice:
        result = "It's a draw!"

    return render_template('play.html', result=result)


    


    


