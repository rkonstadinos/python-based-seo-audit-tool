from urllib.parse import urlparse

import requests  # use the requests to make api requests
from bs4 import BeautifulSoup  # use BeautifulSoup library to scrape the websites
import re  # use the re library to use regex


class seoAudit:
    def __init__(self, url, position, amp, target_keyword, moz_api_client, moz_api_key, mobile_api_key, pagespeed_api_key):
        self.url = url
        self.position = position
        self.amp = amp
        self.target_keyword = target_keyword
        self.moz_api_client = moz_api_client
        self.moz_api_key = moz_api_key
        self.mobile_api_key = mobile_api_key
        self.pagespeed_api_key = pagespeed_api_key

    def perform_seo_checks(self):
        seo = {
            'page': self.url,
            'position': self.position,
            'amp': self.amp,
        }

        seo_suggestions = {}

        r = requests.get(self.url)

        # If the line bellow causes an error, run 'pip install html5lib', and import html5lib
        soup = BeautifulSoup(r.content, 'html.parser')

        # Find all the <img> tags from source code, get and store their src and alt attributes to images_alt
        # Example: <img src="jacket.jpg" alt="jacket>
        # If there are missing alt attributes return 0
        images_alt = self.get_image_alt(soup.find_all('img'))
        seo['images_alt'] = images_alt[0]
        if images_alt[1]:
            seo_suggestions['images_alt'] = {
                'comments': 'The images on the WebPage are missing alternative tags. It is recommended to add alternative tags to all images for better accessibility and SEO optimization.',
                'data': images_alt[1]}

        # Find all the <a> tags from source code, get and store their href and title attributes to links_title
        # Example: <a href="product/jacket" title="jacket>
        # If there are missing title attributes return 0
        links_title = self.get_links_title(soup.find_all('a'))
        seo['links_title'] = links_title[0]
        if links_title[1]:
            seo_suggestions['links_title'] = {
                'comments': 'The links on the WebPage are missing title tags. It is recommended to add title tags to all links for better user experience and SEO optimization.',
                'data': links_title[1]}

        # Find all the <h1> tags from source code, and store them to heading1
        # Example: <h1>jacket</h1>
        # If page has one h1 then return 1 else return 0
        heading1 = self.get_h_text(soup.find_all('h1'))
        if heading1[0] != 1:
            seo['heading1'] = 0
            if heading1[0] > 1:
                seo_suggestions['heading1'] = {
                    'comments': 'The WebPage contains multiple H1 tags, which should be unique. It is recommended to use only one H1 tag on a webpage for optimal SEO performance.',
                    'data': heading1[1]}
            else:
                seo_suggestions[
                    'heading1'] = {
                    'comments': 'It is recommended to utilize an H1 tag on the WebPage, incorporating the targeted keyword. Currently, the H1 tag is not being used.',
                    'data': ''}
        else:
            if self.is_word_in_string(self.target_keyword, heading1[1][0]):
                seo['heading1'] = 1
            else:
                seo['heading1'] = 0
                seo_suggestions['heading1'] = {
                    'comments': 'The H1 tag on the WebPage does not contain the targeted keyword (' + self.target_keyword + '). It is recommended to include the targeted keyword in the H1 tag for better SEO optimization.',
                    'data': heading1[1]}

        # Find all the <h2> tags from source code, and store them to heading2
        # Example: <h2>jacket</h2>
        # If page has at least one h2 return 1 else 0
        heading2 = self.get_h_text(soup.find_all('h2'))
        if heading2[0] == 0:
            seo['heading2'] = 0
            seo_suggestions['heading2'] = {
                'comments': 'The WebPage is not utilizing H2 tags. It is recommended to include H2 tags with the targeted keyword for better SEO optimization.',
                'data': ''}
        else:
            h2_suggestions = []
            for h2 in heading2[1]:
                if not self.is_word_in_string(self.target_keyword, h2):
                    h2_suggestions.append(h2)

            if not h2_suggestions:
                seo['heading2'] = 1
            else:
                seo['heading2'] = 0
                seo_suggestions['heading2'] = {
                    'comments': 'The H2 tags on the WebPage do not contain the targeted keyword. It is recommended to include the targeted keyword in the H2 tags for better SEO optimization.',
                    'data': h2_suggestions}

        # Find <title> tag from source code, and store it to title
        # Example: <title>jacket</title>
        # If page has title then return 1 else 0
        title = self.get_title_text(soup.find('title'))
        if not title:
            seo['title'] = 0
            seo_suggestions['title'] = {
                'comments': 'Your WebPage does not include a title tag, which is a mandatory element for SEO optimization. It is recommended to include a title tag with the targeted keyword for better search engine visibility.',
                'data': ''}
        else:
            if self.is_word_in_string(self.target_keyword, title):
                seo['title'] = 1
            else:
                seo['title'] = 0
                seo_suggestions['title'] = {
                    'comments': 'The title tag on the WebPage does not contain the targeted keyword. It is recommended to include the targeted keyword in the title tag for better SEO optimization.',
                    'data': title}

        # Get all meta tags
        meta_tags = soup.find_all('meta')

        # Find <meta> tag from source code with name="description" attribute, and store the content to meta_description
        # Example: <meta name="description" content="the meta description">
        # If page has meta_description then return 1 else 0
        meta_description = self.get_meta_description(meta_tags)
        if not meta_description:
            seo['meta_description'] = 0
            seo_suggestions['meta_description'] = {
                'comments': 'A meta description is mandatory for SEO, but it is missing on the WebPage.',
                'data': ''}
        else:
            if self.is_word_in_string(self.target_keyword, meta_description):
                seo['meta_description'] = 1
            else:
                seo['meta_description'] = 0
                seo_suggestions['meta_description'] = {
                    'comments': 'The WebPage\'s meta description does not contain the targeted keyword. It is recommended to include the targeted keyword in the meta description for better SEO optimization.',
                    'data': meta_description}

        # Find <meta> tag from source code with property="og:type" attribute, and store the content to opengraph
        # Example: <meta property="og:type" content="website" />
        # If page has at least one opengraph then return 1 else 0
        opengraph = self.get_meta_opengraph(meta_tags)
        if not opengraph:
            seo['opengraph'] = 0
            seo_suggestions['opengraph'] = {
                'comments': 'The WebPage is not using Opengraph tags, which can be helpful for SEO optimization.',
                'data': ''}
        else:
            seo['opengraph'] = 1

        # Get all link tags
        link_tags = soup.find_all('link')

        # Find all the <link> tags with rel='stylesheet' attribute and store their href to style
        # Example: <link rel='stylesheet' href='frontend.css'>
        # If every url include the word .min return 1 else 0
        style = self.get_style_list(link_tags)
        if style[0] == 0:
            seo['style'] = 0
            seo_suggestions['style'] = {
                'comments': 'The WebPage\'s stylesheets have not been minified, which can negatively impact website speed and SEO.',
                'data': style[1]}
        else:
            seo['style'] = 1

        # Find all the <link> tags with rel="sitemap" and
        # type="application/xml" attributes
        # And store their href to sitemap
        # Example: <link rel="sitemap" type="application/xml" href="sitemap.xml">
        # If there is at least one return 1 else 0
        sitemap = self.get_sitemap(link_tags)
        if not sitemap:
            seo['sitemap'] = 0
            seo_suggestions['sitemap'] = {
                'comments': 'A sitemap is crucial for SEO optimization, but the WebPage is not currently using one.',
                'data': ''}
        else:
            seo['sitemap'] = 1

        # Find all the <link> tags with rel="alternate" and
        # type="application/rss+xml" attributes
        # And store their href to rss
        # Example: <link rel="alternate" type="application/rss+xml" href="rss.php">
        # If there is at least one return 1 else 0
        rss = self.get_rss(link_tags)
        if not rss:
            seo['rss'] = 0
            seo_suggestions['rss'] = {
                'comments': 'The WebPage is not utilizing an RSS feed, which can be beneficial for SEO optimization.',
                'data': ''}
        else:
            seo['rss'] = 1

        # Get all script tags
        script_tags = soup.find_all('script')

        # Find all the <script> tags and store their src to script
        # Example: <script src='jquery.min.js'></script>
        # If every script url include the word .min return 1 else 0
        script = self.get_script_list(script_tags)
        if script[0] == 0:
            seo['script'] = 0
            seo_suggestions['script'] = {
                'comments': 'The WebPage\'s scripts have not been minified, which can negatively impact website speed and SEO.',
                'data': script[1]}
        else:
            seo['script'] = 1

        # Find all the <script> tags with type="application/ld+json" attribute
        # If there is at least one return 1 else 0
        # Example: <script type="application/ld+json">...</script>
        # If json-ld tag exists return 1 else 0
        seo['json_ld'] = self.get_json_ld(script_tags)
        if seo['json_ld'] == 0:
            seo_suggestions['json_ld'] = {
                'comments': 'It appears that the WebPage does not include JSON-LD structured data, which can be beneficial for SEO. Consider using JSON-LD, Microdata, or RDFa.',
                'data': ''}

        tags = soup.find('body').findChildren()

        # Check if there is inline css into source code.
        # If inline css return 0 else 1
        # Example: <div style='color:red;font-size:16px'>
        seo['inline_css'] = self.get_inline_css_flag(tags)
        if seo['inline_css'] == 0:
            seo_suggestions['inline_css'] = {
                'comments': 'It appears that the WebPage is using inline CSS, which is not optimal for SEO. It is recommended to include CSS styles in an external file for better website performance and search engine visibility.',
                'data': ''}

        # Check if there is anywhere in the code the attribute itemtype
        # If there is at least one return 1 else 0
        # Example: <div itemscope itemtype="https://schema.org/Movie">
        seo['microdata'] = self.get_item_type_flag(tags)
        if seo['microdata'] == 0:
            seo_suggestions['microdata'] = {
                'comments': 'It appears that the WebPage does not include Microdata structured data, which can be beneficial for SEO. Consider using JSON-LD, Microdata, or RDFa.',
                'data': ''}

        # Check if there is anywhere in the code the attribute vocab
        # If there is at least one return 1 else 0
        # Example: <address property="http://example.org/address"
        #          vocab="http://example.org/" typeof="Address">
        seo['rdfa'] = self.get_rdfa_flag(tags)
        if seo['rdfa'] == 0:
            seo_suggestions['rdfa'] = {
                'comments': 'It appears that the WebPage does not include RDFa structured data, which can be beneficial for SEO. Consider using JSON-LD, Microdata, or RDFa.',
                'data': ''}

        # Send a request to url + 'robots.txt'
        # and return 1 if r.status_code == 200 (robots.txt exist)
        seo['robots'] = self.get_robots(self.url)
        if seo['robots'] == 0:
            seo_suggestions['robots'] = {
                'comments': 'It seems that the WebPage is missing a robots.txt file, which is important for both SEO and security purposes.',
                'data': ''}

        # Send a request to url
        # and get from the response HEAD the 'Content-Encoding'
        # if ['Content-Encoding'] == 'gzip' return 1 else 0
        seo['gzip'] = self.get_gzip(self.url)
        if seo['gzip'] == 0:
            seo_suggestions['gzip'] = {
                'comments': 'It appears that the WebPage is not utilizing gzip compression, which can help improve loading speed, save bandwidth for users, and have positive impacts on SEO.',
                'data': ''}

        # If the given url includes https return 1 else 0
        # It is proposed an alternative method instead
        seo['web_ssl'] = self.get_web_ssl(self.url)
        if seo['web_ssl'] == 0:
            seo_suggestions['web_ssl'] = {
                'comments': 'The WebPage may not be using SSL/HTTPS, which is a protocol that can be important for SEO optimization.',
                'data': ''}

        # If the given url is seo friendly return 1 else 0
        seo['seo_friendly_url'] = self.seo_friendly_url(self.url)
        if seo['seo_friendly_url'] == 0:
            seo_suggestions['seo_friendly_url'] = {
                'comments': 'The WebPage does not use an SEO/user-friendly URL, which can be important for optimizing search engine visibility.',
                'data': ''}

        # If the given url follows the amp guidelines return 1 else 0
        if seo['amp'] == '':  # if the amp is not specified then check if the url follows the amp guidelines
            seo['amp'] = self.get_amp(self.url)
            if seo['amp'] == 0:
                seo_suggestions['amp'] = {
                    'comments': 'It appears that the WebPage is not utilizing AMP, which can be beneficial for SEO optimization.',
                    'data': ''}

        # Get WebPage's speed using the runPagespeed API
        from apiPagespeed import apiPagespeed
        speed = apiPagespeed(self.url, self.pagespeed_api_key)
        seo['speed'] = speed.get_speed()

        # Check if the WebPage is responsive using the mobileFriendlyTest API
        from apiMobileFriendlyTest import apiMobileFriendlyTest
        mobile = apiMobileFriendlyTest(self.url, self.mobile_api_key)
        seo['responsive'] = mobile.get_responsive_test()

        # Get the Website's Domain Authority using the MozScape API
        from apiMOZ import apiMOZ
        da = apiMOZ(self.url, self.moz_api_client, self.moz_api_key)
        seo['da'] = da.get_da()

        # Predict website's backlinks' number based on DA
        # Predict website's linking domains' number based on DA
        from Predict import Predict
        predict = Predict(seo['da'])

        seo['backlinks'] = predict.predict_backlinks()
        seo['linking_domains'] = predict.predict_linking_domains()

        return seo, seo_suggestions

    def get_image_alt(self, img_tags):
        images_alt_dict = {}
        has_attr = 1
        for img_tag in img_tags:
            if img_tag.get('src'):
                if not img_tag.get('alt'):
                    has_attr = 0
                    images_alt_dict[img_tag.get('src')] = img_tag.get('alt')

        return has_attr, images_alt_dict

    def get_links_title(self, a_tags):
        link_titles_dict = {}
        has_attr = 1
        for a_tag in a_tags:
            href = a_tag.get('href') if a_tag.get('href') else ''
            title = a_tag.get('title') if a_tag.get('title') else ''

            if not title:
                has_attr = 0
                link_titles_dict[href] = title

        return has_attr, link_titles_dict

    # This function can be used for all the h tags h1-h6 just pass the h tags as needed
    def get_h_text(self, h_tags):
        h_text_list = []
        for h_tag in h_tags:
            h_text_list.append(h_tag.text)

        return len(h_text_list), h_text_list

    def get_title_text(self, title_tag):
        return title_tag.text if title_tag else ''

    def get_meta_description(self, meta_tags):
        for meta_tag in meta_tags:
            if 'name' in meta_tag.attrs and meta_tag['name'] == 'description':
                return meta_tag.get('content') if meta_tag.get('content') else ''

        return ''  # return '' if no name = 'description' exists

    def get_meta_opengraph(self, meta_tags):
        for meta_tag in meta_tags:
            if 'property' in meta_tag.attrs and meta_tag['property'] == 'og:type':
                return meta_tag.get('content') if meta_tag.get('content') else ''

        return ''  # return '' if no property = 'og:type' exists

    def get_meta_responsive(meta_tags):
        for meta_tag in meta_tags:
            if 'name' in meta_tag.attrs and meta_tag['name'] == 'viewport':
                return meta_tag.get('content') if meta_tag.get('content') else ''

        return ''  # return '' if no name = 'viewport' exists

    def get_style_list(self, link_tags):
        style_list = []
        is_minified = 1
        for link_tag in link_tags:
            if 'rel' in link_tag.attrs and 'stylesheet' in link_tag['rel']:
                if link_tag.get('href'):
                    # check if the file is minified by url
                    if 'min.' in link_tag.get('href'):
                        is_minified = 1
                    else:
                        is_minified = 0
                        style_list.append(link_tag.get('href'))  # append if not include min word

        return is_minified, style_list
        # Instead you can check for comments into a css file. Minified files have not any comments
        # Retrieve the contents of the CSS file from the URL
        # response = requests.get(url)
        # css = response.text
        #
        # # Check for any occurrence of two or more whitespace characters in a row
        # whitespace_regex = re.compile(r'\s{2,}')
        # if whitespace_regex.search(css):
        #     return 0
        #
        # # Check for any occurrence of a comment marker (/* */) followed immediately by a line break
        # comment_regex = re.compile(r'/\*.*?\*/\n')
        # if comment_regex.search(css):
        #     return 0
        #
        # return 1

    def get_sitemap(self, link_tags):
        for link_tag in link_tags:
            if ('rel' in link_tag.attrs and 'sitemap' in link_tag['rel']) and \
                    ('type' in link_tag.attrs and 'application/xml' in link_tag['type']):
                return link_tag.get('href') if link_tag.get('href') else ''

        return ''  # return '' if no match found

    def get_rss(self, link_tags):
        for link_tag in link_tags:
            if ('rel' in link_tag.attrs and 'alternate' in link_tag['rel']) and \
                    ('type' in link_tag.attrs and 'application/rss+xml' in link_tag['type']):
                return link_tag.get('href') if link_tag.get('href') else ''

        return ''  # return '' if no match found

    def get_script_list(self, script_tags):
        script_list = []
        is_minified = 1
        for script_tag in script_tags:
            if script_tag.get('src'):
                # check if the file is minified by url
                if 'min.' in script_tag.get('src'):
                    is_minified = is_minified
                else:
                    is_minified = 0
                    script_list.append(script_tag.get('src'))
        return is_minified, script_list

    def get_json_ld(self, script_tags):
        for script_tag in script_tags:
            if 'type' in script_tag.attrs and script_tag['type'] == 'application/ld+json':
                return 1

        return 0  # return 0 if no name = 'application/ld+json' exists

    def get_inline_css_flag(self, tags):
        for tag in tags:
            if tag.get('style'):
                return 0

        return 1

    def get_item_type_flag(self, tags):
        for tag in tags:
            if tag.get('itemtype'):
                return 1

        return 0

    def get_rdfa_flag(self, tags):
        for tag in tags:
            if tag.get('vocab'):
                return 1

        return 0

    def get_robots(self, url):
        par_url = urlparse(url)
        robots_url = par_url.scheme + '://' + par_url.netloc + '/robots.txt'
        r = requests.get(robots_url)
        return 1 if r.status_code == 200 else 0

    def get_gzip(self, url):
        response = requests.request("HEAD", self.url)
        if 'Content-Encoding' in response.headers and response.headers['Content-Encoding'] == 'gzip':
            return 1
        else:
            return 0

    def get_web_ssl(self, url):
        response = requests.get(url)  # send a GET request to the website

        # check if the response URL starts with https://
        if response.url.startswith("https://"):
            return 1
        else:
            return 0

        # Additionally you can check if the ssl certificate is valid
        # In our tool we know in advance that the URL is correct based on zenserp API
        # import ssl
        # import socket
        # # create a socket connection to the web page
        # context = ssl.create_default_context()
        # with socket.create_connection((url, 443)) as sock:
        #     with context.wrap_socket(sock, server_hostname=url) as sslsock:
        #         # check the validity of the SSL/TLS certificate
        #         cert = sslsock.getpeercert()
        #         if ssl.match_hostname(cert, url):
        #             return 1  # The SSL/TLS certificate is valid
        #         else:
        #             return 0  # The SSL/TLS certificate is invalid

    def seo_friendly_url(self, url):
        from urllib.parse import urlparse, urlunparse

        # use urlparse to extract the path, parameters, and query string
        parsed_url = urlparse(url)
        path = parsed_url.path
        params = parsed_url.params
        query_string = parsed_url.query

        # combine the path, parameters, and query string components into a single string
        path = urlunparse(('', '', path, params, query_string, ''))

        if path == "":  # we do not have a path so the url is by default seo friendly
            return 1
        else:
            # define a regular expression pattern
            pattern = r'^[a-z0-9/-]+$'

            # check if the URL matches the pattern
            if re.match(pattern, path):
                return 1
            else:
                return 0

    def get_amp(self, url):
        # get the HTML content of the web page
        response = requests.get(url)
        html = response.content

        # parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # check if the HTML includes at least a link tag with rel="amphtml"
        if soup.find("link", {"rel": "amphtml"}):
            return 1
        else:
            return 0

    def is_word_in_string(self, word, string):
        regex = r'\b' + re.escape(word) + r'\b'
        if re.search(regex, string, re.IGNORECASE | re.UNICODE):
            return 1
        else:
            return 0
