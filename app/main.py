import os
from flask import Flask

"""
Flask Documentation: 
https://flask.palletsprojects.com/en/stable/

OS lib: 
https://docs.python.org/3/library/os.html
"""

app = Flask(__name__

# WEB_API_PORT = os.getenv('WEB_API_PORT')
# WEB_API_VALUE = os.getenv('WEB_API_VALUE')

@app.route("/health")
def health():
    return "OK", 200

@app.route("/value")
def value():
    return os.getenv('WEB_API_VALUE')



"""
 if __name__ == '__main__' Allows app.run to run when script is executed.
 Added some validation incase if 'WEB_API_PORT' is not set as an Enviornment variable

 Took a while to find port as an optional parameter in the documentation but found this:
 https://www.geeksforgeeks.org/python/how-to-change-port-in-flask-app/

 On docker, I couldnt get the app to work, found that there was option to set host for external visbility 
 and it helped; https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application

"""

if __name__ == '__main__':
    if os.getenv('WEB_API_PORT') == None:
        print("Please assign a port to the enviornment variable WEB_API_PORT")
    elif os.getenv('WEB_API_VALUE') == None:
        print("Please assign a value to the enviornment variable WEB_API_VALUE")
    else:
        app.run(host="0.0.0.0", port=os.getenv('WEB_API_PORT'))
        #Adding host="0.0.0.0" fixed my none response problem (only for docker)

