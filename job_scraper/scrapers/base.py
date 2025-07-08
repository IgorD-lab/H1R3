from typing import List, Dict

class BaseScraper:
    """
    Abstract base class for job scrapers.
    """
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    def scrape_job_links(self) -> List[Dict]:
        """
        Scrape job links from the main board.
        To be implemented by subclasses.
        """
        raise NotImplementedError

    def scrape_job_details(self, jobs: List[Dict]) -> List[Dict]:
        """
        Scrape job details for each job link.
        To be implemented by subclasses.
        """
        raise NotImplementedError

