from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')  # decorator.special capability...define route for endpoint
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/super_simple')
def super_simple():
    return jsonify(meassage='yahoo122') #make these valid jason

@app.route('/not_found')
def not_found():
    return jsonify(message='That resource are not found !'), 404

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18 :
        return jsonify(message="Sorry " + name + ", you are not Old enough"), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old Enough")


if __name__ == '__main__':
    app.run()
