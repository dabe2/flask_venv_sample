from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://python:god@localhost/py_test'
db = SQLAlchemy(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'python'
app.config['MYSQL_PASSWORD'] = 'god'
mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/orm/init')
def init_sqlalchemy():
    db.create_all()
    return 'DB Created!'

@app.route('/orm/insert')
def insert_sqlalchemy():
    for i in range(10):
        user = User('user number '+str(i),'user email ' + str(i) + '@someaddr.com')
        db.session.add(user)
    db.session.commit()
    return 'ok'

@app.route('/test/mysqldb')
def test_mysqldb():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM py_test.user''');
    rv = cur.fetchall()
    return str(rv)

