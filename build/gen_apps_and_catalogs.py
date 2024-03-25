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
        apps_filepath = os.path.join('docs', 'apps', '_include', f'allapps_{lang}.md')
    elif lang == 'en-US':
        apps_filepath = os.path.join('i18n', 'en', 'docusaurus-plugin-content-docs', 'current', 'apps', '_include', f'allapps_{lang}.md')
    else:
        raise ValueError(f"Unsupported language: {lang}")

    # 确保输出目录存在
    os.makedirs(os.path.dirname(apps_filepath), exist_ok=True)

    # 提取trademarks并根据首字母升序排序
    trademarks = sorted(
        (product.fields().get('trademark') for product in products),
        key=lambda x: ('',) if x is None else (x[0].upper(), x.lower())
    )

    # 生成apps文件
    with open(apps_filepath, 'w', encoding='utf-8') as f_apps:
        f_apps.write(', '.join(trademark for trademark in trademarks if trademark))  # 过滤掉None值


# 获取所有产品，指定中文版本
products_zh = fetch_all_products('zh-CN')
# 为中文产品生成 Markdown 文件
generate_markdown_files(products_zh, 'zh-CN')

# 获取所有产品，指定英文版本
products_en = fetch_all_products('en-US')
# 为英文产品生成 Markdown 文件
generate_markdown_files(products_en, 'en-US')

