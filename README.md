# News Scraper 📰

A simple Python web scraper that collects the latest news headlines from [Hacker News](https://news.ycombinator.com/) and saves them to a CSV file.

## Features
- Fetches the main page of Hacker News
- Parses news titles and links
- Saves the data into a `news.csv` file
- Includes basic error handling for network and file I/O
- Clean and beginner-friendly code structure

## Technologies Used
- Python 3.x
- Requests
- BeautifulSoup4

## How to Run
1. Clone this repository.
2. Install the dependencies:
    ```bash
    pip install requests beautifulsoup4
    ```
3. Run the script:
    ```bash
    python news_scraper.py
    ```
4. The news will be saved into a file called `news.csv`.

## Example CSV Output
| title | link |
|:---|:---|
| Example News Title 1 | https://example.com/1 |
| Example News Title 2 | https://example.com/2 |

## when executed
![news_scraper result](./images/result.png)
