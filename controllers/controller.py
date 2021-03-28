from app import app
from flask import render_template, request, redirect
from models.player import Player
from random import randint
from models.game import computer_game, two_player_game


@app.route('/')
def index():
    return render_template('welcome.html', title="Home", game=game)

@app.route('/game')
def home():
    return render_template('index.html', title="Game", game=game)

@app.route('/game', methods=['post'])
def game():

    player1_name = request.form['player1_name']
    player1_choice = request.form['player1_choice']

    player2_name = request.form['player2_name']
    player2_choice = request.form['player2_choice']

    player1 = Player(player1_name, player1_choice)
    player2 = Player(player2_name, player2_choice)

    result = two_player_game(player1, player2)

    return render_template('index.html', result=result, game=game)

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

    result = computer_game(player, computer)

    return render_template('play.html', result=result)


    


    


