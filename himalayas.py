from invoke_request import himalayas
from bs4 import BeautifulSoup


def parse_data(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    jobs = soup.find_all("article", class_="flex")

    job_data = []

    for job in jobs:
        title = job.find("a", class_="text-xl")
        title_text = title.get_text()
        title_href = f"https://himalayas.app{title.get("href")}"

        company = job.find("a", class_="inline-flex")
        company_text = company.get_text()
        company_href = f"https://himalayas.app{company.get("href")}"
        
        job_data.append({"title_text": title_text, "title_href": title_href, "company_text": company_text, "company_href": company_href})

    return job_data

print(parse_data(himalayas))
