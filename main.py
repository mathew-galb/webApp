import os
from flask import Flask


app = Flask(__name__)

WEB_API_PORT = os.getenv('WEB_API_PORT')
WEB_API_VALUE = os.getenv('WEB_API_VALUE')

@app.route("/health")
def health():
    return "OK", 200



"""
 if __name__ == '__main__' Allows code to only run when script is executed.
 Added some validation incase if 'WEB_API_PORT' is not set as an Enviornment variable

"""

if __name__ == '__main__':
    if os.getenv('WEB_API_PORT') == None :
        print("Please assign a port to the enviornment variable WEB_API_PORT")
    else:
        app.run(debug=True, port=WEB_API_PORT)