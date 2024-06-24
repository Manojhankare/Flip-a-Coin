from flask import Flask, render_template, request
import random

app = Flask(__name__)

def flip_coin():
    result = random.randint(0, 1)
    if result == 0:
        return "Heads"
    else:
        return "Tails"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flip', methods=['POST'])
def flip():
    if request.method == 'POST':
        outcome = flip_coin()
        return render_template('flip.html', outcome=outcome)

if __name__ == '__main__':
    app.run(debug=True)
