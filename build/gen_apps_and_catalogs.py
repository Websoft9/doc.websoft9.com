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
    limit = 100

    while True:
        response = client.entries({
            'content_type': 'product',
            'skip': skip,
            'limit': limit,
            'locale': locale
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

# 获取所有产品，指定中文版本
products_zh = fetch_all_products('zh-CN')

# 获取所有产品，指定英文版本
products_en = fetch_all_products('en-US')
