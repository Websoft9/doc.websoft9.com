from contentful import Client
from jinja2 import Environment, FileSystemLoader
import os
import argparse

# 解析命令行参数
parser = argparse.ArgumentParser(description='Generate Markdown files from Contentful entries based on a template file.')
parser.add_argument('template_file', help='The template file to use for generating the Markdown files.')
args = parser.parse_args()

# 设置 Jinja2 模板环境
TEMPLATE_DIR = 'docs/apps/_include'
TEMPLATE_FILE = args.template_file
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_FILE)

# 根据模板文件名判断使用的语言
locale = 'zh-CN' if 'zh' in TEMPLATE_FILE else 'en-US'

CONTENTFUL_SPACE_ID = "ffrhttfighww"
# CONTENTFUL_ACCESS_TOKEN = os.environ['CONTENTFUL_ACCESS_TOKEN']
CONTENTFUL_ACCESS_TOKEN = "BZz6LDz-PeMhqiWhd9zElh1lKz-TxZC5Gdk-oB1JdOA"

# 创建 Contentful 客户端实例
client = Client(CONTENTFUL_SPACE_ID, CONTENTFUL_ACCESS_TOKEN)

# 设置查询数据
content_type_id = 'product'
# entries = client.entries({'content_type': content_type_id})
entries = client.entries({
    'locale': locale,
    'content_type': content_type_id,
    'select': 'fields.key,fields.catalog,fields.license,fields.trademark,fields.overview,fields.summary,fields.websiteurl,fields.screenshots'
})

# 设置 Markdown 文件的输出目录
OUTPUT_DIR = 'output/markdown_files'

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 使用 Jinja2 模板和从 Contentful 获取的数据生成 Markdown 文件
for entry in entries:
    # 调用 fields() 方法来获取字段的字典
    fields = entry.fields(ocale=locale)

    # 解析 catalog 引用字段
    if 'catalog' in fields:
        catalog_items = []
        for catalog_link in fields['catalog']:
            # 获取整个entry
             catalog_entry = client.entries({
                'sys.id': catalog_link.sys['id'],
                'locale': locale
            })[0]
            # 从entry的fields中获取title字段
            catalog_fields = catalog_entry.fields()
            title = catalog_fields.get('title', None)
            # 将title添加到catalog_items列表中
            catalog_items.append({'title': title})
        fields['catalog'] = catalog_items

    # 解析 license 引用字段
    if 'license' in fields:
        # 获取整个entry
        license_entry = client.entries({
            'sys.id': fields['license'].sys['id'],
            'locale': locale
        })[0]
        # 从entry的fields中获取name和url字段
        license_fields = license_entry.fields()
        name = license_fields.get('name', None)
        url = license_fields.get('url', None)
        # 将name和url添加到fields中
        fields['license'] = {'name': name, 'url': url}

    print(fields)
    
    # 获取 trademark 作为文件名
    trademark = fields.get('trademark', entry.sys['id'])
    md_filename = f"{trademark}.md"
    
    # 完整的文件路径
    md_file_path = os.path.join(OUTPUT_DIR, md_filename)
    
    # 渲染模板，直接传递 fields 字典给模板
    rendered_content = template.render(**fields)
    
    # 将渲染后的内容写入 Markdown 文件
    with open(md_file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(rendered_content)


print("Markdown files have been created.")
