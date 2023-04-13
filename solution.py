import pandas as pd
import numpy as np
from hyppo.ksample import MMD

chat_id = 235789175 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    pval = cramervonmises_2samp(x, y).pvalue
    alpha = 0.08 
    
    if pval < alpha:
        return True
    else:
        return False
