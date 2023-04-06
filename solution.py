import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 472321216 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    return ((loc - 0.092) / (1 - norm.ppf(alpha))) + 0.092, \
           ((loc - 0.092) / norm.ppf(1-alpha)) + 0.092
