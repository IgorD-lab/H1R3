from job_processing import runner
from job_scraper import main_scraper
import json

scraped_data = main_scraper.main()

# Output as JSON
output_file = "./data/jobs_output.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(scraped_data, f, ensure_ascii=False, indent=2)
print(f"\nJob details written to {output_file}")

proceed_AI = input("Data scraping complete and written to jobs_output.json.\nDo you wish to run jobs trough AI? (y/n): ").lower().strip()
if proceed_AI != "y":
    print("Goodbye")
else:
    cv_text = "I am a Python developer i can use C, C++, python i do data science i have 0 years of experience"
    jobs_json_path = "./data/jobs_output.json"
    output_path = "./data/match_results.json"
    runner.main(cv_text, jobs_json_path, output_path)



