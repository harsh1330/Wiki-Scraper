import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import defaultdict
import re
import unicodedata


class BusinessLogicService():

    def do_some_logical_ops(self, country_name):
        def clean_text(string):
            string = re.sub("\(.*?\)", "", string)
            string = re.sub("\[.*?\]", "", string)
            return unicodedata.normalize("NFKD", string)

        result = defaultdict(list)
        url = f'https://en.wikipedia.org/wiki/{country_name}'
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        my_table = soup.find('table', {'class': 'infobox ib-country vcard'})
        counter = 1
        next_is_area_total = False
        next_is_GDP_total = 0
        next_is_P_total = 0
        country_name_div = soup.find('div', {'class': 'fn org country-name'})
        if country_name_div.string:
            result["country_name"] = country_name_div.string
        else:
            country_name_div = soup.find('span', {'lang': 'en'}).text
            country_name_div = str(country_name_div)
            result["country_name"] = country_name_div

        flag_link_td = soup.find('td', {'class': 'infobox-image'})

        result["flag_link"] = "https:"+flag_link_td.find('img')["src"]
        h2 = ""

        makeshift = {}

        for row in my_table.find_all('tr'):
            header = row.find_all('th')
            cells = row.find_all('td')

            if header:
                h = clean_text(str(header[0].string))

                if next_is_area_total:

                    result["area_total"] = clean_text(cells[0].text)
                    next_is_area_total = False

                if h == "Area ":
                    next_is_area_total = True

                if next_is_GDP_total == 4:

                    result["GDP_nominal"] = clean_text(cells[0].text)

                if next_is_P_total == 1:
                    result["population"] = clean_text(cells[0].text)

                if header[0].find("a"):
                    h2 = clean_text(header[0].find("a").string)

                if h2 == "GDP":
                    next_is_GDP_total += 1

                if h2 == "Population":
                    next_is_P_total += 1

                if cells:

                    try:
                        for i in cells[0].find_all('li'):
                            if i.find('a'):

                                temp = i.find('a').string

                                result[h].append(temp)

                        if not result[h]:
                            if cells[0].find("a"):
                                result[h] = clean_text(
                                    cells[0].find("a").string)
                    except:
                        if h == "None":
                            makeshift = result["None"]

        if not result["Capital"] and not result["Largest city"]:
            result["Capital"] = makeshift
            result["Largest city"] = makeshift

        required_Keys = {'country_name', 'flag_link', 'Capital', 'Largest city',
                         'Official languages', 'area_total',  'population', 'GDP_nominal'}
        processed_data = {key.replace(" ", "_").lower(
        ): result[key] for key in required_Keys}
        return processed_data
