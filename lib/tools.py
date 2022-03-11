import csv


def write_rows_to_csv(rows, csv_file, fieldheader):
    with open(csv_file, "w", encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldheader)
        writer.writeheader()
        writer.writerows(rows)
    return


# Special Character             Hex     Decimal
# Dollar (“$”)	                24	    36
# Ampersand (“&”)	            26	    38
# Plus (“+”)	                2B	    43
# Comma (“,”)	                2C	    44
# Forward slash/Virgule (“/”)	2F	    47
# Colon (“:”)	                3A	    58
# Semi-colon (“;”)	            3B	    59
# Equals (“=”)	                3D	    61
# Question mark (“?”)	        3F	    63
# ‘At’ symbol (“@”)	            40	    64
# See: https://secure.n-able.com/webhelp/nc_9-1-0_so_en/content/sa_docs/api_level_integration/api_integration_urlencoding.html


def process_special_character(title):
    return (
        title.replace("$", "%24")
        .replace("&", "%26")
        .replace("+", "%2B")
        .replace(",", "%2C")
        .replace("/", "%2F")
        .replace(":", "%3A")
        .replace(";", "%3B")
        .replace("=", "%3D")
        .replace("?", "%3F")
        .replace("@", "%40")
    )
