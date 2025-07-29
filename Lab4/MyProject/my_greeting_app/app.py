from flask import Flask
from my_greeting_app.greeter import Greeter
import os

def create_app(): 
    app = Flask(__name__)
    greeter = Greeter()

    @app.route('/')
    def hello(): 
        greeting = greeter.say_hello()
        return greeting
    return app

if __name__ == '__main__': 
    app = create_app()
    app.run()