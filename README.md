# H1R3

This project is a job scraper and AI evaluation tool written in Python. It scrapes job postings from various sources and uses a local large language model (LLM) for AI evaluation of how well your CV matches the job description.

## Requirements

- **Python:** Python 3.8+ is recommended.
- **Virtual Environment (optional):** It is advised to use a virtual environment.
- **Dependencies:** Install them using `requirements.txt`.
- **Ollama & LLM Model:**  
  - Download and install [Ollama](https://ollama.ai).
  - Pull the `llama3:instruct` model using Ollama.  
  - **System Requirements:** Ensure your system meets the hardware/software demands for running the local LLM.  
  - **Change Model:** If you want to switch the model, update the call in [runner.py](c:\Users\PC\Desktop\H1R3\job_processing\runner.py) where `DoomModel` is instantiated (e.g., `DoomModel("your_model")`).

## Installation

1. **Clone the Repository:**

    ````bash
    git clone <repository-url>
    cd H1R3
    ````

2. **Set Up Virtual Environment (Optional):**

    ````bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ````

3. **Install Dependencies:**

    ````bash
    pip install -r requirements.txt
    ````

## Running the Program

1. **Run the Main Script:**

    The program is initiated with [main.py](c:\Users\PC\Desktop\H1R3\main.py):

    ````bash
    python main.py
    ````

2. **User Inputs:**

    - **Job Title Keyword:** When prompted, input the job title keyword that you are looking for.
    - **Job Scraping Confirmation:** After displaying the number of scraped jobs (which could be high), you'll be asked if you want to proceed. This gives you an option to cancel if the number is too large.
    - **AI Evaluation Confirmation:** Finally, confirm if you want to run the AI evaluation on the scraped jobs. This step involves sending your CV and job description to the local AI model and can take some time.

## File Structure

```
H1R3/
│
├── main.py             # Main entry point of the application.
├── config.py           # Configuration file with paths to CV and job data.
├── requirements.txt    # Python dependencies.
├── job_processing/     # Contains files for job processing and AI evaluation.
│   ├── runner.py       # Orchestrates the AI evaluation.
│   ├── wrapper.py      # Contains the DoomModel for interacting with Ollama.
│   └── daemon.py       # Manages the lifecycle of the Ollama daemon.
│
├── job_scraper/        # Contains scraping utilities and modules.
│   ├── main_scraper.py # Main entry point for job scraping (asks for keyword).
│   ├── scrapers/       # Scraper implementations.
│   │   ├── helloworld.py  # Helloworld.rs scraper (currently supported).
│   │   └── base.py     # Base class for all scrapers.
│   ├── utils/          # Helper modules (HTTP client, parser, anti-detection).
│   └── config/         # Site-specific configuration files (YAML).
│
├── data/               # Contains local data files (e.g., CV.txt).
└── notes/              # Developer notes and ideas.
```

## How It Works

1. **Load Configuration & CV:**  
   [main.py](c:\Users\PC\Desktop\H1R3\main.py) loads configuration paths from [config.py](c:\Users\PC\Desktop\H1R3\config.py) and reads your CV from the specified file (or via prompt if not found).

2. **Job Scraping:**  
   The scraper ([job_scraper/main_scraper.py](c:\Users\PC\Desktop\H1R3\job_scraper\main_scraper.py)) asks for a job title keyword, scrapes job links from supported sources (currently only Helloworld.rs), and displays the total job count before prompting for confirmation.

3. **AI Evaluation:**  
   After scraping, on confirmation, the program calls the AI evaluator ([job_processing/runner.py](c:\Users\PC\Desktop\H1R3\job_processing\runner.py)), which uses [DoomModel](c:\Users\PC\Desktop\H1R3\job_processing\wrapper.py) (based on `llama3:instruct`) to assess your job compatibility.

## TODO / Future Improvements

- **Extend Scrapers:** Implement scrapers for LinkedIn and Indeed.
- **Model Flexibility:**  
  - Provide an option to modify the local LLM model.
  - Support GPT API tokens for faster responses (with potential cost concerns).
- **Selective Processing:**  
  - Allow processing of specific jobs through the AI.
  - Enable selection of which scraped jobs to process.
- **Post-AI Processing:** Automatically output a tailored CV for the selected jobs.
- **Additional Filtering:** More filtering options & a tracker to store job postings and corresponding CV submissions.
- **UI Development:** Consider building a web or desktop interface (possibly via Docker) – volunteer help for GUI development is welcome!

## License

This project is under the [MIT License](LICENSE) (if applicable).

---

Happy coding!