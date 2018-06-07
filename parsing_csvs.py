import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.line_width', 5000)
pd.set_option('display.max_columns', 60)

df = pd.read_csv('~/Downloads/TechCrunchcontinentalUSA.csv', index_col='fundedDate',
                parse_dates=['fundedDate'], dayfirst=True,)

# print('First five rows {}'.format(df[:5]))

raised = df['raisedAmt'][:5]
print('Funding raised by companies over time: \n', raised)

sns.set_style('darkgrid')
sns_plot = df['raisedAmt'].plot()
plt.ylabel('Amount raised in USD')
plt.xlabel('Funding year')
plt.savefig('AmountRaisedOverTime.pdf')