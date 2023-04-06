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
    tmp = 2*loc - 0.092
    return  tmp - (2*np.sqrt(np.var(x))-0.092) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x)), \
            tmp - (2*np.sqrt(np.var(x))-0.092) * norm.ppf(alpha / 2) / np.sqrt(len(x))
