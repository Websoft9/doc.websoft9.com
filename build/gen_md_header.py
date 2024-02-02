from contentful import Client
from jinja2 import Environment, FileSystemLoader
import os

CONTENTFUL_SPACE_ID = "ffrhttfighww"
CONTENTFUL_ACCESS_TOKEN = os.environ['CONTENTFUL_ACCESS_TOKEN']

print(CONTENTFUL_ACCESS_TOKEN)

# 创建 Contentful 客户端实例
client = Client(CONTENTFUL_SPACE_ID, CONTENTFUL_ACCESS_TOKEN)

# 设置查询数据
content_type_id = 'product'
# entries = client.entries({'content_type': content_type_id})
entries = client.entries({'content_type': content_type_id, 'limit': 1})[0]

print(entries)

# 设置 Jinja2 模板环境
TEMPLATE_DIR = 'docs/apps/_include'
TEMPLATE_FILE = 'meta-zh.jinja2'
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_FILE)

# 设置 Markdown 文件的输出目录
OUTPUT_DIR = 'output/markdown_files'

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 使用 Jinja2 模板和从 Contentful 获取的数据生成 Markdown 文件
for entry in entries:
    # 获取 key 作为文件名
    key = entry.fields.get('key', entry.sys.id)
    md_filename = f"{key}.md"
    
    # 完整的文件路径
    md_file_path = os.path.join(OUTPUT_DIR, md_filename)
    
    # 渲染模板
    rendered_content = template.render(entry=entry)
    
    # 将渲染后的内容写入 Markdown 文件
    with open(md_file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(rendered_content)

print("Markdown files have been created.")
