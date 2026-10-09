"""
Task 1 — Data Science Fundamentals Assessment
A small, reproducible demonstration of Python, statistics, data handling, and visualization.

The data below are illustrative synthetic records created for learning. They are not real
people, research participants, or evidence about any actual population.
"""
from pathlib import Path
import csv
import json
import statistics
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "outputs"
DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# Synthetic example data: score values are only for demonstrating techniques.
records = [
    {"student_id": "S001", "study_hours": 2.0, "score": 58, "attendance_pct": 80},
    {"student_id": "S002", "study_hours": 3.5, "score": 67, "attendance_pct": 88},
    {"student_id": "S003", "study_hours": 1.0, "score": 49, "attendance_pct": 72},
    {"student_id": "S004", "study_hours": 5.0, "score": 84, "attendance_pct": 95},
    {"student_id": "S005", "study_hours": 4.0, "score": 76, "attendance_pct": 90},
    {"student_id": "S006", "study_hours": 2.5, "score": 63, "attendance_pct": 84},
    {"student_id": "S007", "study_hours": 6.0, "score": 91, "attendance_pct": 98},
    {"student_id": "S008", "study_hours": 3.0, "score": 70, "attendance_pct": 86},
    {"student_id": "S009", "study_hours": 4.5, "score": 81, "attendance_pct": 93},
    {"student_id": "S010", "study_hours": 1.5, "score": 54, "attendance_pct": 76},
]

def main():
    df = pd.DataFrame(records)
    csv_path = DATA_DIR / "illustrative_student_scores.csv"
    df.to_csv(csv_path, index=False)

    # Core data-quality checks.
    missing_counts = df.isna().sum()
    duplicate_rows = int(df.duplicated().sum())
    assert df["student_id"].is_unique, "Student IDs should be unique in this example."
    assert df["score"].between(0, 100).all(), "Scores must be between 0 and 100."
    assert df["attendance_pct"].between(0, 100).all(), "Attendance must be between 0 and 100."

    # Descriptive statistics. These summarize this synthetic sample only.
    summary = df[["study_hours", "score", "attendance_pct"]].describe()
    mean_score = float(df["score"].mean())
    median_score = float(df["score"].median())
    mode_scores = df["score"].mode().tolist()
    sample_std = float(df["score"].std(ddof=1))
    score_study_correlation = float(df["study_hours"].corr(df["score"]))

    # Save a machine-readable summary.
    summary_path = OUTPUT_DIR / "descriptive_statistics.csv"
    summary.to_csv(summary_path)

    # Chart: scatter plot is descriptive; association does not prove causation.
    fig, ax = plt.subplots(figsize=(7.5, 5))
    ax.scatter(df["study_hours"], df["score"])
    ax.set_title("Illustrative Study Hours and Scores")
    ax.set_xlabel("Study hours (synthetic example)")
    ax.set_ylabel("Score (0–100)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    chart_path = OUTPUT_DIR / "study_hours_vs_score.png"
    fig.savefig(chart_path, dpi=160)
    plt.close(fig)

    result = {
        "records": len(df),
        "missing_values_by_column": {k: int(v) for k, v in missing_counts.items()},
        "duplicate_rows": duplicate_rows,
        "mean_score": round(mean_score, 2),
        "median_score": round(median_score, 2),
        "mode_scores": mode_scores,
        "sample_standard_deviation_score": round(sample_std, 2),
        "study_hours_score_pearson_correlation": round(score_study_correlation, 3),
        "interpretation_note": (
            "Synthetic demonstration only. Correlation describes association and does not "
            "establish that study hours cause higher scores."
        ),
        "generated_files": [
            str(csv_path.relative_to(ROOT)),
            str(summary_path.relative_to(ROOT)),
            str(chart_path.relative_to(ROOT)),
        ],
    }
    result_path = OUTPUT_DIR / "run_summary.json"
    result_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
