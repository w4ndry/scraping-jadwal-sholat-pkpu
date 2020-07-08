import bs4
import requests

def jadwalSholat(url):
  contents = requests.get(url)

  response = bs4.BeautifulSoup(contents.text, "html.parser")
  data = response.find_all('tr', 'table_highlight')[0]

  sholat = {}
  i = 0

  for val in data:
    if i == 1:
      sholat['subuh'] = val.get_text()
    elif i == 2:
      sholat['zuhur'] = val.get_text()
    elif i == 3:
      sholat['ashar'] = val.get_text()
    elif i == 4:
      sholat['magrib'] = val.get_text()
    elif i == 5:
      sholat['isya'] = val.get_text()
    
    i += 1

  return sholat
