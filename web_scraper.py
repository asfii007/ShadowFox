# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "https://www.example.com/"

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

# Print all text from the page
print(soup.get_text())
