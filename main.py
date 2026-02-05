import os

WEB_API_PORT = os.getenv('WEB_API_PORT')
WEB_API_VALUE = os.getenv('WEB_API_VALUE')


from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200





if __name__ == '__main__':
    app.run(debug=True, )