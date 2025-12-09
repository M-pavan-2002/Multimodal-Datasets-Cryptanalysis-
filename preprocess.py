def preprocess_data(data):
    return {
        'image': data['image'],  # expects flat 64x64 = 4096 grayscale
        'text': data['text']     # expects ASCII array
    }
