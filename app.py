from flask import Flask
from routes import helloword

app = Flask(__name__)


app.register_blueprint(helloword)

if __name__ == "__main__":
    app.run(debug=True)