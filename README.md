# Sensor Analyzer

A Python command-line tool for analyzing temperature and humidity sensor data.  
The project uses **Poetry** for dependency management, versioning, and packaging.  
It demonstrates a fully reproducible Python build pipeline.

---

## 📦 Features

- Load sensor data from CSV files (`pandas`)
- Compute min, max, and mean values
- Detect temperature anomalies outside a configurable range
- Command-line interface built with `click`
- Reproducible installation and execution using Poetry

---

## 🗂 Project Structure

```
sensor-analyzer/
├─ sensor_analyzer/
│  ├─ __init__.py
│  ├─ analyzer.py
│  └─ cli.py
├─ data/
│  └─ sample_sensors.csv
├─ pyproject.toml
├─ poetry.lock
└─ dist/                (generated after building)
```

---

## ⚙️ Installation (Reproducible Build)

Clone the repository:

```bash
git clone https://github.com/Hasna878/sensor-analyzer.git
cd sensor-analyzer
```

Install dependencies:

```bash
poetry install
```

---

## ▶️ Running the CLI

Run the tool through Poetry:

```bash
poetry run python -m sensor_analyzer.cli data/sample_sensors.csv
```

---

## ⚙️ Optional CLI Parameters

Custom temperature range:

```bash
poetry run python -m sensor_analyzer.cli data/sample_sensors.csv --temp-min 18 --temp-max 26
```

Disable anomaly listing:

```bash
poetry run python -m sensor_analyzer.cli data/sample_sensors.csv --no-anomalies
```

Show help:

```bash
poetry run python -m sensor_analyzer.cli --help
```

---

## 🔢 Version Management

Check version:

```bash
poetry version
```

Increase version:

```bash
poetry version patch
```

---

## 📦 Packaging

Build the project:

```bash
poetry build
```

Generated artifacts (in `dist/`):

```
sensor-analyzer-<version>.tar.gz
sensor_analyzer-<version>-py3-none-any.whl
```

Install the built wheel:

```bash
pip install dist/sensor_analyzer-*-py3-none-any.whl
```
