import json
import urllib.request
import time

# https://rruntsch.medium.com/how-to-write-a-python-program-to-query-biomedical-journal-citations-in-the-pubmed-database-c7e842e4df89
# Query : GraphQL

class E_utility:

    def __init__(self):
        self.sleep_minute = .01
        self.base_url_esearch = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"
        self.base_url_efetch = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
        self.output_file_path = r"files/"

    def Search(self, search_term):
        url = self.base_url_esearch + 'db=pubmed&term=' + \
              search_term + "&retmode=json&retmax=20&usehistory=y"

        result = urllib.request.urlopen(url)
        text = result.read().decode('utf-8')

        json_text = json.loads(text)

        webenv = json_text["esearchresult"]["webenv"]
        for uid in json_text["esearchresult"]["idlist"]:
            self.Retrieve_Abstract(uid, webenv)

    def Retrieve_Abstract(self, uid, webenv):
        url = self.base_url_efetch + 'db=pubmed&xml=json&id=' + \
              uid + '&webenv=' + webenv

        result = urllib.request.urlopen(url)
        json_text = result.read().decode('utf-8')

        file_name = self.output_file_path + "pubmed_" + uid + ".xml"

        file_out = open(file_name, 'w', encoding="utf-8")
        file_out.write(json_text)
        file_out.close()

        time.sleep(self.sleep_minute)


util = E_utility()
util.Search("Thyroid%5BMeSH+Terms%5D")

# util.Search("Johns+Hopkins[ad]+heart[ti]+2020/12/1:2020/12/31[dp]")
