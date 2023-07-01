# Reddit ASX_Bets Web Scraper

This is a Python web scraper that extracts stock code mentions and performs sentiment analysis on the post titles from the ASX_Bets subreddit on Reddit.

## Prerequisites

To run this web scraper, you need to have the following installed:

- Python 3.x
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)
- NLTK library (`pip install nltk`)

## Usage

1. Clone the repository or download the source code.

2. Install the required dependencies using the following command:
 
3. Run the script:


## How It Works

1. The web scraper sends a GET request to the ASX_Bets subreddit URL using the Requests library.

2. The HTML content of the page is parsed using BeautifulSoup to extract post elements.

3. The scraper finds all post elements on the first 3 pages and stores them in a list.

4. The SentimentIntensityAnalyzer from the NLTK library is initialized for sentiment analysis.

5. The script iterates over each post and extracts the title.

6. Sentiment analysis is performed on the title using the SentimentIntensityAnalyzer, producing a compound sentiment score.

7. Stock codes mentioned in the title are identified by checking for uppercase, three-character words.

8. The count of stock code mentions is updated in a dictionary.

9. Finally, the script prints the count of stock code mentions for each code.

## Limitations and Future Improvements

- This scraper only extracts data from the first 3 pages of the ASX_Bets subreddit. You can modify the script to scrape more pages if needed.

- Sentiment analysis is performed solely on the title of each post. You may consider expanding the analysis to include other parts of the post or additional sentiment analysis techniques.

- This script does not handle cases where stock codes appear as abbreviations or acronyms that are not in uppercase. Improving the stock code identification logic can make it more robust.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request.





