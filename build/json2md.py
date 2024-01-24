import json
import sys

# The first command-line argument is the path to the JSON file
json_file_path = sys.argv[1]
# The second command-line argument is the output Markdown file name
output_md_file_name = sys.argv[2]

# Load the JSON data
with open(json_file_path) as json_file:
    data = json.load(json_file)

# Create a dictionary to hold the titles and their corresponding keys and trademarks
# and a set to keep track of added sub-titles to avoid duplicates
catalog_dict = {}
added_sub_titles = set()

# Traverse the JSON data to fill the dictionary
for entry in data:
    key = entry['key']
    trademark = entry['trademark']
    items = entry['catalogCollection']['items']
    for item in items:
        title = item['title']
        if 'catalogCollection' in item:
            subitems = item['catalogCollection']['items']
            for subitem in subitems:
                sub_title = subitem['title']
                # Only add the sub_title if it hasn't been added before
                if sub_title not in added_sub_titles:
                    added_sub_titles.add(sub_title)
                    if sub_title not in catalog_dict:
                        catalog_dict[sub_title] = []
                    catalog_dict[sub_title].append((trademark, key))

# Now, generate the Markdown content
markdown_content = ""
for title, pairs in catalog_dict.items():
    markdown_content += f"## {title}\n\n"
    for trademark, key in pairs:
        markdown_content += f"- [{trademark}](/apps/{key})\n\n"

# Write the Markdown content to the specified output file
with open(output_md_file_name, 'w') as md_file:
    md_file.write(markdown_content)
