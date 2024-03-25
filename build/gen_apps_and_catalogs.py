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
            'select': 'fields.key,fields.trademark,fields.catalog',
            'fields.production': 'yes',
            'fields.appStore': 'yes',
            'include': 2
        })
        products.extend(response.items)
        if len(response.items) < limit:
            break
        skip += limit
    return products


def generate_markdown_files(products,lang):
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


def generate_catalog_markdown_files(products, lang):
    # 根据语言设置输出文件路径
    if lang == 'zh-CN':
        catalogs_dirpath = os.path.join('docs', 'catalogs', '_include')
    elif lang == 'en-US':
        catalogs_dirpath = os.path.join('i18n', 'en', 'docusaurus-plugin-content-docs', 'current', 'catalogs', '_include')
    else:
        raise ValueError(f"Unsupported language: {lang}")

    # 确保输出目录存在
    os.makedirs(catalogs_dirpath, exist_ok=True)

    # 文件名统一为allcatalogs.md
    catalogs_filepath = os.path.join(catalogs_dirpath, 'allcatalogs.md')

    # 组织catalog数据结构
    catalog_structure = {}
    for product in products:
        product_fields = product.fields()
        key = product_fields.get('key')
        for catalog_entry in product_fields.get('catalog', []):
            catalog_fields = catalog_entry.fields()
            base_catalog = catalog_fields.get('catalog')
            if base_catalog:
                base_catalog_fields = base_catalog.fields()
                category = base_catalog_fields.get('catalog')
                title = base_catalog_fields.get('title')

                if category not in catalog_structure:
                    catalog_structure[category] = []
                catalog_structure[category].append((title, key))

    # 写入Markdown文件
    with open(catalogs_filepath, 'w', encoding='utf-8') as f_catalogs:
        for category, items in catalog_structure.items():
            f_catalogs.write(f"## {category}\n\n")
            for title, key in items:
                f_catalogs.write(f"- [{title}](https://www.websoft9.com/apps/{key})\n\n")

products_zh = fetch_all_products('zh-CN')
generate_markdown_files(products_zh, 'zh-CN')
generate_catalog_markdown_files(products_zh, 'zh-CN')

products_en = fetch_all_products('en-US')
generate_markdown_files(products_en, 'en-US')
generate_catalog_markdown_files(products_en, 'en-US')
