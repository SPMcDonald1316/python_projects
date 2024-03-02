import requests
from bs4 import BeautifulSoup as bSoup

# Get user input
github_user = input('Input Github User: ')

# Use user input to complete url
url = f'https://github.com/{github_user}'

# Send request
r = requests.get(url)

# Use Beautiful Soup to grab content from request and parse html
soup = bSoup(r.content, 'html.parser')

# select the profile image src url
profile_image = soup.find('img', {'class' : 'avatar'})['src']

# print the url
print(profile_image)