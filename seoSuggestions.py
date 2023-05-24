import pandas as pd


# Give SEO suggestions to user based on the SEO Audit results from SEOTechniques
class seoSuggestions:
    def __init__(self):
        self.seo_rules = {
            'images_alt': [
                'Example: <img src="..." alt="...">',
                'According to Google\'s Image publishing guidelines, adding descriptive alt text to your images can help people with visual impairments understand the content of your images. Google also considers alt text as a ranking factor for image search.',
                'The Web Content Accessibility Guidelines (WCAG) recommend using alternative text for all non-text content, including images, to ensure accessibility for people with disabilities.',
                'Moz, a leading SEO software provider, also recommends using alternative text for images as a best practice for SEO optimization.'
            ],
            'links_title': [
                'Example: <a href="..." title="...">',
                'According to Google\'s Search Engine Optimization (SEO) Starter Guide, adding descriptive title tags to your links can help both users and search engines understand the content of your pages. Google also considers title tags as a ranking factor for search results.',
                'The Web Content Accessibility Guidelines (WCAG) also recommend using descriptive text for links, including title attributes, to ensure accessibility for people with disabilities.',
                'Moz, a leading SEO software provider, also recommends using descriptive title tags for links as a best practice for SEO optimization.'
            ],
            'heading1': [
                'Example: <h1>...</h1>',
                'According to Google\'s Search Engine Optimization (SEO) Starter Guide, the use of descriptive, well-structured headings can help make your page more accessible and understandable for both users and search engines. The guide recommends using one H1 tag per page, and incorporating your primary keyword into it.',
                'Moz, a leading SEO software provider, also recommends using a single H1 tag on each page, and incorporating the primary keyword into it. They suggest using H2-H6 tags for subheadings and other content hierarchy.',
                'Ahrefs, another popular SEO tool, also recommends using H1 tags and optimizing them with targeted keywords for better SEO performance.'],
            'heading2': [
                'Example: <h2>...</h2>',
                'According to Google\'s Search Engine Optimization (SEO) Starter Guide, using descriptive, well-structured headings such as H2 tags can help make your page more accessible and understandable for both users and search engines. Google also considers headings as a ranking factor for search results.',
                'Moz, a leading SEO software provider, recommends using H2 tags for subheadings and other content hierarchy. They suggest incorporating targeted keywords into H2 tags to help with SEO optimization.',
                'Ahrefs, another popular SEO tool, also recommends using H2 tags for subheadings and incorporating targeted keywords into them for better SEO performance.'],
            'title': [
                'Example: <title>...</title>',
                'According to Google\'s Search Engine Optimization (SEO) Starter Guide, using descriptive, well-structured <title> tags can help make your page more accessible and understandable for both users and search engines. Google also considers <title> tags as a ranking factor for search results.',
                'The Web Content Accessibility Guidelines (WCAG) also recommend using descriptive and concise <title> tags to ensure accessibility for people with disabilities.',
                'Moz, a leading SEO software provider, recommends including targeted keywords in the <title> tag for better search engine visibility and click-through rates.'
            ],
            'meta_description': [
                'Example: <meta name="description" content="..." />'
                'According to Google\'s Search Engine Optimization (SEO) Starter Guide, meta descriptions are an important element for on-page SEO, as they provide a concise summary of a webpage\'s content to search engines and users.',
                'Moz, a leading SEO software provider, recommends including targeted keywords in the meta description for better search engine visibility and click-through rates.',
                'Yoast, a popular SEO plugin for WordPress, advises website owners to create unique and compelling meta descriptions that accurately reflect the content on the page, while also including the targeted keyword.'
            ],
            'opengraph': [
                'Example: <meta property="og:title" content="..." /><meta property="og:description" content="..." /><meta property="og:image" content="..." />',
                'According to Facebook, Open Graph tags allow you to control how your website content appears when it is shared on Facebook, which can improve click-through rates and engagement.',
                'Yoast, a popular SEO plugin for WordPress, recommends using Open Graph tags to help your content look better on social media platforms and to provide additional context for search engines.',
                'Moz, a leading SEO software provider, also recommends using Open Graph tags for better social media engagement and search engine visibility.'
            ],
            'style': [
                'Example: <link rel="stylesheet" href="theme.min.css">',
                'According to Google\'s PageSpeed Insights, minifying CSS files can significantly reduce page load times and improve website speed.',
                'HubSpot, a leading marketing software provider, recommends minifying stylesheets as part of a broader set of strategies to improve website speed and SEO.',
                'Yoast, a popular SEO plugin for WordPress, also recommends minifying stylesheets to improve website performance and SEO.'
            ],
            'sitemap': [
                'Example: <link rel="sitemap" type="application/xml" href="path/to/sitemap.xml" />',
                'From Google\'s official documentation: "A sitemap is a file where you provide information about the pages, videos, and other files on your site, and the relationships between them. Search engines like Google read this file to more intelligently crawl your site. A sitemap tells Google which pages and files you think are important in your site, and also provides valuable information about these files: for example, for pages, when the page was last updated, how often the page is changed, and any alternate language versions of a page."',
                'According to Yoast SEO: "A sitemap is a file where you can list the web pages of your site to tell Google and other search engines about the organization of your site content. Search engine web crawlers like Googlebot read this file to more intelligently crawl your site."',
                'From Moz: "Sitemaps help search engines index your website correctly and quickly. A sitemap is essentially a map of all the pages on your website. Submitting a sitemap to search engines ensures that they know about all the pages on your site, including URLs that may not be discoverable by their normal crawling process."'
            ],
            'rss': [
                'Example: <link rel="alternate" type="application/rss+xml" title="Title of Your RSS Feed" href="http://www.example.com/rss.xml" />',
                'Utilizing an RSS feed can allow search engines to easily crawl and index your website\'s content, which can help improve your search engine visibility.',
                'RSS feeds can also make it easier for visitors to subscribe to your content and stay up-to-date with new posts and updates.'
            ],
            'json_ld': [
                'Google\'s documentation on structured data: https://developers.google.com/search/docs/guides/intro-structured-data',
                'Moz\'s guide to structured data: https://moz.com/learn/seo/schema-structured-data',
                'Search Engine Land\'s article on the benefits of structured data: https://www.searchenginepeople.com/blog/5-reasons-add-structured-data-site.html'
            ],
            'inline_css': [
                'According to Google\'s PageSpeed Insights, one of the key factors affecting website speed is the number of CSS resources that need to be downloaded and processed by the browser. When CSS is inlined, it adds to the size of the HTML file, which can increase the load time for the webpage. Additionally, search engines may have a harder time interpreting the CSS styles if they are not in a separate file.',
                'To optimize CSS delivery and improve website speed and SEO, it is recommended to externalize CSS styles in a separate file, and to minify and compress the file to reduce its size. This can also make it easier to maintain and update the website\'s design and styling.'
            ],
            'microdata': [
                'Google\'s documentation on structured data: https://developers.google.com/search/docs/guides/intro-structured-data',
                'Moz\'s guide to structured data: https://moz.com/learn/seo/schema-structured-data',
                'Search Engine Land\'s article on the benefits of structured data: https://www.searchenginepeople.com/blog/5-reasons-add-structured-data-site.html'
            ],
            'rdfa': [
                'Google\'s documentation on structured data: https://developers.google.com/search/docs/guides/intro-structured-data',
                'Moz\'s guide to structured data: https://moz.com/learn/seo/schema-structured-data',
                'Search Engine Land\'s article on the benefits of structured data: https://www.searchenginepeople.com/blog/5-reasons-add-structured-data-site.html'
            ],
            'robots': [
                'Google\'s documentation on robots.txt: https://developers.google.com/search/docs/advanced/robots/create-robots-txt',
                'Moz\'s guide on robots.txt: https://moz.com/learn/seo/robotstxt',
                'Semrush\'s article on robots.txt: https://www.semrush.com/blog/beginners-guide-robots-txt/'
            ],
            'gzip': [
                'Google Developers - Optimize Encoding and Transfer Size of Text-Based Assets: https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/optimize-encoding-and-transfer',
                'Mozilla Developer Network - HTTP compression: https://developer.mozilla.org/en-US/docs/Web/HTTP/Compression',
                'GTmetrix - What is Gzip Compression?: https://gtmetrix.com/enable-gzip-compression.html',
                'BetterExplained - The Importance Of Gzipping Your Website: https://betterexplained.com/articles/how-to-optimize-your-site-with-gzip-compression/'
            ],
            'web_ssl': [
                'Google: HTTPS as a ranking signal - https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html',
                'Moz: HTTPS SEO Checklist - https://moz.com/blog/seo-tips-https-ssl'
            ],
            'seo_friendly_url': [
                'According to Google\'s Search Engine Optimization (SEO) Starter Guide, creating user-friendly and easily understandable URLs can improve search engine ranking and make it easier for users to navigate a website. Specifically, the guide recommends keeping URLs simple and descriptive, using words that accurately describe the page\'s content, and avoiding lengthy or confusing URLs that can deter users from clicking on them.'
            ],
            'amp': [
                'According to Google\'s official documentation, Accelerated Mobile Pages (AMP) is a framework for building fast, mobile-friendly web pages. Google has indicated that the use of AMP can have a positive impact on a website\'s search engine ranking, as it is designed to load quickly and improve the user experience on mobile devices. Additionally, AMP pages are indicated by a special icon in mobile search results, which can help improve visibility and click-through rates.'
            ]

        }

    def seo_suggestions(self):
        # Initialize a suggestions Dictionary
        suggestions = {'page': 'suggestions', 'position': 0, 'amp': 0, 'images_alt': 0, 'links_title': 0,
                       'heading1': 0,
                       'heading2': 0, 'title': 0, 'meta_description': 0, 'opengraph': 0, 'style': 0, 'sitemap': 0,
                       'rss': 0,
                       'script': 0, 'json_ld': 0, 'inline_css': 0, 'microdata': 0, 'rdfa': 0, 'robots': 0,
                       'gzip': 0,
                       'web_ssl': 0, 'seo_friendly_url': 0, 'speed': 0, 'responsive': 0, 'da': 0,
                       'predict_backlinks': 0,
                       'predict_linking_domains': 0}

        ## 1. SEO Techniques
        # List of columns to select from the CSV file
        seo_techniques = ['amp', 'images_alt', 'links_title', 'heading1', 'heading2', 'title', 'meta_description',
                          'opengraph', 'style', 'sitemap', 'rss', 'script', 'json_ld', 'inline_css', 'microdata',
                          'rdfa',
                          'robots', 'gzip', 'web_ssl', 'seo_friendly_url', 'responsive']

        # Load the CSV file into a pandas DataFrame with only the selected columns and ignore the last row which is actually user's website
        df = pd.read_csv('report-seo_audit.csv', skipfooter=1, engine='python', usecols=seo_techniques)

        # Count the number of rows in the DataFrame
        num_rows = df.shape[0]

        # Loop through each column in the DataFrame
        for col in df.columns:
            # Count the occurrences of 1s in the column
            ones_count = df[col].sum()

            # Find if the majority of the competitors use this technique
            if ones_count >= (num_rows / 2):
                # If true, make changes to the suggestions variable
                suggestions[col] = 1

        ## 2. SEO Metrics
        # List of columns to select from the CSV file
        seo_metrics = ['speed', 'da', 'backlinks', 'linking_domains']

        # Load the CSV file into a pandas DataFrame with only the selected columns and ignore the last row which is actually user's website
        df = pd.read_csv('report-seo_audit.csv', skipfooter=1, engine='python', usecols=seo_metrics)

        # Loop through each column in the DataFrame
        for col in df.columns:
            # If the column is speed find the maximum value in the column
            if col == 'speed':
                mm_value = df[col].max()
            # Else find the minimum value in the column
            else:
                mm_value = df[col].min()

            suggestions[col] = mm_value

        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv('report-seo_audit.csv')

        # Get the column names of the DataFrame
        column_names = list(df.columns)

        # Get the last row of the DataFrame which is actually user's website
        last_row = df.iloc[-1]

        # Create a dictionary from the last row and column names
        user_website = {column_names[i]: last_row[i] for i in range(len(column_names))}

        seo_recommendations = {}
        # Loop through the SEO techniques and return the suggestions
        for seo in seo_techniques:
            # If user's website do not follow this technique, but the suggestions suggest its usage
            if user_website[seo] == 0 and suggestions[seo] == 1:
                # Append the recommendation
                seo_recommendations[seo] = "It is suggested to use the [" + seo + "] SEO technique, which the " \
                                                                                  "majority of the competition have " \
                                                                                  "also applied. "

        # Loop through the SEO metrics and return the suggestions
        for seo in seo_metrics:
            if seo == 'speed':
                if user_website[seo] > suggestions[seo]:
                    seo_recommendations[seo] = "Currently, your website has [" + seo + "] = [" + user_website[
                        seo] + "]. It is suggested to improve the loading speed of your website, since the maximum loading speed of competing websites is [" + \
                                               suggestions[seo] + "] seconds."
            else:
                if user_website[seo] < suggestions[seo]:
                    seo_recommendations[seo] = "Currently, your website has [" + seo + "] = [" + user_website[
                        seo] + "]. It is suggested to increase the number of [" + seo + "] for your website, since the minimum " + seo + " of competing websites is [" + \
                                               suggestions[seo] + "]."

        return {"seo_recommendations": seo_recommendations, "seo_rules": self.seo_rules}
