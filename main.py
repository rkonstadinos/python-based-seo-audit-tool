from urllib.parse import urlparse
from apiZenSerp import apiZenSerp
from seoSuggestions import seoSuggestions
from seoAudit import seoAudit
from createCSV import createCSV


def is_valid_url(url):
    try:
        # use urlparse to check if the input string is a valid URL
        parsed_url = urlparse(url)
        if all([parsed_url.scheme, parsed_url.netloc]):
            return 1
        else:
            return 0
    except ValueError:
        return 0


# Request from user website URL
user_website = input('Type your web page\'s URL\n')
if is_valid_url(user_website) == 0:
    print('Invalid URL structure')
    exit()

# Request from user the target keyword
target_keyword = input('Type the target keyword\n')
if not target_keyword:
    print('Invalid keyword')
    exit()

# create a free account on https://app.zenserp.com/
# get your API key up to 50 free API requests per month
# or upgrade to premium
zenserp_api_key = input('Type the ZenSerp Api Key\n')  # Ex. 5c2cc020-69c3-11ed-8cef-d7f0d916d783
if not zenserp_api_key:
    print('Invalid API Key')
    exit()

# create a free account on https://moz.com/products/api/pricing
# get your API key up to 2,500 rows per month
# or upgrade to premium
moz_api_client = input("Type the Moz Client ID\n")  # Ex. mozscape-229f6d2c36
if not moz_api_client:
    print('Invalid Moz Client ID')
    exit()

moz_api_key = input("Type the Moz API Key ID\n")  # Ex. 442b26fb278eb50caf8b1412a702c077
if not moz_api_key:
    print('Invalid Moz API Key')
    exit()

# use your gmail to get a key from https://developers.google.com/webmaster-tools/search-console-api/v1/configure
# there are limitations have to take into consideration
# https://developers.google.com/webmaster-tools/search-console-api/v1/pricing
mobile_api_key = input("Type the MobileFriendlyTest API Key ID\n")  # Ex. AIzaSyABgSO4Z0p-zEjnzHIRRWjS5fEBNWal7-s
if not mobile_api_key:
    print('Invalid MobileFriendlyTest API Key')
    exit()

# use your gmail to get a key from https://developers.google.com/speed/docs/insights/v5/get-started
# there are limitations have to take into consideration
pagespeed_api_key = input("Type the PageSpeed API Key ID\n")  # Ex. AIzaSyAVDI6VTjyzpG1KrGrCMuM15Dw7BH1g3zE
if not pagespeed_api_key:
    print('Invalid PageSpeed API Key')
    exit()

seo = []
tool_suggestions = {}
seo_suggestions = {}

# Retrieve from API search results for this specific target_keyword
GetSERPS = apiZenSerp(target_keyword, zenserp_api_key)
websites = GetSERPS.get_organic_serps()
websites['target_website'] = {'position': 0, 'url': user_website, 'amp': ''}  # Add user_website to the list

# for each website url
for website in websites:
    # perform seo checks
    seo_audit = seoAudit(websites[website]['url'], websites[website]['position'],
                         websites[website]['amp'], target_keyword, moz_api_client, moz_api_key, mobile_api_key,
                         pagespeed_api_key)
    seo_results = seo_audit.perform_seo_checks()

    # append the returned dictionary to seo
    seo.append(seo_results[0])
    tool_suggestions[websites[website]['url']] = seo_results[1]

# Create an empty CSV file and its column names
csv_columns = ['page', 'position', 'amp', 'images_alt', 'links_title', 'heading1', 'heading2',
               'title', 'meta_description',
               'opengraph', 'style', 'sitemap', 'rss', 'script', 'json_ld', 'inline_css', 'microdata',
               'rdfa', 'robots', 'gzip', 'web_ssl', 'seo_friendly_url', 'speed', 'responsive', 'da',
               'backlinks',
               'linking_domains']
csv = createCSV([], "report-seo_audit.csv")
csv.create_csv(csv_columns)

# Write SEO results from competitors' and user's websites to a csv file
for seo_checks in seo:
    csv = createCSV([seo_checks], "report-seo_audit.csv")
    csv.append_csv(csv_columns)

# Provide SEO suggestions and changes that must be made to user's website
suggestions_based_on_competition = seoSuggestions()
suggestions_based_on_competition = suggestions_based_on_competition.seo_suggestions()

# Create CSVs as an output to the user
csv = createCSV(suggestions_based_on_competition, "report-suggestions_based_on_competition.csv")
csv.suggestions_to_csv()
csv = createCSV(seo, "report-seo_competitors_table.csv")
csv.seo_competitors_table()
csv = createCSV(seo, "report-seo_tool_suggestions.csv")
csv.seo_tool_suggestions(user_website, tool_suggestions, suggestions_based_on_competition)
exit()

# Additionally you can check for dead links on user's website
# from findDeadLinks import findDeadLinks
# deadlinks = findDeadLinks(user_website)
# deadlinks = deadlinks.dead_links()
# print(deadlinks)