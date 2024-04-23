import himalayas
from request_urls.request_url import request_url, url

# try:
#     himalayas = request_url(url["himalayas"])
#     # roberthalf = request_url(url["roberthalf"])
#     print("Requested URL successful")
# except Exception as e:
#     print("A request error occurred:", e)


# NOTE: scrap mulitple pages
himalayas, roberthalf = ["" for i in range(2)]

for i in range(1, 3):
    url_path = f"{url["himalayas"]}?page={i}"
    himalayas += request_url(url_path)
