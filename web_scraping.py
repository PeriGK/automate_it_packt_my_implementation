from lxml import html
import requests

print('Getting pricing elements from github\'s premium plans page')
page = requests.get('https://github.com/pricing/')
tree = html.fromstring(page.content)
print("Page Object:", tree)
plans = tree.xpath('//h2[@class="pricing-card-name alt-h3"]/text()')
pricing = tree.xpath('//span[@class="default-currency"]/text()')
print("Plans:", plans, "\nPricing:", pricing)