# Data Analytics Fundamentals — Task 1

**YuvaIntern | Data Analyst Internship**  
**Author:** Aditya Kumar

---

## 1. Project Overview

This project demonstrates foundational data analytics skills using Python, Pandas, NumPy, Matplotlib, descriptive statistics, and basic data quality checks.

The objective is to demonstrate a complete introductory data analytics workflow, starting with dataset inspection and validation and progressing to statistical analysis, visualization, interpretation, and automated testing.

The project uses a small synthetic dataset containing study hours and student scores. It examines the structure and quality of the data, calculates descriptive statistics, and visualizes the relationship between study hours and scores.

**Important data note:** The dataset is synthetic and was created exclusively for educational and demonstration purposes. It does not represent actual students or a real-world population. The findings must not be interpreted as evidence of real-world relationships or causation.

## 2. Project Objectives

The main objectives of this project are to:

- Understand fundamental Python concepts used in data analysis.
- Work with structured datasets using Pandas.
- Apply NumPy for numerical operations.
- Calculate descriptive statistical measures.
- Perform basic data quality and validation checks.
- Visualize relationships between variables using Matplotlib.
- Interpret analytical results carefully and responsibly.
- Create a reproducible analysis workflow.
- Use automated tests to validate important results.
- Document the project so that another person can reproduce the analysis.

## 3. Tools and Technologies

The following tools and technologies are used in this project:

| Tool or Technology | Purpose |
|---|---|
| Python | Programming and analysis |
| Pandas | Data manipulation and tabular analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| CSV | Dataset storage |
| JSON | Structured output and execution summary |
| Pytest | Automated testing |
| Git and GitHub | Version control and project hosting |

## 4. Project Structure

The repository is organized into the following files and folders:

```text
yuva-intern-task-1-data-analytics/
│
├── report/
│   └── Task_1_Data_Science_Fundamentals_Assessment.docx
│
├── src/
│   └── fundamentals_demo.py
│
├── data/
│   └── illustrative_student_scores.csv
│
├── outputs/
│   ├── descriptive_statistics.csv
│   ├── execution_stdout.json
│   ├── run_summary.json
│   └── study_hours_vs_score.png
│
├── tests/
│   └── test_fundamentals_demo.py
│
├── requirements.txt
├── submission_description.txt
├── .gitignore
└── README.md
```

The project may also contain these files at the repository root, depending on how the files were uploaded to GitHub.

- `fundamentals_demo.py` — Python analysis script.
- `illustrative_student_scores.csv` — synthetic dataset.
- `descriptive_statistics.csv` — generated statistical results.
- `run_summary.json` — structured execution summary.
- `study_hours_vs_score.png` — generated visualization.
- `test_fundamentals_demo.py` — automated tests.

## 5. Dataset Description

The project uses a small synthetic dataset to demonstrate basic data analytics techniques.

The dataset includes information such as:

- **Student ID:** A unique identifier for each synthetic record.
- **Study Hours:** The number of study hours represented in the example dataset.
- **Score:** A numerical score associated with each synthetic record.

The dataset contains 10 records. It is intentionally small so that the analysis can be understood easily and reproduced without requiring a large external dataset.

No real student information is used.

## 6. Analysis Performed

### 6.1 Dataset Inspection

The analysis loads the dataset and examines its structure, columns, data types, and number of records.

Dataset inspection is an important first step because it helps an analyst understand the available information before performing calculations or drawing conclusions.

### 6.2 Data Quality Checks

The workflow checks for common data quality issues, including:

- Missing values.
- Duplicate rows.
- Validity of numerical values.
- Consistency of identifiers and expected data ranges.

These checks help establish whether the dataset is suitable for the planned demonstration analysis.

For the included synthetic dataset, the recorded results show no missing values and no duplicate rows.

### 6.3 Descriptive Statistics

The project calculates descriptive statistical measures to summarize the score data and examine the relationship between study hours and scores.

The measures include:

- **Mean:** The arithmetic average of the values.
- **Median:** The middle value when observations are ordered.
- **Mode:** The most frequently occurring value or values.
- **Standard deviation:** A measure of the spread of values around their mean.
- **Pearson correlation:** A measure of the strength and direction of a linear relationship between two numerical variables.

