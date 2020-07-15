import pandas as pd

f1 = pd.read_csv('f1.csv', delimiter=';')
f2 = pd.read_csv('f2.csv', delimiter=';')

diff = f2[~f2.price.eq(f1.price)]
diff.to_csv('diff.csv', index=False)