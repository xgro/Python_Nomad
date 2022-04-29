import requests
from bs4 import BeautifulSoup

def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class": "s-pagination"})
  if pages is None:
    last_page = 1
  else:
    pages = pages.find_all("a")
    last_page = pages[-2].get_text(strip=True)
  return int(last_page)

def extract_job(html):
  title = html.find("a", {"class": "s-link"}).get("title")
  company, location = html.find("h3", {"class": "fc-black-700"}).find_all("span", recursive=False)
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)
  job_id = html["data-jobid"]
  apply_link = f"https://stackoverflow.com/jobs/{job_id}"
  return {"title":title, "company":company, "location":location, "apply_link":apply_link}

def extract_jobs(last_page, url):
  print("Scrapping StackOverflow jobs...")

  jobs = []
  for page in range(last_page):
    result = requests.get(f"{url}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs(word):
  url = f"https://stackoverflow.com/jobs?q={word}&sort=p"
  last_page = get_last_page(url)
  jobs = extract_jobs(last_page, url)
  return jobs