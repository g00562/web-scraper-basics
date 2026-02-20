from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import csv
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://remoteok.com/remote-dev-jobs")


time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

jobs = soup.find_all("tr", class_="job")[:10]

job_list = []

for job in jobs:
  
    title_tag = job.find("h2", {"itemprop": "title"})
    title = title_tag.get_text(strip=True) if title_tag else "N/A"

    
    company_tag = job.find("h3", {"itemprop": "name"})
    company = company_tag.get_text(strip=True) if company_tag else "N/A"

    location_tag = job.find("div", class_="location")
    location = location_tag.get_text(strip=True) if location_tag else "Remote"

    job_list.append([title, company, location])

for job in job_list:
    print(job)

with open("remote_jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Company", "Location"])
    writer.writerows(job_list)

print("Saved to remote_jobs.csv")
