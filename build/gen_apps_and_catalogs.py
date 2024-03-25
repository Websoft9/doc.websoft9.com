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
            'locale': locale,
            'select': 'fields.key,fields.catalog'
        })
        products.extend(response.items)
        if len(response.items) < limit:
            break
        skip += limit
    return products

def fetch_base_catalogs(locale):
    catalogs = {}
    skip = 0
    limit = 100

    while True:
        response = client.entries({
            'content_type': 'baseCatalog',
            'skip': skip,
            'limit': limit,
            'locale': locale
        })
        for item in response.items:
            catalogs[item.sys['id']] = {
                'title': item.fields().get('title'),
                'catalog': item.fields().get('catalog')
            }
        if len(response.items) < limit:
            break
        skip += limit
    return catalogs

def generate_markdown_files(products,catalogs,lang):
    # 根据语言设置输出文件路径
    if lang == 'zh-CN':
        apps_dirpath = os.path.join('docs', 'apps', '_include')
    elif lang == 'en-US':
        apps_dirpath = os.path.join('i18n', 'en', 'docusaurus-plugin-content-docs', 'current', 'apps', '_include')
    else:
        raise ValueError(f"Unsupported language: {lang}")

    # 确保输出目录存在
    os.makedirs(apps_dirpath, exist_ok=True)

    # 文件名统一为allapps.md
    apps_filepath = os.path.join(apps_dirpath, 'allapps.md')

    # 提取trademarks并根据首字母升序排序
    trademarks = sorted(
        (product.fields().get('trademark') for product in products),
        key=lambda x: ('',) if x is None else (x.upper(),)
    )
    
    # 生成apps文件
    with open(apps_filepath, 'w', encoding='utf-8') as f_apps:
        f_apps.write(', '.join(trademark for trademark in trademarks if trademark))

    catalogs_dirpath = apps_dirpath
    catalogs_filepath = os.path.join(catalogs_dirpath, 'allcatalogs.md')

    with open(catalogs_filepath, 'w', encoding='utf-8') as f_catalogs:
        for product in products:
            product_fields = product.fields()
            key = product_fields.get('key')
            product_catalogs = product_fields.get('catalog', [])
            for catalog_id in product_catalogs:
                catalog = catalogs.get(catalog_id, {})
                catalog_title = catalog.get('title')
                parent_catalog = catalog.get('catalog')
                if parent_catalog:
                    parent_catalog_title = catalogs[parent_catalog].get('title')
                    f_catalogs.write(f"## {parent_catalog_title}\n\n")
                    f_catalogs.write(f"- [{catalog_title}](https://www.websoft9.com/apps/{key})\n")


products_zh = fetch_all_products('zh-CN')
catalogs_zh = fetch_base_catalogs('zh-CN')
generate_markdown_files(products_zh, catalogs_zh, 'zh-CN')

products_en = fetch_all_products('en-US')
catalogs_en = fetch_base_catalogs('en-US')
generate_markdown_files(products_en, catalogs_en, 'en-US')
