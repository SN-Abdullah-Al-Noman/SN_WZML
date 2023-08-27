from flask import Flask
app = Flask(__name__)

@app.route('/')
def inddex():
    return "LCUBOTS"

if __name__ == "__main__":
    app.run()
