###### Tutorials Used
# https://medium.com/daily-python/consuming-nasa-api-using-python-part-1-daily-python-17-4ce104fa47ab
######

### Libraries
import requests
import os
from pprint import PrettyPrinter
from datetime import date


### Initialize Variables
url_apod="https://api.nasa.gov/planetary/apod"
url_neo="https://api.nasa.gov/neo/rest/v1/feed"
url_neo_browse="https://api.nasa.gov/neo/rest/v1/neo/browse"
url_epic="https://api.nasa.gov/EPIC/api/natural/"

NASA_API_KEY = os.environ.get("NASA_API_KEY")

# NASA_API_KEY = os.getenv('NASA_API_KEY')
# NASA_API_KEY = os.environ['NASA_API_KEY']


### Main
def main():
  today = str(date.today())
  pp = PrettyPrinter()
  
  
  ### Attempt 1
  
  response = requests.get('https://api.nasa.gov/planetary/api/apod')
  pp.pprint(response)
  ## The result is only a 404 because  we didn't add anything authentication
  
  
  
  ### Attempt 2
  
  params = {'api_key': NASA_API_KEY , 'date': today}
  response = requests.get(url_apod,params=params).json()
  # print(response.keys())
  pp.pprint(response)
  print(response['hdurl'])
  
  
  ### Attempt 3
  
  # response = requests.get(url_neo,params=params).json()
  # pp.pprint(response)
  
  # response = requests.get(url_neo_browse,params=params).json()
  # pp.pprint(response)
  
  ### Attempt 4 EPIC ( Earth Polychromatic Imaging Camera) API

  
  response = requests.get(url_epic,params=params).json()
  pp.pprint(response)
  
def fetchEPICImage():
  YEAR = '2015'
  MONTH = '10'
  DAY = '31'
  IMAGE_ID = 'epic_1b_20151031074844'
  URL_EPIC = "https://epic.gsfc.nasa.gov/archive/natural/"
  URL_EPIC = URL_EPIC + YEAR +'/' + MONTH + '/'+DAY
  URL_EPIC = URL_EPIC + '/png'
  URL_EPIC = URL_EPIC + '/' + IMAGE_ID + '.png' 
  print(URL_EPIC)
  
fetchEPICImage()

if __name__ == "__main__":
  main()  





