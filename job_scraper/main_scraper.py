import logging
from typing import List, Dict

from .scrapers.helloworld import HelloWorldScraper


def main() -> List[Dict]:
    logging.basicConfig(level=logging.INFO)
    keyword = input("Enter keyword to search for jobs: ").strip()

    scrapers = [
        HelloWorldScraper(keyword),
        # OtherSiteScraper(keyword),
        # Add more scrapers here
    ]

    all_links = []
    for scraper in scrapers:
        try:
            links = scraper.scrape_job_links()
            all_links.extend(links)
        except Exception as e:
            logging.error(f"Error scraping links: {e}")

    total_jobs = len(all_links)
    print(f"\nFound {total_jobs} jobs in total.")
    if total_jobs == 0:
        print("No jobs found. Exiting.")
        return

    proceed = input("Do you want to proceed and fetch job details? (y/n): ").strip().lower()
    if proceed != 'y':
        print("Aborted by user.")
        return

    all_details = []
    for scraper in scrapers:
        # Filter links for this scraper's domain
        scraper_links = [job for job in all_links if scraper.domain in job['url']]
        if not scraper_links:
            continue
        try:
            details = scraper.scrape_job_details(scraper_links)
            all_details.extend(details)
        except Exception as e:
            logging.error(f"Error scraping job details: {e}")
    
    return all_details
    
if __name__ == "__main__":
    main()
    
    