import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

plt.style.use('default')

pd.set_option('display.line_width', 5000)
pd.set_option('display.max_columns', 60)

df = pd.read_csv('~/Downloads/TechCrunchcontinentalUSA.csv', index_col='fundedDate', parse_dates=['fundedDate'], dayfirst=True,)

funds = df[['raisedAmt', 'round']] 
funds['month'] = funds.index.month
print ("Funding Rounds with Month Index:\n", funds)