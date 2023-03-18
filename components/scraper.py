import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['test']
collection = db['pets']

# URL to scrape
url = 'https://linkedin.com/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
# Find the data you want to scrape from the page
#data = {}
#data['title'] = soup.title.string
#data['description'] = soup.find('meta', attrs={'name': 'description'})['content']

# Insert the scraped data into MongoDB
#collection.insert_one(data)

# Close the MongoDB connection
#client.close()