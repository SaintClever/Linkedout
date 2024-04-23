from request_urls.request_url import request_url, url


# NOTE: scrap mulitple pages
himalayas, roberthalf = ["" for i in range(2)]

try:
  for i in range(1, 3):
      himalayas_path = f"{url["himalayas"]}?page={i}"
      himalayas += request_url(himalayas_path)

      # Additional urls EXAMPLE
      # roberthalf_path = f"{url["roberthalf"]}?page={i}"
      # roberthalf += request_url(roberthalf_path)

  print("Requested URL successful")
except Exception as e:
  print("A request error occurred:", e)
