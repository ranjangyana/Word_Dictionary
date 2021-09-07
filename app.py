from flask import Flask, render_template, request
from textblob import TextBlob, Word

# initialize the app
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/submit', methods = ["POST"])
def form_data():

    data = request.form.get('text')

    # Find word definations

    defination = Word(data).definitions

    return render_template('form.html', data = defination)
    

if __name__ == '__main__':
    app.run(debug=True)