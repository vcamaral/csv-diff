import pandas as pd

f1 = pd.read_csv('f1.csv')
f2 = pd.read_csv('f2.csv')

diff = f2[~f2.price.eq(f1.price)]
diff.to_csv('diff.csv', index=False)
