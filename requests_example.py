import requests

r = requests.get('http://ip.jsontest.com/')
print('Response object: ', r)
print('Response text: ', r.text)
print('Response json: ', r.json())

print('Sending a request with data payload: ')
r = requests.get('https://github.com/search', params={'q': 'perigk'})
print('Url produced: ', r.url)
print('Status code: ', r.status_code)
print('Giant content: ', r.content)

print('\n')

# Data for post, params for get
payload_post = {'key1': 'value1'}
r = requests.post('http://httpbin.org/post', data=payload_post)
print('Response json from post: ', r.json())

print('\n')


print('Handling errors:')

try:
    r = requests.get("https://www.44wegodfdsogle.com/")
except requests.exceptions.RequestException as e:
    print("Error Response:", e)