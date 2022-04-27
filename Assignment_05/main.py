import os
import csv
import requests
from bs4 import BeautifulSoup

# 실행시 콘솔 초기화

os.system('clear')




def make_csv(company):
    file = open(f"{company['name']}.csv", mode="w", encoding="utf-8-sig")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])

    for job in (company["jobs"]):
        writer.writerow(list(job.values()))


url = "http://www.alba.co.kr"
request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")
main = soup.find("div", {"id": "MainSuperBrand"})
brands = main.find_all("li", {"class": "impact"})


# 알바천국에 슈퍼 브랜드로 분류된 브랜드들의 정보를 가져옴
# 개별 브랜드 정보 스크래핑
for brand in brands:
    link = brand.find("a", {"class": "goodsBox-info"})
    name = brand.find("span", {"class": "company"})

    if link and name:
        # a 태그 안의 href 값 가져옴
        link = link["href"]
        name = name.text
        # 브랜드명에 '/' 포함된 경우 '_'로 대체
        name = name.replace('/', '_')
        company = {'name': name, 'jobs': []}

        # 추출한 개별 브랜드 링크로, 브랜드별 공고 추출
        jobs_request = requests.get(link)
        jobs_soup = BeautifulSoup(jobs_request.text, "html.parser")
        tbody = jobs_soup.find("div", {"id": "NormalInfo"}).find("tbody")

        # class 명이 'divide'인 tr태그와 클래스가 없는 tr태그를 모두 가져옴
        job_posting = tbody.find_all("tr", {"class": {"", "divide"}})

        # 각 브랜드 사이트 이동하여 지역, 근무시간, 급여 정보를 가져옴    
        for job in job_posting:

            local = job.find("td", {"class": "local"})
            if local:
                local = local.text.replace(u'\xa0', ' ')
            
            # 공백을 의미하는 유니코드 '\xa0'를 ' '로 대체)
            title = job.find("td", {"class": "title"})
            if title:
                title = title.find("a").find("span", {"class": "company"}).text.strip()
                title = title.replace(u'\xa0', ' ')
            
            time = job.find("td", {"class": "data"})
            if time:
                time = time.text.replace(u'\xa0', ' ')
            
            pay = job.find("td", {"class": "pay"})
            if pay:
                pay = pay.text.replace(u'\xa0', ' ')
            
            date = job.find("td", {"class": "regDate last"})
            if date:
                date = date.text.replace(u'\xa0', ' ')
                
            # 추출된 각 정보를 job 딕셔너리에 추가
            job_dict = {
                        "place": local,
                        "title": title,
                        "time": time,
                        "pay": pay,
                        "date": date
                        }
            # print(job)
                
            # 딕셔너리를 리스트에 저장
            company['jobs'].append(job_dict)
            
            #csv 파일저장
            make_csv(company)
