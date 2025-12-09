def dummy_cnn(image_array):
    # Simulate CNN by returning normalized pixel average
    score = image_array.mean() / 255.0
    return score
