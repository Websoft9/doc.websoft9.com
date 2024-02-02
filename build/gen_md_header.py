from contentful import Client
from jinja2 import Environment, FileSystemLoader
import os

CONTENTFUL_SPACE_ID = "ffrhttfighww"
CONTENTFUL_ACCESS_TOKEN = os.getenv('CONTENTFUL_TOKEN')

# 创建 Contentful 客户端实例
client = Client(CONTENTFUL_SPACE_ID, CONTENTFUL_ACCESS_TOKEN)

# 设置查询数据
content_type_id = 'product'
entries = client.entries({'content_type': content_type_id})

# 设置 Jinja2 模板环境
TEMPLATE_DIR = 'docs/apps/_include'
TEMPLATE_FILE = 'meta-zh.jinja2'
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_FILE)

# 使用 Jinja2 模板和从 Contentful 获取的数据生成 Markdown 文件
for entry in entries:
    # 你可以根据 entry 的 key 属性来创建文件名
    md_filename = f"{entry.key.replace(' ', '_')}.md"
    
    # 渲染模板
    rendered_content = template.render(entry=entry)
    
    # 将渲染后的内容写入 Markdown 文件
    with open(md_filename, 'w') as md_file:
        md_file.write(rendered_content)

print("Markdown files have been created.")
