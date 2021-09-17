from bs4 import BeautifulSoup
import requests
print("Enter the type of image(Eg:Happy Images,Crying Images etc.")
image = input('>')
url = f"https://unsplash.com/s/photos/{image}"
r = requests.get(url).text
soup = BeautifulSoup(r,"html5lib")
images = soup.find_all("img",class_="oCCRx")
for imag in images:
    print(imag.get("src"))
    print("")


