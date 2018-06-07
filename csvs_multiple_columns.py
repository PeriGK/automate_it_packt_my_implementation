import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

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

web_funding = fundings['category'] == 'web'
in_CA = fundings['state'] == 'CA'
in_city = fundings['city'].isin(['Palo Alto', 'San Fransisco', 'San Mateo', 
                                'Los Angeles', 'Redwood City'])

web_funding = fundings[web_funding & in_CA & in_city] 
total_counts = web_funding['city'].value_counts()
print('Funding rounds for web companies in CA:\n', web_counts)

sns.set_style("darkgrid") 
sns_plot = (total_counts*100/total_counts.astype(float)).plot(kind='barh') 

plt.xlabel("(Funding Rounds in Web Category) / (Funding Rounds in All Categories) * (100)")
plt.savefig('webFundedByCity.pdf')