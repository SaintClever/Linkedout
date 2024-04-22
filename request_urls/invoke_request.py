from request_urls.request_url import request_url, url

try:
    himalayas = request_url(url["himalayas"])
    # smartrecruiters = request_url(url["smartrecruiters"])
    # roberthalf = request_url(url["roberthalf"])
    print("Requested URL successful")
except Exception as e:
    print("A request error occurred:", e)
