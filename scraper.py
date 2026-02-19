import requests
import pandas as pd

url = "https://remoteok.com/api"

response = requests.get(url)

data = response.json()

jobs_raw = data[1:11]

jobs = []

for job in jobs_raw:
    title = job.get("position", "N/A")
    company = job.get("company", "N/A")
    location = job.get("location", "Worldwide")

    jobs.append([title, company, location])


df = pd.DataFrame(jobs, columns=["Job Title", "Company", "Location"])
df.to_csv("remoteok_jobs.csv", index=False)

print(df)

print("\nData saved to remoteok_jobs.csv")