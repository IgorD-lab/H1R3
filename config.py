import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
JOBS_JSON_PATH = os.path.join(DATA_DIR, "jobs_output.json")
CV_PATH = os.path.join(DATA_DIR, "cv.txt")

print (DATA_DIR)