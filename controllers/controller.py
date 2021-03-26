from app import app
from flask import render_template, request, redirect
from models.player import Player




@app.route('/')
def index():
    return render_template('welcome.html', title="Home", game=game)

@app.route('/game')
def home():
    return render_template('index.html', title="Play", game=game)

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
    
    


    


