from flask import Flask # create web APIs
app = Flask(__name__)

# app is a flask instance. .route tells where code becomes available
# methods are curl calls, same route can do different things depending
@app.route('/hello', methods=["GET","POST"]) # decorator -- save time, available for import
def hello_world():
    return "Hello World"

@app.route('/<name>', methods=["GET"]) # 
def hello_name(name):
    return f"Hello, {name}"

# if you import this somewhere else, you dont want the flask app running
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
