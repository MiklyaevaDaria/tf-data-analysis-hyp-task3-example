import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 819168380

def solution(control_npv: np.array, test_npv: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    t_value, p_value = ttest_ind(control_npv, test_npv, equal_var=False)
    return p_value < 0.09
