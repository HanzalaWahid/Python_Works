# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True)
print ("This is a test")
from flask import Flask

app = Flask(__name__)

# Your routes and other application configurations go here

if __name__ == "__main__":
    app.run(debug=False)
