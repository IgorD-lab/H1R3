from .wrapper import DoomModel
from .daemon import DoomDaemon


def main():
    daemon = DoomDaemon() 
    daemon.start()
    try:
        doom_ai = DoomModel("llama3:instruct")

        cv_text = "I am a Python developer"
        job_text = "We need someone experienced with Django, PostgreSQL, and REST..."

        prompt = f"""
            Compare the following CV and job description. Return only JSON:
            {{
                "match_score": "X.X/10",
                "missing_keywords": [list],
                "recommendations": [list]
            }}

            CV:
            {cv_text}

            Job:
            {job_text}
            """
        output = doom_ai.ask(prompt)
        print("AI Output:", repr(output))

    finally:
        daemon.stop()


    # with open("./job_scraper/models/jobs_output.json") as f:
    #     print(f.read())

    # llama3:instruct - 86% VRAM
    # deepseek-coder:33b - 90% VRAM, slow response
    # deepseek-coder:6.7b-base-q6_K - testing
  
if __name__ == "__main__":
    main()