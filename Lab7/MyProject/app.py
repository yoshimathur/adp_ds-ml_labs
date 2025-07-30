from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello-message')
def hello_message(): 
    message = {'message': 'Hello!'}
    return jsonify(message)

@app.route('/goodbye-message')
def goodbye_message():
    message = {'message': 'Goodbye!'}
    return jsonify(message)

@app.route('/custom-message/<name>')
def custom_message(name):
    message = {'message': f'Hello, {name}'}
    return jsonify(message)

@app.route('/api/v1/users')
def get_users():
    users = [
        {'id': 1, 'name': 'John'},
        {'id': 2, 'name': 'Jane'},
        {'id': 3, 'name': 'Alice'}
    ]
    return jsonify(users)

@app.route('/api/v1/posts')
def get_posts():
    posts = [
        {'id': 1, 'title': 'First Post'},
        {'id': 2, 'title': 'Second Post'},
        {'id': 3, 'title': 'Third Post'}
    ]
    return jsonify(posts)


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=8080)