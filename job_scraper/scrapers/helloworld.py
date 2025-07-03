import requests
import time
import random
from bs4 import BeautifulSoup
import logging

class HelloWorldScraper:
    BASE_URL = "https://helloworld.rs/oglasi-za-posao/programiranje?"

    def __init__(self, keyword):
        self.keyword = keyword
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    def build_url(self, page_number):
        params = f"q={self.keyword}&scope=full" if self.keyword else ""
        return (
            f"{self.BASE_URL}page={page_number}&{params}&disable_saved_search=1"
            if params else
            f"{self.BASE_URL}page={page_number}&disable_saved_search=1"
        )

    def scrape_jobs(self):
        job_links = []
        seen_urls = set()
        page_number = 0
        while True:
            url = self.build_url(page_number)
            time.sleep(random.uniform(1, 3))
            resp = requests.get(url, headers=self.headers)
            if resp.status_code != 200:
                logging.warning(f"Failed to fetch {url}")
                break
            soup = BeautifulSoup(resp.text, 'html.parser')
            jobs = soup.find_all(attrs={"data-job-id": True})
            if not jobs:
                break
            for elem in jobs:
                job_id = elem["data-job-id"]
                job_url = f"https://helloworld.rs/posao/a/a/{job_id}?disable_saved_search=1"
                if job_url not in seen_urls:
                    job_links.append({"url": job_url})
                    seen_urls.add(job_url)
            page_number += 30
        return job_links
    
    def get_title():
        pass
    
    def get_description(self):
        pass