import requests
from bs4 import BeautifulSoup

url = "https://old.reddit.com/r/ASX_Bets/"

# Send a GET request to the URL
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the post elements on the page
posts = soup.find_all("div", class_="thing")

# Iterate over each post and extract the title and number of likes
for post in posts:
    title = post.find("a", class_="title").text
    likes = post.find("div", class_="score unvoted").text
    
    print("Title:", title)
    print("Likes:", likes)