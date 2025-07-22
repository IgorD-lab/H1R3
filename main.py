from job_processing import runner
from job_scraper import main_scraper
import config
import json


def load_cv_text(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            cv_text = f.read().strip()
    except FileNotFoundError:
        print(f"CV file not found at {path}. Please ensure the path is correct.")
        cv_text = input("Please copy-paste your CV text manually or ensure that file is present and accessible: ").strip()
    return cv_text

def save_job_data(data, path: str):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    # Load config paths
    jobs_output = config.JOBS_OUTPUT_PATH
    ai_output = config.AI_OUTPUT_PATH
    cv_path = config.CV_PATH

    # Load CV
    cv_text = load_cv_text(cv_path)

    # Scrape jobs
    jobs = main_scraper.main()
    save_job_data(jobs, jobs_output)
    print(f"\nJob details saved to {jobs_output}")
    print("Job scraping complete.")

    # Ask to proceed
    proceed = input("Run AI evaluation on the scraped jobs? (y/n): ").lower().strip()
    if proceed == "y":
        runner.main(cv_text, jobs_output, ai_output)
    else:
        print("Exiting without AI evaluation.")

if __name__ == "__main__":
    main()

