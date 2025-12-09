def dummy_rnn(text_array):
    # Simulate RNN output by modulating ASCII values
    score = sum(text_array) % 100 / 100.0
    return score
