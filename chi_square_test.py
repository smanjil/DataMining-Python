
from __future__ import division
import numpy as np

values = np.array([40, 55, 35, 30, 45, 38, 45])

# calculate expexted observate(E) Mean:
expected = values.sum() / len(values)

# level of significance alpha
significance_zero_point_five = 12.52

sum = ((values - expected) ** 2 / expected).sum()

# check hypothesis
print '\nH0 is accepted!' if significance_zero_point_five > sum else '\nH1 is accepted!'
