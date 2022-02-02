from crypt import methods
from enum import unique
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'marcosgav80@gmail.com'
app.config['MAIL_PASSWORD'] = 'gxgoeioxyktvhzab'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

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
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            message = Message(subject,sender='marcosgav80@gmail.com',recipients=[email])
            message.body = msg
            mail.send(message)
            data = Data(email,subject,msg)
            db.session.add(data)
            db.session.commit()
    message = 'Message sent. You will recieve an email shortly!'
    return render_template('success.html', message=message) 


if __name__=='__main__':
    app.run(debug=True)