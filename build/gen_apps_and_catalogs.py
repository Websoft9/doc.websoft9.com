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

    print("产品数量："+str(len(products)))

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

products_zh = fetch_all_products('zh-CN')
# generate_markdown_files(products_zh, 'zh-CN')

products_en = fetch_all_products('en-US')
# generate_markdown_files(products_en, 'en-US')
