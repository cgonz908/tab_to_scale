import requests
#import urllib.request

#Takes url as a string, returns html as a string
def pull_url(url):

    response = requests.get(url)
    #urllib.request.urlopen(url)
    html = response.text

    html = html.replace('\n', '')

    return html