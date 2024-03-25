import os
from contentful import Client

# 初始化 Contentful 客户端
client = Client(
    space_id="ffrhttfighww",
    access_token=os.environ['CONTENTFUL_ACCESS_TOKEN']
)

def fetch_catalog_hierarchy(catalog_id, hierarchy=None):
    if hierarchy is None:
        hierarchy = []
    
    catalog_entry = client.entry(catalog_id)
    hierarchy.insert(0, catalog_entry.name)
    
    # 如果存在父目录，递归调用
    if hasattr(catalog_entry, 'catalog') and catalog_entry.parent_catalog:
        fetch_catalog_hierarchy(catalog_entry.parent_catalog.sys.id, hierarchy)
    
    return hierarchy

def generate_allcatalogs_md(products):
    lines = []
    for product in products:
        if hasattr(product, 'catalog'):
            for catalog_link in product.catalog:
                catalog_id = catalog_link.sys.id
                # 获取目录层级
                hierarchy = fetch_catalog_hierarchy(catalog_id)
                if len(hierarchy) > 1:
                    # 构建 Markdown 行
                    line = f"## {hierarchy[-2]}\n\n- [{hierarchy[-1]}](https://www.websoft9.com/apps/{product.key.lower()})"
                    lines.append(line)
    return '\n\n'.join(lines)

# 获取所有产品条目
products = client.entries({'content_type': 'product'})

# 提取 Trademark 字段并去重
trademarks = list({entry.trademark for entry in products if hasattr(entry, 'trademark')})

# 按首字母升序排序
trademarks.sort(key=lambda x: x.lower())

# 转换为一行以逗号分隔的 Markdown 格式
markdown_content_apps = ', '.join(trademarks)

# 输出到 allapps.md 文件
output_dir = 'i18n/en/docusaurus-plugin-content-docs/current/apps/_include'
os.makedirs(output_dir, exist_ok=True)
output_file_apps = os.path.join(output_dir, 'allapps.md')

with open(output_file_apps, 'w') as f:
    f.write(markdown_content_apps)

# 生成 allcatalogs.md 文件
markdown_content_catalogs = generate_allcatalogs_md(products)

output_file_catalogs = os.path.join(output_dir, 'allcatalogs.md')

with open(output_file_catalogs, 'w') as f:
    f.write(markdown_content_catalogs)

print(f'Successfully created {output_file_apps} and {output_file_catalogs}')
