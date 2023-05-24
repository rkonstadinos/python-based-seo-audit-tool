# A Machine Learning Python-based Search Engine Optimization Audit Software

**Description**:  This opensource software provides support for the scientific documentation presented in the research article entitled "A Machine Learning Python-based Search Engine Optimization Audit Software" that has been published in [Applied Sciences | MDPI](https://www.mdpi.com/journal/applsci) academic journal.

**Aim**: The present study aims to develop an open-source Python-based SEO audit software that will be accessible to the general public without charge and that will perform functions comparable to those offered by commercial SEO audit tools at a cost. The overarching objective is to produce an open-source SEO tool that will provide users with recommendations on appropriate SEO techniques, based on the analysis of their competitors' websites, with the aim of optimizing their own websites for SEO and achieving improved search rankings and traffic.

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
- Next, you will need to generate a free API KEY from the ZenSerp [ZenSerp](https://app.zenserp.com/register?plan=free) page. ( 50 requests / month for free )
- You will need to generate a free API KEY from [MOZ](https://moz.com/products/api/pricing) page. ( Free access allows for one request every ten seconds, up to 2,500 rows per month )
- You will need to generate a free API KEY from [mobileFriendlyTest: Google Search Console Testing Tools API](https://developers.google.com/webmaster-tools/search-console-api/v1/configure) page. ( [Usage Limits](https://developers.google.com/webmaster-tools/search-console-api/limits) )
- Finally, you will need to generate a free API KEY from [PageSpeed Insights API](https://developers.google.com/speed/docs/insights/v5/get-started) page.

If all of the above seems difficult to you, contact us so that we can create the keys together and export the code in an executable format, eg .exe to run without installation on your computer.
## Built With

* [ZenSerp API](https://zenserp.com/) - Used to get the SERPs
* [MOZ API](https://moz.com/products/api/pricing) - Used to get the DA
* [mobileFriendlyTest: Google Search Console Testing Tools API](https://developers.google.com/webmaster-tools/search-console-api/v1/configure) - Used to perform a mobile-friendly test
* [PageSpeed Insights API](https://developers.google.com/speed/docs/insights/v5/get-started) - Used to perform a speed test

## Authors

* **Konstantinos I. Roumeliotis**
* **Prof. Nikolaos D. Tselikas**

## License

This project is licensed under the MIT License.
The python libraries and APIs used clearly belong to their respective owners.

MIT License

Copyright (c) 2023 Konstantinos I. Roumeliotis, Nikolaos D. Tselikas

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

