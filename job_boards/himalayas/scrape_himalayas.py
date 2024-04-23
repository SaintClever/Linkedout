from request_urls.invoke_request import himalayas
from bs4 import BeautifulSoup


def parse_data(html_content):
    # NOTE: only scrape jobs with salaries and country codes
    soup = BeautifulSoup(html_content, "html.parser")
    jobs = soup.find_all("article", class_="flex")

    job_data = []

    for job in jobs:
        country_code = job.find("img", class_="mr-1.5")
        salary = job.find("p", class_="inline-flex")

        if (country_code != None
        and salary != None
        and "salary:" in salary.get_text().casefold()):

            company_name = job.find("a", class_="inline-flex").get_text()

            title = job.find("a", class_="text-xl")
            job_title = title.get_text()
            job_href = f"https://himalayas.app{title.get("href")}"

            location = country_code.get("title").upper()

            salary = job.find("p", class_="inline-flex")
            salary_text = salary.get_text()

            currency = salary_text[salary_text.rfind(" ") + 1:]

            starting_salary = int(salary_text[
                salary_text.find(':') + 2:
                salary_text.find('k-')
            ] + "000")

            max_salary = int(salary_text[
                salary_text.find('k-') + 2:
                salary_text.find('k ')
            ] + "000")

            job_data.append({
                "company_name": company_name,
                "job_title": job_title,
                "job_href": job_href,
                "location": location,
                "currency": currency,
                "starting_salary": starting_salary,
                "max_salary": max_salary
            })

    return job_data

himalayas_jobs = parse_data(himalayas)
