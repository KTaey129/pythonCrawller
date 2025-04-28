import requests
from bs4 import BeautifulSoup
import csv
import time

# 크롤링할 대상 URL
URL = "https://news.ycombinator.com/"

def fetch_news():
    """뉴스 페이지를 요청해서 HTML 반환"""
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()  # HTTP 에러 발생 시 예외 발생
        return response.text
    except requests.RequestException as e:
        print(f"[Error] Failed to fetch page: {e}")
        return None

def parse_news(html):
    """HTML을 파싱해서 뉴스 제목과 링크 추출"""
    soup = BeautifulSoup(html, "html.parser")
    titles = []

    for item in soup.select(".titleline > a"):
        title = item.get_text(strip=True)
        link = item.get("href")
        titles.append({"title": title, "link": link})

    return titles

def save_to_csv(data, filename="news.csv"):
    """뉴스 데이터를 CSV 파일로 저장"""
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "link"])
            writer.writeheader()
            writer.writerows(data)
        print(f"[Success] Saved {len(data)} news articles to {filename}")
    except IOError as e:
        print(f"[Error] Failed to write CSV: {e}")

def main():
    start_time = time.time()
    print("[Info] Starting news scraping...")

    html = fetch_news()
    if html:
        news_list = parse_news(html)
        if news_list:
            save_to_csv(news_list)
        else:
            print("[Warning] No news found on the page.")
    else:
        print("[Error] Could not fetch the news page.")

    end_time = time.time()
    print(f"[Info] Scraping completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
