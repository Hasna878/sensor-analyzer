import pandas as pd


def load_data(csv_path: str) -> pd.DataFrame:
    """
    Load sensor data from a CSV file.

    Expected columns:
        - temperature
        - humidity

    Extra columns are ignored but kept.
    """
    df = pd.read_csv(csv_path)
    if "temperature" not in df.columns or "humidity" not in df.columns:
        raise ValueError("CSV must contain 'temperature' and 'humidity' columns.")
    return df


def compute_stats(df: pd.DataFrame) -> dict:
    """
    Compute basic statistics for temperature and humidity,
    and convert NumPy types to Python native types for JSON compatibility.
    """
    stats = {
        "temperature": {
            "min": float(df["temperature"].min()),
            "max": float(df["temperature"].max()),
            "mean": float(df["temperature"].mean()),
        },
        "humidity": {
            "min": float(df["humidity"].min()),
            "max": float(df["humidity"].max()),
            "mean": float(df["humidity"].mean()),
        },
    }
    return stats


def detect_anomalies(
    df: pd.DataFrame,
    temp_min: float = 15.0,
    temp_max: float = 30.0,
) -> pd.DataFrame:
    """
    Return rows where the temperature is outside [temp_min, temp_max].
    """
    mask = (df["temperature"] < temp_min) | (df["temperature"] > temp_max)
    return df[mask].copy()
