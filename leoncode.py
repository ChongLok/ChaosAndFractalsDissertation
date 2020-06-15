import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import groupby
import time
from numba import jit
from collections import Counter
import pandas as pd

def test(l):
    s=pd.Series(l)
    s[s.duplicated()].unique().tolist()
    return(s)
x=test([1.1,1,2,3,4,4,1.1,2,6,4,8,6,4])
print(x)