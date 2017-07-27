from bs4 import BeautifulSoup
import requests



r = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")

data = r.content
soup = BeautifulSoup(data,'html.parser')

print(soup.find(id="current-conditions"))
