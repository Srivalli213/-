import requests
from bs4 import BeautifulSoup
import csv

def scrape_headlines():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request failed

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all story links
    links = soup.find_all("a", class_="storylink")

    # Extract text and URLs
    headlines = [(link.get_text(strip=True), link["href"]) for link in links]

    # Save to CSV
    with open("headlines.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "URL"])
        writer.writerows(headlines)

    print(f"Saved {len(headlines)} headlines to headlines.csv")

if __name__ == "__main__":
    scrape_headlines()
