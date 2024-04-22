from request_urls.invoke_request import himalayas
from bs4 import BeautifulSoup


def parse_data(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    jobs = soup.find_all("article", class_="flex")

    job_data = []

    for job in jobs:
        title = job.find("a", class_="text-xl")
        job_title = title.get_text()
        job_href = f"https://himalayas.app{title.get("href")}"

        company = job.find("a", class_="inline-flex")
        company_title = company.get_text()
        company_href = f"https://himalayas.app{company.get("href")}"
        
        job_data.append({"job_title": job_title, "job_href": job_href, "company_title": company_title, "company_href": company_href})

    print(job_data)
    return job_data

himalayas_jobs = parse_data(himalayas)
