import json
from flask import Flask, jsonify, abort, redirect
from flasgger import Swagger

app = Flask(__name__)

swag = Swagger(app)


@app.route('/', methods=['GET'])
def index():
    return redirect('/apidocs/')


@app.route('/users', methods=['GET'])
def users_without_id():
    """Endpoint returning all users without id
            This is using docstrings for specifications.
            ---
            parameters:
              - name: username
                in: path
                type: string
                required: true
                default: None
            responses:
              200:
                description: A json of users
                example: hey
                schema:
                  example: {
    "test_user": {
        "name": "Test User",
        "favorite_color": "Black"
    }
}
                  $ref: '#/'
            """
    with open('static/users.json', "r+") as users:
        data = json.load(users)
    for user in data.values():
        user.pop('id')

    return jsonify(data)


@app.route('/users/<user>', methods=['GET'])
def get_user(user):
    """Endpoint returning a user
        This is using docstrings for specifications.
        ---
        parameters:
          - name: username
            in: path
            type: string
            required: true
            default: None
        responses:
          200:
            description: A json of users
            schema:
              example: {
    "test_user": {
        "id": "test",
        "name": "Test User",
        "favorite_color": "Black"
    }
}
              $ref: '#/'
        """
    with open('static/users.json', "r+") as users:
        data = json.load(users)
    if user not in data:
        abort(404)
    res = {user: data[user]}
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
