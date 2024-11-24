from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/create-vm', methods=['POST'])
def create_vm():
    print("Received request at /create-vm")
    data = request.get_json()
    print(f"Request data: {data}")
    name = data.get('name')
    print(f"VM name received: {name}")
    response = jsonify(vmID=f'mock_vm_{name}')
    print(f"Response: {response.get_json()}")
    return response

@app.route('/run-vm', methods=['POST'])
def run_vm():
    print("Received request at /run-vm")
    data = request.get_json()
    print(f"Request data: {data}")
    vmID = data.get('vmID')
    print(f"VM ID received: {vmID}")
    response = jsonify(message=f'Hello world! from {vmID}')
    print(f"Response: {response.get_json()}")
    return response

if __name__ == '__main__':
    print("Starting mock AWS API server on port 5001...")
    app.run(host='0.0.0.0', port=5001)


