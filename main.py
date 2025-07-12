from job_processing import runner
from job_scraper import main_scraper

scraped_data = main_scraper.main()

print(scraped_data)