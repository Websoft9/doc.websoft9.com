## cli sample: python3 create_app.py --appname alfresco --trademark Alfresco --i18n zh  ###

import argparse
import os
from jinja2 import Environment, FileSystemLoader

# 设置命令行参数
parser = argparse.ArgumentParser(description='Render Jinja2 templates with provided variables.')
parser.add_argument('--trademark', type=str, required=True, help='The trademark string')
parser.add_argument('--appname', type=str, required=True, help='The application name')
parser.add_argument('--i18n', type=str, choices=['en', 'zh'], required=True, help='Internationalization language selection')

# 解析命令行参数
args = parser.parse_args()

# 设置 Jinja2 环境
env = Environment(loader=FileSystemLoader('app'))

# 根据 --i18n 参数选择模板
template_file = 'zh.jinja2' if args.i18n == 'zh' else 'en.jinja2'
template = env.get_template(template_file)

# 渲染模板，传入参数
rendered_template = template.render(
    trademark=args.trademark,
    appname=args.appname
)

# 根据 --i18n 参数选择输出路径
output_path = '../docs/apps/' if args.i18n == 'zh' else '../i18n/en/docusaurus-plugin-content-docs/current/apps/'

# 创建输出目录，如果它不存在
os.makedirs(output_path, exist_ok=True)

# 输出文件的名称格式为 appname.md
output_file_name = f"{args.appname}.md"
output_file_path = os.path.join(output_path, output_file_name)

# 保存渲染后的内容到指定文件
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(rendered_template)

print(f"Template rendered and saved to {output_file_path}")
