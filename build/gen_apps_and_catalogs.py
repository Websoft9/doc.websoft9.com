import os
from contentful import Client

# 初始化 Contentful 客户端
client = Client(
    space_id="ffrhttfighww",
    access_token=os.environ['CONTENTFUL_ACCESS_TOKEN']
)

def fetch_all_products(locale):
    products = []
    skip = 0
    limit = 100  # Contentful API的最大条目限制，可以根据API文档调整

    while True:
        response = client.entries({
            'content_type': 'product',
            'skip': skip,
            'limit': limit,
            'locale': locale  # 指定语言版本
        })
        products.extend(response.items)
        if len(response.items) < limit:
            break
        skip += limit

    return products

def generate_markdown_files(products, lang):
    apps_filename = f'allapps_{lang}.md'
    catalog_filename = f'allcatalog_{lang}.md'

    # 生成apps文件
    with open(f'docs/apps/_include/{apps_filename}', 'w', encoding='utf-8') as f_apps, \
         open(f'i18n/en/docusaurus-plugin-content-docs/current/apps/_include/{apps_filename}', 'w', encoding='utf-8') as f_apps_en:
        
        trademarks = [product.fields().get('trademark') for product in products]
        f_apps.write(', '.join(trademarks))
        f_apps_en.write(', '.join(trademarks))

   # 生成catalog文件
    with open(f'docs/apps/_include/{catalog_filename}', 'w', encoding='utf-8') as f_catalog, \
         open(f'i18n/en/docusaurus-plugin-content-docs/current/apps/_include/{catalog_filename}', 'w', encoding='utf-8') as f_catalog_en:

        for product in products:
            catalog_entries = product.fields().get('catalog', [])
            for entry_id in catalog_entries:
                catalog = client.entry(entry_id, {'locale': lang})
                parent_catalog_id = catalog.fields().get('catalog')
                if parent_catalog_id:
                    parent_catalog = client.entry(parent_catalog_id, {'locale': lang})
                    f_catalog.write(f"## {parent_catalog.fields().get('title', '无标题')}\n")
                    f_catalog.write(f"- [{catalog.fields().get('title', '无标题')}](https://www.websoft9.com/apps/{product.fields().get('key', '无键')})\n")
                    
                    parent_catalog_en = client.entry(parent_catalog_id, {'locale': 'en-US'})
                    f_catalog_en.write(f"## {parent_catalog_en.fields().get('title', 'No Title')}\n")
                    f_catalog_en.write(f"- [{catalog.fields().get('title', 'No Title')}](https://www.websoft9.com/apps/{product.fields().get('key', 'no-key')})\n")

# 获取所有产品，指定中文版本
products_zh = fetch_all_products('zh-CN')
# 生成中文的Markdown文件
generate_markdown_files(products_zh, 'zh-CN')

# 获取所有产品，指定英文版本
products_en = fetch_all_products('en-US')
# 生成英文的Markdown文件
generate_markdown_files(products_en, 'en-US')
