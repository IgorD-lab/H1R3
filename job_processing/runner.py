from .wrapper import DoomModel
from .daemon import DoomDaemon
import json


def main(cv_text, jobs_json_path, output_path, ai_limit="None"):
    daemon = DoomDaemon()
    daemon.start()
    try:
        doom_ai = DoomModel("llama3:instruct")

        with open(jobs_json_path, "r", encoding="utf-8") as f:
            jobs = json.load(f)

        results = []
        for job in jobs[:ai_limit] if ai_limit != "None" else jobs:
            job_title = job["title"]
            job_text = job["description"]
            job_tags = job["tags"]
            job_seniority = job["seniority"]
            prompt = f"""
                    You are an ATS match evaluator. Your goal is to rate the compatibility of a CV with a job posting using a concise, structured format.

                    ### INSTRUCTIONS:
                    - Output only a valid JSON object. Each field must be short and clear. Do not include any extra text.
                    - `match_score` is a float from 0 to 10, rated based on skill match, seniority, and relevance
                    - Use short keyword-style entries in `missing_keywords` and `recommendations`
                    - Keep all responses compact; no full paragraphs or narrative

                    ### FORMAT:
                    ```json
                {{
                    "match_score": 7.3,
                    "missing_keywords": ["Kafka", "Kubernetes", "TLS", "PostgreSQL"],
                    "recommendations": ["Add Kafka project", "Mention experience with distributed systems", "Specify Linux admin knowledge"],
                    "explanation": "Strong Python match, lacks direct experience in listed data tools and cloud infra."
                }}

                CV:
                {cv_text}

                Job:
                {job_title, job_text, job_tags, job_seniority}
                """
                
            print(f"Consulting AI about: {job_title}")
            output = doom_ai.ask(prompt)
            results.append({
                "job_url": job["url"],
                "title": job["title"],
                "ai_output": output
            })

        with open(output_path, "w", encoding="utf-8") as out_f:
            json.dump(results, out_f, indent=2)

        print(f"Results written to {output_path}")

    finally:
        daemon.stop()


if __name__ == "__main__":
    cv_text = "I am a Python developer i can use C, C++, python i do data science i have 0 years of experience"
    jobs_json_path = "./job_scraper/models/jobs_output.json"
    output_path = "./job_processing/match_results.json"
    main(cv_text, jobs_json_path, output_path)
    
    