These statistics provide a concise summary of the synthetic dataset.

### 6.4 Data Visualization

A scatter plot is generated to visualize study hours against scores.

Scatter plots are useful for exploring potential relationships between numerical variables. In this project, the chart illustrates the pattern present in the synthetic observations.

The visualization is saved as:

`study_hours_vs_score.png`

### 6.5 Reproducibility and Automated Testing

The Python script generates analysis outputs, and the automated tests check important properties of the dataset and statistical results.

This makes it easier to rerun the project and verify that the results are consistent with the included data and implementation.

## 7. Key Results

The following results are recorded for the included synthetic dataset:

| Metric | Result |
|---|---:|
| Records analyzed | 10 |
| Missing values | 0 |
| Duplicate rows | 0 |
| Mean score | 69.3 |
| Median score | 68.5 |
| Sample standard deviation | Approximately 13.7 |
| Pearson correlation | Approximately 0.991 |

### Interpretation

The synthetic dataset shows a strong positive linear relationship between study hours and scores. This means that, within these illustrative observations, higher study-hour values are associated with higher score values.

However, the dataset is small and synthetic. The correlation value does not establish causation, and the result should not be generalized to real students or populations.

The analysis is intended to demonstrate statistical techniques rather than produce real-world educational findings.

## 8. Setup and Installation

### Prerequisites

- Python 3.10 or later.
- Git.
- A terminal or command prompt.
- An internet connection to clone the repository and install dependencies.

### Step 1: Clone the Repository

```bash
git clone https://github.com/adityakumar1234yyy-cloud/yuva-intern-task-1-data-analytics.git
```

Move into the project directory:

```bash
cd yuva-intern-task-1-data-analytics
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## 9. Running the Project

Run the analysis script from the directory where the script is located.

If the script is in the repository root:

```bash
python fundamentals_demo.py
```

If the script is inside the `src/` directory:

```bash
python src/fundamentals_demo.py
```

The script generates or updates the analysis outputs according to its implementation.

Review the resulting CSV and JSON files and open the generated PNG image to inspect the analysis results.

**Note:** Use the command that matches the actual location of `fundamentals_demo.py` in your repository.

## 10. Running Automated Tests

Install the project dependencies first, then run:

```bash
pytest -q
```

The tests are intended to validate important dataset properties and statistical results.

A successful test run indicates that the assertions included in the test suite passed for the tested implementation and data. It does not independently prove that every possible error is absent.

## 11. Skills Demonstrated

This project demonstrates the following foundational data analytics skills:

- Python programming fundamentals.
- Working with structured data.
- Data manipulation using Pandas.
- Numerical operations using NumPy.
- Descriptive statistical analysis.
- Data validation and quality checks.
- Data visualization using Matplotlib.
- Basic interpretation of statistical relationships.
- Reproducible analysis workflows.
- Automated testing using Pytest.
- Technical documentation.
- Responsible interpretation of analytical results.

## 12. Limitations

This is an introductory learning project based on a small synthetic dataset. It has several limitations:

1. The dataset contains only 10 records.
2. The observations are illustrative and do not represent a real-world population.
3. The results depend on the values included in the synthetic dataset.
4. A strong correlation does not prove that one variable causes another.
5. The analysis does not account for other factors that might affect real-world scores.
6. The project demonstrates foundational techniques rather than advanced predictive modeling.

For these reasons, the results should not be used to make decisions about actual students or populations.

## 13. Conclusion

This project demonstrates a basic end-to-end data analytics workflow, from dataset inspection and data quality checks to descriptive statistics and visualization.

Using Python and its data analysis libraries, the project shows how structured data can be examined, summarized, and presented in a reproducible format. It also demonstrates the importance of automated testing, clear documentation, and responsible interpretation of results.

The skills developed through this project provide a foundation for future data analytics work involving larger datasets, more advanced statistical methods, and real-world business problems.

## 14. Author

**Aditya Kumar**  
Data Analyst Intern — YuvaIntern

GitHub Repository:  
https://github.com/adityakumar1234yyy-cloud/yuva-intern-task-1-data-analytics

## 15. Disclaimer

This repository was prepared for educational and internship task demonstration purposes. The dataset is synthetic, and the results are illustrative only. All conclusions should be interpreted within the limitations described in this README.
