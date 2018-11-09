import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
wiki = "https://en.wikipedia.org/wiki/List_of_Miami_Heat_seasons"
response = http.request('GET', wiki)
soup = BeautifulSoup(response.data, "lxml")

maindiv = soup.findAll('div', class_='mw-parser-output')
table = soup.find('table', class_="wikitable plainrowheaders")

ratio_list = []

for row in table.findAll("tr"):
    for cell in row.findAll("td"):

        plain_cell = cell.text
        if len(plain_cell) == 4:
            ratio_list.append(float(plain_cell))

            ratio_total = sum(ratio_list) / len(ratio_list)

print("Miami Heat total win ratio through " + str(len(ratio_list)) +
" seasons equals " + str("%.3f" % ratio_total))