from lib.research_paper import Research_Paper
import csv
from lib.tools import process_special_character, write_rows_to_csv
from lib.variables import DATA_INPUT_DIR, DATA_OUTPUT_DIR

research_paper = Research_Paper()


def main():
    a = research_paper.get_doi_from_title(
        "Deep-learning-based burned area mapping using the synergy of Sentinel-1%262 data"
    )
    print(a)
    return


def add_doi_json(csv_file, output_file):
    all_rows = []
    header = []
    count = 0
    with open(csv_file, "r") as file:
        csvreader = csv.reader(file)
        header = next(csvreader)  # header
        for csv_row in csvreader:
            title = str(csv_row[2])
            title = process_special_character(title)
            json_data = research_paper.get_json_from_title(title)
            doi = research_paper.get_doi_from_json(json_data)
            research_paper.add_title_json(doi, json_data)
            row = {}
            for i in range(len(header)):
                row[header[i]] = csv_row[i]
            row["DOI"] = str(doi)
            all_rows.append(row)
            count += 1
            print(count)
    header.append("DOI")
    write_rows_to_csv(all_rows, output_file, header)
    research_paper.dump_titles_jsons_file()
    return


def add_doi_authors_year_volume_page(csv_file, output_file):
    all_rows = []
    header = []
    count = 0
    with open(csv_file, "r") as file:
        csvreader = csv.reader(file)
        header = next(csvreader)  # header
        for csv_row in csvreader:
            title = process_special_character(str(csv_row[2]))
            json_data = research_paper.get_json_from_title(title)
            doi = research_paper.get_doi_from_json(json_data)
            str_authors = research_paper.get_str_authors_from_json(json_data)
            year = research_paper.get_year_from_json(json_data)
            volume = research_paper.get_volume_from_json(json_data)
            page = research_paper.get_volume_from_json(json_data)
            research_paper.add_title_json(doi, json_data)
            row = {}
            for i in range(len(header)):
                row[header[i]] = csv_row[i]
            row["DOI"] = str(doi)
            row["Authors"] = str_authors
            row["Year"] = year
            row["Volume"] = volume
            row["Page"] = page
            all_rows.append(row)
            count += 1
            print(count)
    header.append("DOI")
    header.append("Authors")
    header.append("Year")
    header.append("Volume")
    header.append("Page")
    write_rows_to_csv(all_rows, output_file, header)
    research_paper.dump_titles_jsons_file()
    return


if __name__ == "__main__":
    # main()
    # add_doi_json(
    #    DATA_INPUT_DIR + "mailing list-Augmented.csv",
    #    DATA_OUTPUT_DIR + "mailing list-doi.csv",
    # )
    add_doi_authors_year_volume_page(
        DATA_INPUT_DIR + "mailing list-Augmented.csv",
        DATA_OUTPUT_DIR + "mailing list-doi_authors.csv",
    )
    print("Done!")
