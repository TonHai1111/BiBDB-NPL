import requests as rq
import json

from lib.variables import (
    CROSSREF_ORG_API,
    SEARCH_ON_TITLE,
    TITLE_JSON_OUTPUT,
)


class Research_Paper:
    def __init__(self):
        self.host = CROSSREF_ORG_API
        self.all_titles_jsons = {}

    def get_doi_from_title(self, title):
        data = self.get_json_from_title(title)
        try:
            doi = str(data["message"]["items"][0]["DOI"])
        except KeyError:
            doi = ""
        except TypeError:
            doi = ""
        return doi

    def get_json_from_title(self, title):
        url = self.host + SEARCH_ON_TITLE + "=" + str(title)
        result = rq.get(url).text
        data = json.loads(result)
        return data

    def get_doi_from_json(self, json_data):
        try:
            doi = str(json_data["message"]["items"][0]["DOI"])
        except KeyError:
            doi = ""
        except TypeError:
            doi = ""
        return doi

    def get_authors_from_json(self, json_data):
        try:
            authors = str(json_data["message"]["items"][0]["DOI"])
        except KeyError:
            authors = ""
        except TypeError:
            authors = ""
        return authors

    def get_year_from_json(self, json_data):
        try:
            year = str(json_data["message"]["items"][0]["DOI"])
        except KeyError:
            year = ""
        except TypeError:
            year = ""
        return year

    def add_title_json(self, title, data_json):
        self.all_titles_jsons[title] = data_json

    def dump_titles_jsons_file(self, filename=TITLE_JSON_OUTPUT):
        with open(filename, "w") as file:
            json.dump(self.all_titles_jsons, file)
