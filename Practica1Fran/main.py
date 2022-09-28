from scipy.io import arff
import pandas as pd
from sklearn import tree

data = arff.loadarff('cpu.with.vendor.arff')
df = pd.DataFrame(data[0])

print(df.head())