# Orchestrator

# Helloworld job scraper
import requests
from bs4 import BeautifulSoup
import random
import pandas as pd

# Get user input for job search keyword
keyword = input("Enter keyword to search for jobs: ").strip()

# Search parameters
scope = "full"
page_number = 30  # Use integer for page number

base_url = "https://helloworld.rs/oglasi-za-posao?"

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


# Request
response = requests.get(paginated_url)
if response.status_code == 200:
    print("Successfully fetched the page.")
    
response = requests.get(job_url)
if response.status_code == 200:
    print("Successfully fetched the job details page.")