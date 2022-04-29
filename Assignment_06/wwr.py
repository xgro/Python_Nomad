import requests
from bs4 import BeautifulSoup

def extract_job(result):
  company = result.find("span", {"class":"company"}).get_text(strip=True)
  title = result.find("span", {"class":"title"}).get_text(strip=True)
  location = result.find("span", {"class":"region"})
  if location is None:
    location = " "
  else:
    location = location.get_text(strip=True)
  link = result.find("a", recursive=False)["href"]
  apply_link = f"https://weworkremotely.com{link}"
  return {"title":title, "company":company, "location":location, "apply_link":apply_link}

def extract_jobs(url):
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
  result = requests.get(url, headers=headers)
  # result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  sections = soup.find_all("section", {"class":"jobs"})
  jobs = []
  results = []
  print("Scrapping WWR jobs...")
  for section in sections:
    lists = section.find("ul").find_all("li", {"class": ["", "feature"]})
    results.extend(lists)
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs

def get_jobs(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  jobs = extract_jobs(url)
  return jobs