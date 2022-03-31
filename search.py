import configparser
from fuzzywuzzy import process

parser = configparser.ConfigParser()
intermediate_result = []
with open("cricket.ini","r") as file:
    parser.read_file(file)
    sect = parser.sections()
    country = input("Please enter your desired Cricketing Country : ")
    search_query = input("Please enter the search term: ")
    for k,v in parser.items(sect[0]):
        if v == country:
            intermediate_result.append(k)


semi_final_data = process.extract(search_query,intermediate_result)
print(f"Search Results for {search_query} ({len(semi_final_data)}) :")
for i,name in enumerate(dict(semi_final_data).keys()):
    print(f"{i+1}. {name}")
