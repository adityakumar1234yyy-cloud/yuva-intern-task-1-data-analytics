"""Basic smoke tests for the fundamentals demonstration."""
import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "src" / "fundamentals_demo.py"
spec = importlib.util.spec_from_file_location("fundamentals_demo", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def test_example_records_are_valid():
    import pandas as pd
    df = pd.DataFrame(module.records)
    assert len(df) == 10
    assert df["student_id"].is_unique
    assert df["score"].between(0, 100).all()
    assert df["attendance_pct"].between(0, 100).all()

def test_score_summary_is_computable():
    import pandas as pd
    df = pd.DataFrame(module.records)
    assert round(float(df["score"].mean()), 2) == 69.3
    assert round(float(df["score"].median()), 2) == 68.5
