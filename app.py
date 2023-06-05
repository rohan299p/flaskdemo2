from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']  # Get the user input from the input box
        result = process_query(query)  # Process the input to get the result
        return render_template('index.html', result=result)
    return render_template('index.html')

def process_query(query):
    # Placeholder logic for generating a response
    responses = ["Hello!", "How can I assist you?", "Nice to meet you!"]
    return random.choice(responses)

if __name__ == '__main__':
    app.run(debug=True)
