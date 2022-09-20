import requests
from bs4 import BeautifulSoup

def Job_Search(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://www.amazon.jobs/en/internal/search?base_query=&loc_query=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll("a", {"class":"job-title"}):
            href = "https://www.amazon.jobs/en/internal" + link.get("href")
            title = link.string 
            print(href)
            print(title)

        page += 1

Job_Search(1)





