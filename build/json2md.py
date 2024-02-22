import json
import sys

# The first command-line argument is the path to the JSON file
json_file_path = sys.argv[1]
# The second command-line argument is the output Markdown file name
output_md_file_name = sys.argv[2]

# Define the fixed content for both languages
fixed_content_zh = (
    "# 应用\n\n"
    "我们提供了数百个热门开源应用的自动化部署包，请点击下面的类目详细了解。\n\n"
    "如果您期望的应用不在类目中，欢迎给我们反馈。如果您是优质应用供应商，"
    "欢迎[加入](http://www.websoft9.com)到我们的目录中来。\n\n"
)

fixed_content_en = (
    "# Apps\n\n"
    "Docs of hundreds of pre-packaged apps below\n\n"
)

# Check the language from the file name or another indicator
if 'zh' in output_md_file_name:
    fixed_content = fixed_content_zh
else:  # Default to English if 'zh' is not found
    fixed_content = fixed_content_en

# Load the JSON data
with open(json_file_path) as json_file:
    data = json.load(json_file)

# Create a dictionary to hold the titles and their corresponding keys, trademarks, and positions
catalog_dict = {}

# Traverse the JSON data to fill the dictionary
for entry in data:
    try:
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
    except Exception as e:
        print(f"Error processing entry: {entry.get('key', 'Unknown')}")
        print(e)

# Now, generate the Markdown content sorted by position in ascending order
markdown_content = ""  

# 首先检查每个条目的positions是否会导致排序出错
for title, info in catalog_dict.items():
    try:
        # 尝试获取每个条目的最小positions值
        _ = min(info['positions'])
    except Exception as e:
        # 如果出错，打印出错的title和错误信息
        print(f"Error with title '{title}': {e}")
        # 可以选择跳过出错的条目或者停止处理
        break  # 或者使用continue来跳过当前条目

# 如果上面没有错误发生，或者你决定忽略错误继续执行，可以进行排序
try:
    sorted_items = sorted(catalog_dict.items(), key=lambda x: min(x[1]['positions']))
except Exception as e:
    # 如果排序时发生异常，这里只是额外的保障，理论上应该不会到达这里
    print(f"Error sorting the catalog: {e}")
else:
    # 如果排序成功，则继续生成Markdown内容
    for title, info in sorted_items:
        markdown_content += f"## {title}\n\n"
        for trademark, key in sorted(info['entries']):
            markdown_content += f"- [{trademark}](./{key})\n\n"


# Write the Markdown content to the specified output file
with open(output_md_file_name, 'w') as md_file:
    md_file.write(fixed_content + markdown_content)
