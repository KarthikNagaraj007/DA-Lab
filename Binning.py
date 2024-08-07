# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:40:04 2021

@author: Kar
"""
import pandas as pd
import numpy as np

# Generate 20 random integers uniformly between 0 and 99
small_counts = np.random.randint(0, 100, 20)
print(small_counts)
# Map to evenly spaced bins 0-9 by division
print(np.floor_divide(small_counts, 10))

large_counts = [296, 8286, 64011, 80, 3, 725, 867, 2215, 7689, 11495, 91897, 44, 28, 7971, 926, 12]
# print(np.floor(np.log10(large_counts)))
#Map the counts to quartiles into 4 bins (quartile)
print(pd.qcut(large_counts, 4, labels=False))
#convert large_counts into series data
large_counts_series = pd.Series(large_counts)
# print(large_counts_series)
print(large_counts_series.quantile([0.25, 0.5, 0.75]))
