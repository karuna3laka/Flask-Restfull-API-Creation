from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))  # take absolute location of the file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')

db = SQLAlchemy(app)

@app.route('/')  # decorator.special capability...define route for endpoint
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/super_simple')
def super_simple():
    return jsonify(meassage='yahoo122')  # make these valid jason


@app.route('/not_found')
def not_found():
    return jsonify(message='That resource are not found !'), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not Old enough"), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old Enough")


from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/url_variable/<string:name>/<int:age>')  # Corrected route definition
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough"), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old enough"), 201


# data base models

class User (db.Model):  #This line defines a new class User that inherits from db.Model.
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)











if __name__ == '__main__':
    app.run(debug=True)
