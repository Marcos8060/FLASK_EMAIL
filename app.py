from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    message = 'Your message is sent successfully!'
    return render_template('success.html', message=message) 


if __name__=='__main__':
    app.run(debug=True)