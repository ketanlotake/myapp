import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://root:example@mongo:27017/test?authSource=admin')
db = client['test']
collection = db['pets']

# URL to scrape
url = 'http://localhost:3000/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the data you want to scrape from the page
pet_cards=soup.find_all('div',class_='card')
for card in pet_cards:
    # Find the h5 element with class 'pet-name' inside the current card
    name_elem = card.find('h5', class_='pet-name')
    if name_elem:
        name = name_elem.text.strip()
    else:
        name = None

    owner_elem=card.find('div',class_='main-content').find('p',class_='owner')
    if owner_elem:
        owner_name  = owner_elem.text.strip()
    else:
        owner_name = None

    species_elem=card.find('div',class_='main-content').find('p',class_='species')
    if species_elem:
        species  = species_elem.text.strip()
    else:
        species = None
    
    age_elem=card.find('div',class_='main-content').find('p',class_='age')
    if age_elem:
        age  = age_elem.text.strip()
    else:
        age = None

    # Find the img element inside the current card and get the 'src' attribute
    img_elem = card.find('img')
    if img_elem:
        img_url = img_elem['src']
    else:
        img_url = None
    
    data = {
        'name': name,
        'owner_name': owner_name,
        'species': species,
        'age': age,
        'poddy_trained': 'null',
        'diet': 'null',
        'image_url': img_url,
        'likes': 'null',
        'dislikes': 'null'
    }

    # Insert the scraped data into MongoDB
    collection.insert_one(data)

# Close the MongoDB connection
client.close()
