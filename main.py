from job_processing import runner
from job_scraper import main_scraper
import config
import json


# Path
jobs_output_file = config.JOBS_OUTPUT_PATH
ai_output_path = config.AI_OUTPUT_PATH
cv_path = config.CV_PATH

# Get text from CV
try:
    with open(cv_path, "r", encoding="utf-8") as f:
        cv_text = f.read().strip()
except FileNotFoundError:
    cv_text = "I am a Python developer i can use C, C++, python i do data science i have 0 years of experience"
    
# Scrape job data
scraped_data = main_scraper.main()

# Output as JSON
with open(jobs_output_file, "w", encoding="utf-8") as f:
    json.dump(scraped_data, f, ensure_ascii=False, indent=2)
print(f"\nJob details written to {jobs_output_file}")   
print("Job scraping complete. Now you can run the AI evaluation on the scraped jobs.")

# Ask user if they want to proceed with AI evaluation
proceed_AI = input("Do you wish to run jobs through AI? (y/n): ").lower().strip()
if proceed_AI != "y":
    print("Goodbye")
else:
    runner.main(cv_text, jobs_output_file, ai_output_path)



