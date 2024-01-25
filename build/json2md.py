import json
import sys

# The first command-line argument is the path to the JSON file
json_file_path = sys.argv[1]
# The second command-line argument is the output Markdown file name
output_md_file_name = sys.argv[2]

# Load the JSON data
with open(json_file_path) as json_file:
    data = json.load(json_file)

# Create a dictionary to hold the titles and their corresponding keys, trademarks, and positions
catalog_dict = {}

# Traverse the JSON data to fill the dictionary
for entry in data:
    parent_key = entry['key']  # This is the key for the parent item
    trademark = entry['trademark']
    items = entry['catalogCollection']['items']
    for item in items:
        # Check if the item has a 'catalogCollection' and process accordingly
        if 'catalogCollection' in item:
            subitems = item['catalogCollection']['items']
            for subitem in subitems:
                sub_title = subitem['title']
                position = subitem.get('position', 0)  # Use 0 as a default if position is not specified
                # Initialize the dictionary for this sub_title if it hasn't been added before
                if sub_title not in catalog_dict:
                    catalog_dict[sub_title] = {'positions': [], 'entries': set()}
                # Add position and the (trademark, parent_key) tuple to the dictionary for this sub_title
                catalog_dict[sub_title]['positions'].append(position)
                catalog_dict[sub_title]['entries'].add((trademark, parent_key))

# Now, generate the Markdown content sorted by position in ascending order
markdown_content = ""
for title, info in sorted(catalog_dict.items(), key=lambda x: min(x[1]['positions'])):
    markdown_content += f"## {title}\n\n"
    for trademark, key in sorted(info['entries']):
        markdown_content += f"- [{trademark}](/apps/{key})\n\n"

# Write the Markdown content to the specified output file
with open(output_md_file_name, 'w') as md_file:
    md_file.write(markdown_content)
