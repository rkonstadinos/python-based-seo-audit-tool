import csv  # use the csv library to save the dictionary to a csv file


class createCSV:
    def __init__(self, seo, csv_file):
        self.seo = seo
        self.csv_file = csv_file

    def create_csv(self, csv_columns):

        dict_data = self.seo
        try:
            with open(self.csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)
        except IOError:
            return 0
        return 1

    def append_csv(self, csv_columns):
        dict_data = self.seo
        try:
            with open(self.csv_file, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                # writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)
        except IOError:
            return 0
        return 1

    def suggestions_to_csv(self):
        seo_issues = self.seo['seo_recommendations']
        seo_rules = self.seo['seo_rules']

        issues = []
        for issue_key, issue_value in seo_issues.items():
            my_rule = ''
            for rule in seo_rules[issue_key]:
                my_rule = my_rule + '- ' + rule + '\n'

            issues.append({'Missing SEO Technique': issue_key, 'Comments': issue_value, 'SEO Rules': my_rule})

        self.seo = issues
        self.create_csv(['Missing SEO Technique', 'Comments', 'SEO Rules'])

    def seo_competitors_table(self):
        new_seo = []
        zero_one_techniques = ['amp', 'images_alt', 'links_title', 'heading1', 'heading2', 'title', 'meta_description',
                               'opengraph', 'style', 'sitemap', 'rss', 'script', 'json_ld', 'inline_css', 'microdata',
                               'rdfa', 'robots', 'gzip', 'web_ssl', 'seo_friendly_url', 'responsive']
        for page in self.seo:
            for seo_key, seo_value in page.items():
                if seo_key in zero_one_techniques:
                    if seo_value == 0:
                        page[seo_key] = ''
                    else:
                        page[seo_key] = '✓'
                else:
                    page[seo_key] = seo_value
            new_seo.append(page)

        self.create_csv(['page', 'position', 'amp', 'images_alt', 'links_title', 'heading1', 'heading2',
                         'title', 'meta_description',
                         'opengraph', 'style', 'sitemap', 'rss', 'script', 'json_ld', 'inline_css', 'microdata',
                         'rdfa', 'robots', 'gzip', 'web_ssl', 'seo_friendly_url', 'speed', 'responsive', 'da',
                         'backlinks',
                         'linking_domains'])

    def seo_tool_suggestions(self, url, tool_suggestions, suggestions_based_on_competition):
        new_suggestions = []
        user_website_tool_suggestions = tool_suggestions[url]  # user_website
        for sug_key, sug_value in user_website_tool_suggestions.items():
            my_rule = ''  # find the seo_rule
            if sug_key in suggestions_based_on_competition['seo_rules']:
                my_rules = suggestions_based_on_competition['seo_rules'][sug_key]
                for rule in my_rules:
                    my_rule = my_rule + '- ' + rule + '\n'
            else:
                my_rule = 'No SEO rules found for this technique\n'

            new_suggestions.append(
                {'Missing SEO Technique': sug_key, 'Comments': sug_value['comments'], 'Data': sug_value['data'],
                 'SEO Rules': my_rule})

        self.seo = new_suggestions
        self.create_csv(['Missing SEO Technique', 'Comments', 'Data', 'SEO Rules'])
