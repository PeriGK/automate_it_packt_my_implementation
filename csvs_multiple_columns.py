import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.line_width', 5000)
pd.set_option('display.max_columns', 60)

fundings = pd.read_csv('~/Downloads/TechCrunchcontinentalUSA.csv')
print('Type of funding:\n ',fundings[:5]['round'])

# print('First five rows {}'.format(df[:5]))

print('Selected company category and date of funding \n', fundings[
    ['company', 'category', 'fundedDate']
][800:820])

counts = fundings['category'].value_counts()
print('Most common categories of companies that raised funds: ', counts)

counts.plot(kind='barh')
plt.xlabel('Count categories')
plt.savefig('categoriesfunded.pdf')