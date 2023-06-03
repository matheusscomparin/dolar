import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def GetDolar():
  url = ['https://dolarhoje.com/', 'https://www.google.com/search?q=dolar+hoje&oq=dolar&aqs=chrome.0.35i39i650j69i59j0i67i433i650l2j0i67i650j0i67i433i650j0i67i131i433i650j69i60.681j0j4&sourceid=chrome&ie=UTF-8']
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
  atributos = [{'id':'nacional'}, {'class':'DFlfde SwHCTb'}]
  returns = ['value', 'data-value']
  locs = ['input','span']
  i = 0

  while (i < len(url)):
    page = requests.get(url[i], headers=headers)
    if page.status_code == 200:
      soup = BeautifulSoup(page.content, 'html.parser')
      dollar = soup.find_all(locs[i], attrs=atributos[i])[0]
      return {'dollar': dollar[returns[i]]}
    else:
      i+=1

  if i >= len(url):
    return 502
  else:
    pass

