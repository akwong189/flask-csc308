from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

users = { 
    'users_list' :
    [
        { 
            'id' : 'xyz789',
            'name' : 'Charlie',
            'job': 'Janitor',
        },
        {
            'id' : 'abc123', 
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id' : 'ppp222', 
            'name': 'Mac',
            'job': 'Professor',
        }, 
        {
            'id' : 'yat999', 
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
            'id' : 'zap555', 
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}

@app.route('/')
def hello_world():
        return 'Hello, World!'

def generate_ids():
    return "%06d" % (random.randint(1, 1000000))

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')
        if search_username:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username and not search_job:
                    subdict['users_list'].append(user)
                elif user['name'] == search_username and user['job'] == search_job:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = generate_ids()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True), 201
        return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if id :
        if request.method == 'GET':
            for user in users['users_list']:
                if user['id'] == id:
                    return user
            return ({})
        elif request.method == 'DELETE':
            for user in users['users_list']:
                if user['id'] == id:
                    users['users_list'].remove(user)
                    resp = jsonify(), 204
                    return resp
            resp = jsonify({"msg:": "user id not found"}), 404
            return resp
    return users