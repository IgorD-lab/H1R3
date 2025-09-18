
# H1R3

**Status:** Functional – in active development  
**Goal:** Automate the job search process by scraping listings, matching them against your CV, and providing AI-powered recommendations.  

---

## Overview
H1R3 is a Python-based tool that helps developers streamline their job hunt.  
- Upload your CV  
- Enter the job title you’re looking for  
- The app scrapes job postings from supported boards  
- A local LLM (via Ollama) evaluates how well your CV matches each posting  
- Results highlight best matches and provide keyword suggestions to optimize your CV  

---

## Current Capabilities
- ✅ CV input and parsing from text file  
- ✅ Job scraping from **Helloworld.rs** (more sites planned)  
- ✅ Local AI evaluation using **Llama3 via Ollama**  
- ✅ Command-line interface for entering keywords and reviewing matches  
- ✅ Configurable model selection in `runner.py`  

---

## In Progress
- Expanding scrapers (Indeed, LinkedIn, others)  
- Performance optimizations for LLM evaluation (batching, caching, multithreading)  
- Flexible model selection via CLI/config file  
- Improved error handling and path validation  

---

## Planned Enhancements
- Support for OpenAI GPT API (cloud-based evaluation)  
- Local job tracker (Scraped / Evaluated / Applied)  
- Export results to CSV, Markdown, or HTML  
- Automatic CV tailoring per job description  
- GUI interface (web/desktop)  
- Dockerized deployment for easy setup  
- Unit tests and mock AI for faster development  

---

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/IgorD-lab/H1R3.git
cd H1R3
````

### 2. Set Up Virtual Environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama & Model

* Download and install [Ollama](https://ollama.ai)
* Pull the model:

```bash
ollama pull llama3:instruct
```

---

## Usage

Run the main script:

```bash
python main.py
```

Follow the prompts:

1. **Enter job title keyword** (e.g. "Python developer")
2. **Confirm scraping** once job count is shown
3. **Confirm AI evaluation** to run compatibility analysis with your CV

---

## File Structure

```
H1R3/
├── main.py             # Application entry point
├── config.py           # Configuration (CV path, job data path)
├── requirements.txt    # Dependencies
│
├── job_processing/     # AI evaluation pipeline
│   ├── runner.py       # Orchestrates AI evaluation
│   ├── wrapper.py      # DoomModel (Ollama interface)
│   └── daemon.py       # Ollama lifecycle management
│
├── job_scraper/        # Scraping utilities
│   ├── main_scraper.py # Runs scraping workflow
│   ├── scrapers/       # Individual scrapers (Helloworld.rs supported)
│   ├── utils/          # HTTP client, parser, helpers
│   └── config/         # Site configs (YAML)
│
└── data/               # CV and job data
```

---

## Limitations

* Currently only scrapes **Helloworld.rs**
* Performance limited by local LLM evaluation speed (Llama3 requires significant VRAM)
* No GUI yet — CLI-based interface only

---

### 🛠️ Contributing

H1R3 is still in early development, and contributions are welcome!
If you’d like to help, here are some areas that need attention:

* **Scrapers**: Add support for more job boards (Indeed, LinkedIn, Glassdoor, etc.)
* **Evaluation Engine**:

  * Batch processing and caching to reduce LLM evaluation time
  * Configurable scoring metrics (semantic similarity, keyword overlap, etc.)
* **Data Handling**:

  * Standardize scraped job data format
  * Add persistence layer (SQLite or PostgreSQL)
* **User Interface**:

  * Export results to CSV/Markdown/HTML
  * Basic web or desktop GUI
* **Deployment**:

  * Docker setup for easier environment replication
  * Optional OpenAI GPT integration for cloud evaluation
* **Testing**:

  * Unit tests for scrapers
  * Mock AI interface for faster dev cycles

---

### 📌 Roadmap

* **MVP (current)** – CV parsing, job scraping (Helloworld.rs), AI-based matching
* **Next** – Expand scrapers, optimize evaluation, basic exports
* **Later** – GUI, cloud deployment, job tracker, CV auto-tailoring

