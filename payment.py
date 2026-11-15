from flask import Flask

app = Flask(__name__)

def calculate (a, b):
    c = a+b
    return c

@app.route("/")
def index():

    return "This is a payment page! Please pay %s USD"%(calculate(10, 20))

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)