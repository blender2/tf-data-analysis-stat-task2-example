import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 469912664 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x = x * 2/t**2
    n = np.shape(x)[0]
    avg = 0.5
    x = avg - x
    alpha = 1 - p

    scale = x.min()*110
    return avg + norm.ppf(1 - alpha / 2)/n/scale, \
           avg + norm.ppf(alpha / 2)/n/scale
