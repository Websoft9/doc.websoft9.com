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
        f_apps.write(', '.join(trademark for trademark in trademarks if trademark))  # 过滤掉None值


def get_catalog_info(product):
    catalogs = []
    for catalog_link in product.fields().get('catalog', []):
        catalog_entry = catalog_link
        if catalog_entry:
            catalog_title = catalog_entry.fields().get('title')
            parent_catalog_entry = catalog_entry.fields().get('catalog')
            parent_catalog_title = parent_catalog_entry.fields().get('title') if parent_catalog_entry else None
            catalogs.append((parent_catalog_title, catalog_title))
    return catalogs

def generate_allcatalogs_files(products_with_catalogs, lang):
    # 构建目录和产品的映射关系
    catalog_product_map = {}
    for product in products_with_catalogs:
        # 获取产品的目录信息
        catalogs = get_catalog_info(product)
        for parent_catalog, catalog in catalogs:
            if parent_catalog not in catalog_product_map:
                catalog_product_map[parent_catalog] = {}
            if catalog not in catalog_product_map[parent_catalog]:
                catalog_product_map[parent_catalog][catalog] = []
            catalog_product_map[parent_catalog][catalog].append(product)

    # 根据语言设置输出文件路径
    if lang == 'zh-CN':
        catalogs_filepath = os.path.join('docs', 'apps', '_include', 'allcatalogs.md')
    elif lang == 'en-US':
        catalogs_filepath = os.path.join('i18n', 'en', 'docusaurus-plugin-content-docs', 'current', 'apps', '_include', 'allcatalogs.md')
    else:
        raise ValueError(f"Unsupported language: {lang}")

    # 确保输出目录存在
    os.makedirs(os.path.dirname(catalogs_filepath), exist_ok=True)

    # 生成Markdown文件
    with open(catalogs_filepath, 'w', encoding='utf-8') as f_catalogs:
        for parent_catalog, subcatalogs in catalog_product_map.items():
            if parent_catalog:  # Skip if the parent catalog is None or empty
                f_catalogs.write(f"## {parent_catalog}\n\n")
            for catalog, products in subcatalogs.items():
                f_catalogs.write(f"### {catalog}\n\n")
                for product in products:
                    key = product.fields().get('key')
                    title = product.fields().get('name')  # Assuming 'name' is the field for product name
                    f_catalogs.write(f"- [{title}](https://www.websoft9.com/apps/{key})\n")
                f_catalogs.write("\n")  # Add an extra newline for spacing

products_zh = fetch_all_products('zh-CN')
# generate_markdown_files(products_zh, 'zh-CN')

products_en = fetch_all_products('en-US')
# generate_markdown_files(products_en, 'en-US')

generate_allcatalogs_files(products_zh, 'zh-CN')
generate_allcatalogs_files(products_en, 'en-US')
