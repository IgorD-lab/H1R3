H1R3/
│
├── main.py
│
├── job_scraper/
│   ├── main_scraper.py
│   ├── scrapers/
│   │   ├── helloworld.py
│   │   └── base.py
│   │   └── ... (other site scrapers)
│   ├── utils/
│   │   └── ... (helper modules)
│   ├── config/
│   │   └── ... (site configs)
│   └── models/
│       └── jobs_output.json
│
├── job_processing/
│   ├── runner.py
│   ├── wrapper.py
│   ├── daemon.py
│   └── ... (other processing modules)
│
└── README.md (optional)