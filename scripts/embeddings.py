import numpy as np


def average_word_vectors(tokens, embedding_model, vector_size):
    vectors = []

    for token in tokens:
        if token in embedding_model:
            vectors.append(embedding_model[token])

    if len(vectors) == 0:
        return np.zeros(vector_size)

    return np.mean(vectors, axis=0)