from flask import Flask, request, jsonify
app = Flask(__name__)


def add(x, y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y == 0:
        return 'Error: zero division'
    return x/y

# Define API routes
@app.route('/calculate', methods=['GET'])
def calculate():
    # Get the operation and numbers from the query parameters
    operation = request.args.get('operation')
    x = float(request.args.get('x', 0))
    y = float(request.args.get('y', 0))

    # Perform the requested operation
    if operation == 'add':
        result = add(x, y)
    elif operation == 'subtract':
        result = sub(x, y)
    elif operation == 'multiply':
        result = mul(x, y)
    elif operation == 'divide':
        result = div(x, y)
    else:
        return jsonify({'error': 'Invalid operation specified'}), 400

    # Return the result as a JSON response
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
