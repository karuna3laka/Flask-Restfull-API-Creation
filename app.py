from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))  # take absolute location of the file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')

db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.cli.command('db_create')  # This decorator registers a new CLI command named db_create
def db_create():
    db.create_all()  # This method creates all the tables defined in your SQLAlchemy models in the database.
    print('DataBase created !')


@app.cli.command('db_drop')  # This decorator registers a new CLI command named db_drop
def db_drop():
    db.drop_all()  # Drops all tables from the database
    print('Database Dropped !')


@app.cli.command('db_seed')  # This decorator registers a new CLI command named db_seed
def db_seed():
    mercury = Planet(planet_name='Mercury',
                     planet_type='Class D',
                     home_star='Sol',
                     mass=3.222,
                     radius=123,  # Corrected typo: redius -> radius
                     distance=32.33333)

    earth = Planet(
        planet_name='Earth',  # Corrected attribute: name -> planet_name
        planet_type='Class M',  # Corrected attribute: type -> planet_type
        home_star='Sol',
        mass=5.972,
        radius=6371,
        distance=149.6
    )

    mars = Planet(
        planet_name='Mars',  # Corrected attribute: name -> planet_name
        planet_type='Class M',  # Corrected attribute: type -> planet_type
        home_star='Sol',
        mass=0.64171,
        radius=3389.5,
        distance=227.9
    )

    db.session.add(mercury)
    db.session.add(earth)
    db.session.add(mars)

    test_user = User(first_name='joe',
                     last_name='roguoan',
                     email='test@test.com',
                     password='p@ssw0rd')

    db.session.add(test_user)
    db.session.commit()
    print('seeded done ! ')


@app.route('/')  # decorator.special capability...define route for endpoint
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/super_simple')  # Define a simple endpoint
def super_simple():
    return jsonify(message='yahoo122')  # Corrected typo: meassage -> message


@app.route('/not_found')  # Define a not-found endpoint
def not_found():
    return jsonify(message='That resource are not found !'), 404


@app.route('/parameters')  # Define a route with query parameters
def parameters():
    name = request.args.get('name')
    age = request.args.get('age')
    if not age or not age.isdigit():  # Validate age as a number
        return jsonify(message="Invalid age parameter"), 400
    age = int(age)

    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough"), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old enough")


@app.route('/url_variable/<string:name>/<int:age>')  # Define a route with URL variables
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough"), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old enough"), 201


@app.route('/planets', methods=['GET'])
def planets():
    planets_list = Planet.query.all()
    result = planets_schema.dump(planets_list)  # Fixed schema usage
    return jsonify(result)


# data base models
class User(db.Model):  # This line defines a new class User that inherits from db.Model.
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Planet(db.Model):  # This line defines a new class Planet that inherits from db.Model.
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


class PlanetSchema(ma.Schema):
    class Meta:
        fields = ('planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')


user_schema = UserSchema()
user_schemas = UserSchema(many=True)

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)


if __name__ == '__main__':  # This block runs the app when the script is executed directly
    app.run(debug=True)
