import requests
import redis
from bs4 import BeautifulSoup
from fastapi import FastAPI, status, Response

app = FastAPI()
r = redis.StrictRedis(host='redis', port='6379', decode_responses=True)

@app.get("/", status_code=200)
async def GetDolar(response: Response):
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
      r.set('dollar', dollar[returns[i]])
      return r.get('dollar')
      #return {'dollar': dollar[returns[i]]}
    else:
      i+=1

  response.status_code = status.HTTP_404_NOT_FOUND



