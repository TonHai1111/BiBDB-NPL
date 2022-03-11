import requests as rq
import json

from lib.variables import (
    CROSSREF_ORG_API,
    SEARCH_ON_TITLE,
    TITLE_JSON_OUTPUT,
)


class Research_Paper:
    def __init__(self):
        self.__host = CROSSREF_ORG_API
        self.__all_titles_jsons = {}
        self.__limit_rows = 5

    def set_limit_rows(self, value):
        self.__limit_rows = value

    def get_doi_from_title(self, title):
        data = self.get_json_from_title(title)
        try:
            doi = str(data["message"]["items"][0]["DOI"])
        except KeyError as k:
            doi = ""
            print("KeyError: " + str(k))
        except TypeError as t:
            doi = ""
            print("TypeError: " + str(t))
        return doi

    def get_json_from_title(self, title):
        url = (
            self.__host
            + SEARCH_ON_TITLE
            + "="
            + str(title)
            + "&rows="
            + str(self.__limit_rows)
        )
        result = rq.get(url).text
        data = json.loads(result)
        return data

    def get_doi_from_json(self, json_data):
        try:
            doi = str(json_data["message"]["items"][0]["DOI"])
        except KeyError as k:
            doi = ""
            print("KeyError: " + str(k))
        except TypeError as t:
            doi = ""
            print("TypeError: " + str(t))
        return doi

    def get_authors_from_json(self, json_data):
        try:
            authors = json_data["message"]["items"][0]["author"]
        except KeyError as k:
            authors = []
            print("KeyError: " + str(k))
        except TypeError as t:
            authors = []
            print("TypeError: " + str(t))
        return authors

    def get_str_authors_from_json(self, json_data):
        output = ""
        array_authors = self.get_authors_from_json(json_data)
        for i in range(len(array_authors)):
            author = array_authors[i]
            if output != "":
                output += "; "
            output += self.__extract_author_name(author)
        return output

    def get_year_from_json(self, json_data):
        try:
            year = str(
                json_data["message"]["items"][0]["published-print"]["date-parts"][0][0]
            )
        except KeyError as k:
            year = ""
            print("KeyError: " + str(k))
        except TypeError as t:
            year = ""
            print("TypeError: " + str(t))
        return year

    def get_title_from_json(self, json_data):
        try:
            title = str(json_data["message"]["items"][0]["title"][0])
        except KeyError as k:
            title = ""
            print("KeyError: " + str(k))
        except TypeError as t:
            title = ""
            print("TypeError: " + str(t))
        return title

    def get_volume_from_json(self, json_data):
        try:
            volume = str(json_data["message"]["items"][0]["volume"])
        except KeyError as k:
            volume = ""
            print("KeyError: " + str(k))
        except TypeError as t:
            volume = ""
            print("TypeError: " + str(t))
        return volume

    def get_page_from_json(self, json_data):
        try:
            page = str(json_data["message"]["items"][0]["page"])
        except KeyError as k:
            page = ""
            print("KeyError: " + str(k))
        except TypeError as t:
            page = ""
            print("TypeError: " + str(t))
        return page

    def add_title_json(self, title, data_json):
        self.__all_titles_jsons[title] = data_json

    def dump_titles_jsons_file(self, filename=TITLE_JSON_OUTPUT):
        with open(filename, "w") as file:
            json.dump(self.__all_titles_jsons, file)

    # Private methods
    def __extract_author_name(self, author):
        author_name = ""
        if "family" in author:
            author_name += str(author["family"])
        if "given" in author:
            if author_name != "":
                author_name += ", "
            author_name += str(author["given"])
        if "name" in author:
            author_name = str(author["name"])
        return author_name
