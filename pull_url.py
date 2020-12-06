import urllib.request

url = "https://tabs.ultimate-guitar.com/tab/stevie-ray-vaughan-double-trouble/pride-and-joy-tabs-30829"

response = urllib.request.urlopen(url)
web_content = response.read()

f = open("webpage.txt", "wb")
f.write(web_content)
f.close()
