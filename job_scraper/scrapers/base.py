import logging
from helloworld import HelloWorldScraper
# from scrapers.other_site import OtherSiteScraper

def main():
    logging.basicConfig(level=logging.INFO)
    keyword = input("Enter keyword to search for jobs: ").strip()

    scrapers = [
        HelloWorldScraper(keyword),
        # OtherSiteScraper(keyword),
        # Add more scrapers here
    ]

    all_jobs = []
    for scraper in scrapers:
        jobs = scraper.scrape_jobs()
        all_jobs.extend(jobs)

    # TODO: Pass jobs to AI filter, extract keywords, update CV, etc.

    with open("job_postings.txt", "w") as file:
        for job in all_jobs:
            file.write(f"Found: {len(all_jobs)} jobs.\n")
            file.write(f"{job['url']}\n")

if __name__ == "__main__":
    main()