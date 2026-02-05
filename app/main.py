import os
from flask import Flask



app = Flask(__name__)

WEB_API_PORT = os.getenv('WEB_API_PORT')
WEB_API_VALUE = os.getenv('WEB_API_VALUE')

@app.route("/health")
def health():
    return "OK", 200

@app.route("/value")
def value():
    return WEB_API_VALUE



"""
 if __name__ == '__main__' Allows code to only run when script is executed.
 Added some validation incase if 'WEB_API_PORT' is not set as an Enviornment variable

"""

if __name__ == '__main__':
    if os.getenv('WEB_API_PORT') == None:
        print("Please assign a port to the enviornment variable WEB_API_PORT")
    if os.getenv('WEB_API_VALUE') == None:
        print("Please assign a value to the enviornment variable WEB_API_VALUE")
    else:
        app.run(host="0.0.0.0", port=WEB_API_PORT)
        #Adding host="0.0.0.0" fixed my none response problem

