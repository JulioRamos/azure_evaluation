from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def guess():
    message = ''
    guesses = []
    if request.method == 'POST':
        user_num = int(request.form['user_num'])
        guess_count = 0
        guess_range = [1, 20]
        while guess_count < 3:
            guess_num = random.randint(guess_range[0], guess_range[1])
            guess_count += 1
            if guess_num == user_num:
                message = f"Sorry, the app guessed correctly ({guess_num}). You lose!"
                break
            else:
                guesses.append((guess_num, "correct" if guess_num == user_num else "incorrect"))
                if guess_num < user_num:
                    guess_range[0] = guess_num + 1
                else:
                    guess_range[1] = guess_num - 1
        else:
            message = f"You win! The number {user_num} was not correctly guessed by my app."
    return render_template('cv.html', message=message, guesses=guesses)

@app.route('/restart')
def restart():
    return redirect(url_for('guess'))



if __name__ == '__main__':
   app.run()