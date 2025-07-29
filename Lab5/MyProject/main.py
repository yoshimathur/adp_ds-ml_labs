from my_greeting_app.greeter import Greeter
import os

def main(port):
    greeter = Greeter()
    greeting = greeter.say_hello()
    print(f"Greeting on port {port}: {greeting}")

if __name__ == '__main__':
    # Allow port to be overridden
    port = int(os.environ.get('PORT', 5000))
    main(port)