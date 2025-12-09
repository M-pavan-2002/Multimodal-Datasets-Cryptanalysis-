def fuse_features(img_score, txt_score):
    final_score = (img_score + txt_score) / 2
    verdict = 'vulnerable' if final_score > 0.5 else 'secure'
    return final_score, verdict
