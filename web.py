# requests module
import requests

url = "https://www.google.com/"
response = requests.get(url)
print(response.text)


url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": 'mohit',
    "body": 'rawat',
    "id": 22,
}
headers = {
    'Content-type': 'application/json;charset=UTF-8',
}

response = requests.post(url, headers=headers, json=data)
print(response.text)
'''

import requests
import bs4

url = "https://www.example.com/"
response = requests.get(url)
#print(response.text)
print(type(response))

soup = bs4.BeautifulSoup(response.text, 'lxml')
print()
print(soup)

print(soup.select('title'))
print(soup.select('title')[0].getText())
print(soup.select('h1'))

print(soup.select('p'))
print(soup.select('p')[0])
print(soup.select('p')[0].getText())
'''
