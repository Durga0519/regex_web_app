from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex = request.form['regex']
    try:
        matches = re.findall(regex, test_string)
    except re.error as e:
        matches = [f"Invalid regex: {e}"]

    return render_template('index.html', test_string=test_string, regex=regex, matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    is_valid = bool(re.match(email_regex, email))
    message = "Valid Email" if is_valid else "Invalid Email"
    return render_template('index.html', email=email, email_message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
