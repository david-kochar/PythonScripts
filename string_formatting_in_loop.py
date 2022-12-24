urls = [
        "https://access.blueberry.org/api/v1/Organizations/Profile/{page_num_param}",
        "https://access.blueberry.org/api/v1/Organizations/Profile/{org_param}/{page_num_param}",
        # "https://access.blueberry.org/api/v1/Organizations/{org_param}/Relationships/{page_num_param}",
        # "https://access.blueberry.org/api/v1/Organizations/{org_param}/Subscriptions/{page_num_param}"
        ]

def print_url(urls, **kwargs):
    for url in urls:
        if kwargs:
            org = kwargs["org"]
            page_num = 1
            request_url = url.format(org_param = org, page_num_param = page_num)
        else:
            page_num = 1
            request_url = url.format(page_num_param = page_num)
        print(request_url)

print_url(urls, org = "abc")

changed_since = "175301010000"

yyyymmdd = changed_since[0:8]
    
hhmm = changed_since[-4:]

page_num = 1
    
url = f"https://access.blueberry.org/api/v1/Organizations/ChangedSince/{yyyymmdd}/{hhmm}/"

print(url)

url = "{url}/{page_num_param}"

url.format(page_num_param = page_num)

print(url)

