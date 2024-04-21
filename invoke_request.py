from request_page import urls, request_page

try:
    himalayas = request_page(urls["himalayas"])
    # smartrecruiters = request_page(urls["smartrecruiters"])
    # roberthalf = request_page(urls["roberthalf"])
except Exception as e:
    print("A request error occurred:", e)
