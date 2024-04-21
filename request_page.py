import json
import requests


# f"https://himalayas.app/jobs/countries/{location}/{job_title}"
# f"https://jobs.smartrecruiters.com/?keyword={job_title}{location}"
# f"https://www.roberthalf.com/us/en/jobs/{location}/{job_title}"


with open("urls.json", "r") as f:
    urls = json.load(f)


def request_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    raise Exception("Failed to fetch web page. Status code:", response.status_code)
