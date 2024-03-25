import json
import argparse

# 设置命令行参数
parser = argparse.ArgumentParser(description='Convert JSON to Markdown.')
parser.add_argument('--json_file', type=str, help='Path to the JSON file', required=True)
parser.add_argument('--output_file', type=str, help='Path to the output Markdown file', required=True)

# 解析命令行参数
args = parser.parse_args()

# 读取JSON文件
with open(args.json_file, 'r', encoding='utf-8') as file:
    apps = json.load(file)

# 提取每个app的trademark，并按照字母升序排序
trademarks = sorted(app['trademark'] for app in apps if app['trademark'] is not None)

# 将排序后的trademarks转换为字符串，并用逗号隔开
trademarks_str = ', '.join(trademarks)

# 将结果写入Markdown文件
try:
    with open(args.output_file, 'w') as file:
        file.write(trademarks_str + '\n')
except IOError as e:
    print(f"Error: Could not write to file {args.output_file}: {e}")
    sys.exit(1)

print(f'The {args.output_file} file has been created with sorted trademarks.')
