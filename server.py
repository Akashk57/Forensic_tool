from flask import Flask, request, jsonify
from sklearn.ensemble import IsolationForest

app = Flask(__name__)
clf = IsolationForest()

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    content = file.read()
    feature = [[len(content) % 1000]]
    clf.fit([[i] for i in range(5)])  # Dummy fit
    pred = clf.predict(feature)[0]
    return jsonify({
        "tampered": pred == -1,
        "confidence": 0.5
    })

if __name__ == '__main__':
    app.run(port=5000)

