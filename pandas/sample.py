import pandas as pd
import numpy as np

s1 = pd.Series([1,2,3], index=['a','b','c'])
print(s1)

print(s1['b'])
print(s1["b"])