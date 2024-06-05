from contentful import Client
from jinja2 import Environment, FileSystemLoader
import os
import argparse

# 解析命令行参数
parser = argparse.ArgumentParser(description='Generate Markdown files from Contentful entries based on a template file.')
parser.add_argument('template_file', help='The template file to use for generating the Markdown files.')
args = parser.parse_args()

# 设置 Jinja2 模板环境
TEMPLATE_DIR = os.path.dirname(args.template_file)
TEMPLATE_FILE = os.path.basename(args.template_file)
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template(TEMPLATE_FILE)

# 根据模板文件名判断使用的语言
locale = 'zh-CN' if 'zh' in TEMPLATE_FILE else 'en-US'

# 设置 Markdown 文件的输出目录
if locale == 'zh-CN':
    OUTPUT_DIR = 'docs/apps/_include'
else:
    OUTPUT_DIR = 'i18n/en/docusaurus-plugin-content-docs/current/apps/_include'

CONTENTFUL_SPACE_ID = "ffrhttfighww"
CONTENTFUL_ACCESS_TOKEN = os.environ['CONTENTFUL_ACCESS_TOKEN']

# 创建 Contentful 客户端实例
client = Client(CONTENTFUL_SPACE_ID, CONTENTFUL_ACCESS_TOKEN)

# 设置每页条目数和初始跳过条目数
limit = 100
skip = 0

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 计数器
count = 0

# 循环直到获取所有条目
while True:
    # 获取分页数据
    entries = client.entries({
        'locale': locale,
        'content_type': 'product',
        'select': 'fields.key,fields.catalog,fields.license,fields.trademark,fields.overview,fields.summary,fields.websiteurl,fields.screenshots',
        'limit': limit,
        'skip': skip
    })

    # 如果没有更多的条目，跳出循环
    if not entries:
        break

    for entry in entries:
        count += 1
        # 调用 fields() 方法来获取字段的字典
        fields = entry.fields(locale=locale)

        # 解析 catalog 引用字段
        if 'catalog' in fields:
            catalog_items = []
            for catalog_link in fields['catalog']:
                catalog_entry = client.entries({
                    'sys.id': catalog_link.sys['id'],
                    'locale': locale
                })[0]
                catalog_fields = catalog_entry.fields()
                title = catalog_fields.get('title', None)
                catalog_items.append({'title': title})
            fields['catalog'] = catalog_items

        # 解析 license 引用字段
        if 'license' in fields:
            license_entry = client.entries({
                'sys.id': fields['license'].sys['id'],
                'locale': locale
            })[0]
            license_fields = license_entry.fields()
            key = license_fields.get('key', None)
            url = license_fields.get('url', None)
            fields['license'] = {'key': key, 'url': url}
        
        # 打印当前记录条数和字段
        print(f"count {count}: {fields}")
        
        # 获取 key 作为文件名
        key = fields.get('key', entry.sys['id'])
        md_filename = f"{key}.md"
        
        # 完整的文件路径
        md_file_path = os.path.join(OUTPUT_DIR, md_filename)
        
        # 渲染模板，直接传递 fields 字典给模板
        rendered_content = template.render(**fields)
        
        # 将渲染后的内容写入 Markdown 文件
        with open(md_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(rendered_content)

    # 更新 skip 以获取下一页条目
    skip += limit

print("Markdown files have been created.")
