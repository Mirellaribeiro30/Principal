import re

pattern = re.compile(r'https?://(www\.)?([a-zA-Z0-9]+)\.([a-zA-Z]{2,})')
url = "https://www.google.com"
match = pattern.match(url)
if match:
    print("url verdadeira")
else:
    print("url invalida")
