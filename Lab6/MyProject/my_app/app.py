from flask import Flask
from my_app.message import Message
import os

def create_app():
    app = Flask(__name__)
    message = Message()

    @app.route("/")
    def getMessage():
        messageText = message.say_hi()
        return messageText
    return app

if __name__ == '__main__':
    port = int(os.getenv('PORT') or 5000)  # Use PORT environment variable if available, otherwise use 5000
    app = create_app()
    app.run(host='0.0.0.0', port=port)