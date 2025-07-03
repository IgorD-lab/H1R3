# Orchestrator

# Helloworld job scraper
import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import time


header = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Get user input for job search keyword
keyword = input("Enter keyword to search for jobs: ").strip()

# Search parameters
scope = "full"
page_number = 0  # Use integer for page number

base_url = "https://helloworld.rs/oglasi-za-posao/programiranje?"

# Build search parameters string
if keyword:
    search_parameters = f"q={keyword}&scope={scope}"
else:
    search_parameters = ""

# Construct search URL
if keyword:
    search_url = f"{base_url}{search_parameters}"
else:
    search_url = base_url

# Construct paginated URL
if keyword:
    paginated_url = (
        f"{base_url}page={page_number}&{search_parameters}&disable_saved_search=1"
    )
else:
    paginated_url = f"{base_url}page={page_number}&disable_saved_search=1"

print("Search URL:", search_url)
print("Paginated URL:", paginated_url)

# Example job ID and job URL
job_id = "669397"
job_url = f"https://helloworld.rs/posao/a/a/{job_id}?disable_saved_search=1"

print("Job URL:", job_url)



# GET LINKS ======================


# print(soup.prettify())

total_jobs = 0
job_links = []

while True:

        if keyword:
            paginated_url = (
                f"{base_url}page={page_number}&{search_parameters}&disable_saved_search=1"
            )
        else:
            paginated_url = f"{base_url}page={page_number}&disable_saved_search=1"

        job_count = 0
        time.sleep(random.uniform(1, 3))
        response = requests.get(paginated_url, headers=headers)
        print("Response status code:", response.status_code)
        if response.status_code == 200:
            all_job_html = response.text
            soup = BeautifulSoup(all_job_html, 'html.parser')

            job_elements = soup.find_all(attrs={"data-job-id": True})
            for elem in job_elements:
                job_id = elem["data-job-id"]
                print("Found job ID:", job_id)
                # Build Job URL
                job_url = f"https://helloworld.rs/posao/a/a/{job_id}?disable_saved_search=1"
                
                if job_url not in job_links:
                    job_links.append(job_url)
                    job_count += 1
                    total_jobs += 1
                    print("Job URL:", job_url)
            if job_count == 0:
                print("No more jobs found. Exiting loop.")
                break
        else:
            print("Failed to fetch the job listings page.")
            
        page_number += 30


with open("job_postings.txt", "w") as file:
    file.write("Paginated URL: " + paginated_url + "\n")
    file.write("Total Jobs: " + str(total_jobs) + "\n")
    for link in job_links:
        file.write(link + "\n")

        