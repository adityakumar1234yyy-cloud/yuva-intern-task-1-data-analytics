# Data Analytics Fundamentals — Task 1

**YuvaIntern | Data Analyst Internship**  
**Author:** Aditya Kumar

## Overview
This project demonstrates introductory data analytics workflows with Python, Pandas, and basic statistical methods. It creates and analyses a small synthetic dataset, checks data quality, calculates descriptive statistics, and produces a visualization comparing study hours and scores.

> **Data note:** The dataset is synthetic and intended for learning only. It does not describe real students or a real-world population. Correlation is descriptive and does not establish causation.

## Project structure
- `report/` — Task 1 assessment report
- `src/` — Python analysis script
- `data/` — illustrative synthetic dataset
- `outputs/` — generated summary statistics, run summary, and chart
- `tests/` — automated tests
- `requirements.txt` — Python dependencies
- `submission_description.txt` — internship submission description

## Setup and run
Use Python 3.10 or later.

```bash
python -m venv .venv
```

Activate the virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python src/fundamentals_demo.py
```

Run tests:

```bash
pytest -q
```

## Skills demonstrated
- Python scripting and data structures
- Tabular data handling with Pandas
- Descriptive statistics
- Data validation and quality checks
- Data visualization
- Reproducible workflows and basic testing

## Limitations
This is a foundational demonstration using a small synthetic dataset. Its results are not real-world findings and should not be used to make decisions about actual students or populations.
