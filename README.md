# 🐍 RemoteOK Job Scraper

A simple Python web scraper that fetches the first 10 remote job listings from RemoteOK using their public API.

This project demonstrates:
- Sending HTTP requests with `requests`
- Parsing JSON data
- Extracting structured job details
- Saving data to a CSV file using `pandas`

---

## 📌 Features

- Fetches live job data from RemoteOK API
- Extracts:
  - Job Title
  - Company Name
  - Location
- Displays results in the terminal
- Saves results to `remoteok_jobs.csv`

---

## 🛠 Technologies Used

- Python 3
- requests
- pandas

---

## 📦 Installation

### 1. Clone the repository

```
git clone https://github.com/g00562/web-scraper-basics.git
cd loginsystem
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run code

```
python scraper.py
```
