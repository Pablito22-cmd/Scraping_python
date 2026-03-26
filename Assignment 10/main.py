import numpy as np
import pandas as pd

raNums = np.random.default_rng(0)
ranSeries = pd.Series(raNums.integers(0,100,10))//10