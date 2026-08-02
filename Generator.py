def generate_urls(base_url, start, end):
    for i in range (start, end + 1):
        yield f'{base_url}{i}'
url_generator = generate_urls("/product/", 1, 3)
for url in url_generator:
   print(url)