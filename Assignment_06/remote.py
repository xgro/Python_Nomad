import requests
from bs4 import BeautifulSoup

def extract_job(result):
  company = result.find("h3", {"itemprop": "name"}).get_text(strip=True)
  title = result.find("h2", {"itemprop":"title"}).get_text(strip=True)
  location = result.find("div", {"class":"tooltip"})
  if location is None:
    location = "Remote"
  else:
    location = location.get_text(strip=True)
    if "$" in location:
      location = "Remote"
  data_id = result["data-id"]
  apply_link = f"https://remoteok.com/remote-jobs/{data_id}"
  return {"title":title, "company":company, "location":location, "apply_link":apply_link}

def extract_jobs(url):
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
  result = requests.get(url, headers=headers)
  # result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("tr", {"class":"job"})
  jobs = []
  print("Scrapping Remote OK jobs...")
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs

def get_jobs(word):
  url = f"https://remoteok.com/remote-{word}-jobs"
  jobs = extract_jobs(url)
  return jobs