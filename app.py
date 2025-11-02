from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

words = [
    "india",
    "unitedstates",
    "china",
    "russia",
    "unitedkingdom",
    "canada",
    "australia",
    "germany",
    "france",
    "japan"
]



@app.route('/')
def home():

    session['secrate_word'] = random.choice(words)
    session['guesses'] = 10
    session['display_word'] = ['_' for _ in session['secrate_word']]
    session['game_over'] = False
    return render_template('gamehomepage.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        guess = request.form['guess'].lower()
        word = session['secrate_word']
        display = session['display_word']
        guesses = session['guesses']

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    display[i] = guess
        else:
            guesses -= 1

        session['display_word'] = display
        session['guesses'] = guesses

        if '_' not in display:
            session['game_over'] = 'win'
        elif guesses == 0:
            session['game_over'] = 'lose'

        return redirect(url_for('game'))

    return render_template('gameplay.html',
                           word=session['display_word'],
                           guesses=session['guesses'],
                           game_over=session['game_over'],
                           actual_word=session.get('secrate_word'))

if __name__ == '__main__':
    app.run(debug=True)
