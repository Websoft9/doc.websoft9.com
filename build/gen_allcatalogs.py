import json
import argparse

# 设置命令行参数
parser = argparse.ArgumentParser(description='Convert JSON to Markdown.')
parser.add_argument('--json_file', type=str, help='Path to the JSON file', required=True)
parser.add_argument('--output_file', type=str, help='Path to the output Markdown file', required=True)

# 解析命令行参数
args = parser.parse_args()

# 读取JSON文件
with open(args.json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 用于存储Markdown内容的字符串
markdown_content = ""

# 对整个data列表按照每个item的position排序，如果position为None则默认为0
data_sorted = sorted(data, key=lambda x: x.get('position') if x.get('position') is not None else 0)

# 遍历JSON数据，生成Markdown内容
for item in data:
    title = item.get('title', '')
    linked_items = item.get('linkedFrom', {}).get('catalogCollection', {}).get('items', [])
    
    # 添加主标题
    markdown_content += f"## {title}\n\n"
    
    # 对linked_items按照position排序
    linked_items_sorted = sorted(linked_items, key=lambda x: x.get('position') if x.get('position') is not None else 0)
    
    # 遍历每个linked item并添加到Markdown内容中
    for linked_item in linked_items_sorted:
        linked_title = linked_item.get('title', '')
        linked_key = linked_item.get('key', '')
        markdown_content += f"- [{linked_title}](https://www.websoft9.com/apps/{linked_key})\n"

# 写入Markdown文件
with open(args.output_file, 'w', encoding='utf-8') as md_file:
    md_file.write(markdown_content)

print(f'Markdown file has been created successfully at {args.output_file}.')
