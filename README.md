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
  - **Change Model:** If you want to switch the model, update the call in [runner.py] where `DoomModel` is instantiated (e.g., `DoomModel("your_model")`).

## Installation

1. **Clone the Repository:**

    ````bash
    git clone https://github.com/IgorD-lab/H1R3.git
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
    - **AI Evaluation Confirmation:** Finally, confirm if you want to run the AI evaluation on the scraped jobs. This step involves sending your CV and job description to the local AI model and can take some time (prepare some netflix shows to watch if you start the process with number of jobs greater then 30 since default llama3:instruct is very slow)

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
└── data/               # Contains local data files (e.g., CV.txt).

```

## How It Works

1. **Load Configuration & CV:**  
   [main.py] loads configuration paths from [config.py] and reads your CV from the specified file (or via prompt if not found).

2. **Job Scraping:**  
   The scraper [job_scraper/main_scraper.py] asks for a job title keyword, scrapes job links from supported sources (currently only Helloworld.rs), and displays the total job count before prompting for confirmation.

3. **AI Evaluation:**  
   After scraping, on confirmation, the program calls the AI evaluator [job_processing/runner.py], which uses [DoomModel] (based on `llama3:instruct`) to assess your job compatibility.

## TODO / Future Improvements

### Core Features

- [x] Scrape jobs from Helloworld.rs
- [ ] Implement all scrapers:
  - [x] Helloworld.rs
  - [ ] Indeed
  - [ ] LinkedIn
- [x] Run local LLM (`llama3:instruct`) via Ollama for AI evaluation
- [ ] 🔲 Support OpenAI GPT API tokens for cloud-based evaluation (⚠️ cost-aware)

---

### Model Configuration & Evaluation Flow

- [x] Allow model name to be changed in `runner.py` (via `DoomModel("model_name")`)
- [ ] Add CLI or config-based model selection
- [ ] Cache LLM evaluations to avoid redundant processing
- [ ] Add multi-threading or batching for faster AI evaluation

---

### Job Selection & Processing

- [ ] Enable selection of specific jobs to process through AI
- [ ] Allow filtering or tagging of job posts before processing
- [ ] Create a local job tracker with status (e.g., Scraped / Evaluated / Applied)

---

### Post-Processing

- [ ] Auto-generate tailored CVs for each evaluated job
- [ ] Output evaluation summary as CSV/Markdown/HTML

---

### UX & Interface

- [x] Prompt user for job keyword
- [x] Confirm job scraping & evaluation steps
- [ ] 🧪 Add `--no-emoji` / `--silent` mode for terminal output
- [ ] 🖥️ Develop a basic GUI (web or desktop)
- [ ] 🐳 Provide Dockerized deployment for easy setup

---

### 🧪 Testing & Maintenance

- [x] Validate file paths and handle missing input files more gracefully
- [ ] Add unit tests for scraper modules
- [ ] Implement mock AI for faster testing without LLM

---

