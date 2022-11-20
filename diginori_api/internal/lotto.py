import random


def predict_lotto_number():
    lotto = random.sample(range(1, 45), 6)
    return lotto
