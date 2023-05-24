import requests
from bs4 import BeautifulSoup


# Check user's website for dead links
class findDeadLinks:
    def __init__(self, url):
        self.url = url

    def dead_links(self):
        from urllib.parse import urljoin

        # get the HTML content of the web page
        response = requests.get(self.url)
        html = response.content

        # parse the HTML using BeautifulSoup and extract all the links on the page
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all("a")

        dead_links = []
        # check each link for a valid response
        for link in links:
            href = link.get("href")
            if href and href != '#' and href != '' and href != 'javascript:void(0);':
                if not href.startswith("http"):  # if the url not includes the http protocol it is a relative link
                    href = urljoin(self.url, href)  # so you have to transform it to absolute link

                response = requests.head(href)
                if response.status_code >= 400:  # if the link has status code greater than 400
                    dead_links.append('Broken link:' + href)  # notify the user that there is a dead link

        return dead_links
