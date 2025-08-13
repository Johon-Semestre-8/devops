from flask import Flask, request, jsonify

app = Flask(__name__)
metrics_data = []

@app.route('/metrics', methods=['POST'])
def receive_metrics():
    data = request.get_json()
    metrics_data.append(data) 
    print(f"Received metrics: {data}")
    return jsonify({'status': 'success'}), 200

@app.route('/metrics', methods=['GET'])
def get_all_metrics():
    return jsonify(metrics_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)