import requests
from bs4 import BeautifulSoup

url = "https://www.premiumtimesng.com/news/585884-supreme-court-extends-old-naira-notes-validity-till-december.html"

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content,"html.parser")
article = soup.find('div', {'class': 'entry-content'})
print(soup.title)
print(soup.title.get_text())
print(soup.get_text())
