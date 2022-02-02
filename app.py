from crypt import methods
from enum import unique
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://marcos:getaways@localhost/email_messenger'

db = SQLAlchemy(app)

# user model
class Data(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String,unique=True)
    subject = db.Column(db.String(120))
    message = db.Column(db.String(255))

    def __init__(self,email,subject,message):
        self.email = email
        self.subject = subject
        self.message = message


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST','GET'])
def success():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']
        print(email,subject,msg)
        data = Data(email,subject,msg)
        db.session.add(data)
        db.session.commit()
    message = 'Your message is sent successfully!'
    return render_template('success.html', message=message) 


if __name__=='__main__':
    app.run(debug=True)