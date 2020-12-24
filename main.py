import requests
from bs4 import BeautifulSoup
url = "http://pincode.india-server.com/cities/kolkata/"
r = requests.get(url)
htmlconent = r.content
soup = BeautifulSoup(htmlconent, 'html.parser')
table = soup.find("table", class_="pincode-tbl")
ls = table.tbody.find_all("tr")

print("{")
try:
    for i in ls:
        if i.find("td", colspan="4") == None:
            print('"',(i.find_all("td")[1]).get_text(),'"', ' : "', (i.find_all("td")[3]).get_text(), '",',)
except:
    pass
print("}")
# python3 main.py > <city-name>.json