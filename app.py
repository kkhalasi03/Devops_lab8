from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Addition API is running!"

@app.route('/add')
def add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return {"result": a + b}
@app.route('/subtract')
def subtract():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return {"operation": "subtraction", "result": a - b}
@app.route('/multiply')
def multiply():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return {"operation": "multiplication", "result": a * b}
@app.route('/divide')
def divide():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 1))  # avoid divide by 0
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"operation": "division", "result": a / b}

if __name__ == '__main__':
    app.run()
