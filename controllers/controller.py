from app import app
from flask import render_template, request, redirect
# from models.player import Player

@app.route('/game')
def index():
    return render_template('index.html', title="Home", game=game)

@app.route('/game/<choice_1>/<choice_2>')
def game(choice_1, choice_2):
    if choice_1 == "rock" and choice_2 == "paper":
        result = f"Player 2 wins by playing {choice_2}"

    elif choice_1 == "rock" and choice_2 == "scissors":
        result = f"Player 1 wins by playing {choice_1}"

    elif choice_1 == "paper" and choice_2 == "rock":
        result = f"Player 1 wins by playing {choice_1}"

    elif choice_1 == "paper" and choice_2 == "scissors":
        result = f"Player 2 wins by playing {choice_2}"

    elif choice_1 == "scissors" and choice_2 == "rock":
        result = f"Player 2 wins by playing {choice_2}"

    elif choice_1 == "scissors" and choice_2 == "paper":
        result = result = f"Player 1 wins by playing {choice_1}"

    elif choice_1 == choice_2:
        result = "It's a draw!"

    return render_template('index.html', result=result, choice_1=choice_1, choice_2=choice_2, game=game)
    
    


    


