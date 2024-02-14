# A Machine Learning Python-Based Search Engine Optimization Audit Software

## Published Paper
* **Journal**: [Informatics | An Open Access Journal from MDPI](https://www.mdpi.com/journal/informatics)
* **Title**: [A Machine Learning Python-Based Search Engine Optimization Audit Software](https://www.mdpi.com/2227-9709/10/3/68)
* **DOI**: https://doi.org/10.3390/informatics10030068

## Authors
* **Konstantinos I. Roumeliotis**
* **Prof. Nikolaos D. Tselikas**

## Abstract
In the present-day digital landscape, websites have increasingly relied on digital marketing practices, notably search engine optimization (SEO), as a vital component in promoting sustainable growth. The traffic a website receives directly determines its development and success. As such, website owners frequently engage the services of SEO experts to enhance their website’s visibility and increase traffic. These specialists employ premium SEO audit tools that crawl the website’s source code to identify structural changes necessary to comply with specific ranking criteria, commonly called SEO factors. Working collaboratively with developers, SEO specialists implement technical changes to the source code and await the results. The cost of purchasing premium SEO audit tools or hiring an SEO specialist typically ranges in the thousands of dollars per year. Against this backdrop, this research endeavors to provide an open-source Python-based Machine Learning SEO software tool to the general public, catering to the needs of both website owners and SEO specialists. The tool analyzes the top-ranking websites for a given search term, assessing their on-page and off-page SEO strategies, and provides recommendations to enhance a website’s performance to surpass its competition. The tool yields remarkable results, boosting average daily organic traffic from 10 to 143 visitors.

## Installation

- For successful installation of this software, it is imperative that your computing system is equipped with the latest edition of Python (i.e., Python 3.10 or Python 3.11).
- It is recommended that each file be consulted and that the requisite libraries be installed, as denoted within the associated classes.
  - import csv
  - from bs4 import BeautifulSoup
  - from SEOmozAPISamples.python.mozscape import Mozscape
  - import requests
  - import json
  - from urllib.parse import urlparse
  - import pandas as pd
  - from sklearn.ensemble import RandomForestRegressor
  - from sklearn.model_selection import train_test_split
  - from sklearn.metrics import mean_squared_error
  - import joblib
  - import re
- Next, you will need to generate a free API KEY from the ZenSerp [ZenSerp](https://app.zenserp.com/register?plan=free) page. ( Usage Limit: 50 requests / month for free )
- You will need to generate a free API KEY from [MOZ](https://moz.com/products/api/pricing) page. ( Usage Limit: Free access allows for one request every ten seconds, up to 2,500 rows per month )
- You will need to generate a free API KEY from [mobileFriendlyTest: Google Search Console Testing Tools API](https://developers.google.com/webmaster-tools/search-console-api/v1/configure) page. ( [Usage Limits](https://developers.google.com/webmaster-tools/search-console-api/limits) )
- Finally, you will need to generate a free API KEY from [PageSpeed Insights API](https://developers.google.com/speed/docs/insights/v5/get-started) page.

If you encounter challenges while following the aforementioned steps, we are available to assist you in creating the required keys and exporting your code into an executable format. This executable can be executed directly on your computer without the need for any installation process. Please feel free to reach out to us for further guidance and support in this regard.
## Built With

* [ZenSerp API](https://zenserp.com/) - Used to get the SERPs
* [MOZ API](https://moz.com/products/api/pricing) - Used to get the DA
* [mobileFriendlyTest: Google Search Console Testing Tools API](https://developers.google.com/webmaster-tools/search-console-api/v1/configure) - Used to perform a mobile-friendly test
* [PageSpeed Insights API](https://developers.google.com/speed/docs/insights/v5/get-started) - Used to perform a speed test
