from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from models.cnn_model import dummy_cnn
from models.rnn_model import dummy_rnn
from models.fusion_model import fuse_features
from utils.preprocess import preprocess_data

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    if not data or 'image' not in data or 'text' not in data:
        return jsonify({'error': 'Invalid input format'}), 400

    processed = preprocess_data(data)
    image_score = dummy_cnn(np.array(processed['image']))
    text_score = dummy_rnn(processed['text'])
    final_score, verdict = fuse_features(image_score, text_score)

    return jsonify({
        'score': final_score,
        'verdict': verdict
    })

@app.route('/')
def home():
    return 'API is running. Use POST /analyze'

if __name__ == '__main__':
    app.run(debug=True)
