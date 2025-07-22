import requests
import time
import random
from bs4 import BeautifulSoup
import logging
from typing import List, Dict
from tqdm import tqdm
from .base import BaseScraper

class HelloWorldScraper(BaseScraper):
    """
    Scraper for helloworld.rs job board.
    """
    BASE_URL = "https://helloworld.rs/oglasi-za-posao/programiranje?"
    domain = "helloworld.rs"

    def __init__(self, keyword: str):
        super().__init__(keyword)

    def build_url(self, page_number: int) -> str:
        """
        Build the URL for a given page number and keyword.
        """
        params = f"q={self.keyword}&scope=full" if self.keyword else ""
        return (
            f"{self.BASE_URL}page={page_number}&{params}&disable_saved_search=1"
            if params else
            f"{self.BASE_URL}page={page_number}&disable_saved_search=1"
        )

    def scrape_job_links(self) -> List[Dict]:
        """
        Scrape all job links from the main board.
        Returns a list of dicts with 'url' key.
        """
        job_links = []
        seen_urls = set()
        page_number = 0
        with tqdm(desc="Scraping job links", unit="page") as pbar:
            while True:
                url = self.build_url(page_number)
                time.sleep(random.uniform(1, 3))
                try:
                    resp = requests.get(url, headers=self.headers, timeout=10)
                    if resp.status_code != 200:
                        logging.warning(f"Failed to fetch {url}")
                        break
                    soup = BeautifulSoup(resp.text, 'html.parser')
                    jobs = soup.find_all(attrs={"data-job-id": True})
                    if not jobs:
                        break
                    for elem in jobs:
                        job_id = elem.get("data-job-id")  # type: ignore
                        if not job_id:
                            continue
                        job_url = f"https://helloworld.rs/posao/a/a/{job_id}?disable_saved_search=1"
                        if job_url not in seen_urls:
                            job_links.append({"url": job_url})
                            seen_urls.add(job_url)
                    page_number += 30
                    pbar.update(1)
                except Exception as e:
                    logging.error(f"Error scraping links from {url}: {e}")
                    break
        return job_links

    def scrape_job_details(self, jobs: List[Dict]) -> List[Dict]:
        """
        For each job link, scrape job details: title, description, tags, seniority.
        Returns a list of dicts with all details.
        """
        detailed_jobs = []
        for job in tqdm(jobs, desc="Scraping job details"):
            url = job['url']
            try:
                resp = requests.get(url, headers=self.headers, timeout=10)
                if resp.status_code != 200:
                    logging.warning(f"Failed to fetch job detail: {url}")
                    continue
                soup = BeautifulSoup(resp.text, 'html.parser')
                title_elem = soup.find("h1")
                title = title_elem.get_text(strip=True) if title_elem else "No Title Found"

                desc_elem = soup.find("div", id="fastedit_html_oglas")
                description = ""
                if desc_elem:
                    for child in desc_elem.children:
                        text = child.get_text(strip=True)
                        description += text
                else:
                    description = "No Description Found"
                description = description.strip()

                tag_spans = soup.select('span.tag')
                tags = [span.get_text(strip=True) for span in tag_spans]
                seniority = tags[-1] if tags else "No Seniority Found"
                tags = tags[:-1] if tags else []

                detailed_jobs.append({
                    "url": url,
                    "title": title,
                    "description": description,
                    "tags": tags,
                    "seniority": seniority
                })
            except Exception as e:
                logging.error(f"Error scraping details for {url}: {e}")
                continue
        return detailed_jobs
    
    