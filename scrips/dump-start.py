import json
import os
import subprocess

def get_two_num(num):
    # 使用格式化字符串来确保数字是两位数，前导零补齐
    return f"{num:02d}"
def process(name, link,index):
    # 创建目录，exist_ok=True 使得如果目录已存在则不会抛出异常
    dir_name = get_two_num(index) + "-" + name
    os.makedirs(dir_name, exist_ok=True)
    print(f"创建目录: {dir_name}")

    # 构建执行的命令
    command = [
        'python', '-u', '/Users/bytedance/python-repo/CSDNExporter/main.py',
        '--category_url', link,
        '--start_page', '1',
        '--page_num', '100',
        '--markdown_dir', "./",
        '--combine_together'
    ]

    # 切换到新创建的目录中执行命令
    subprocess.run(command, cwd=dir_name)
def read_json_file(file_path):
    """从 JSON 文件读取数据"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def read_text_file(file_path):
    """从文本文件读取数据，每行一个数据, 返回 Set """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        return set()  # 如果文件不存在，返回空集合

def append_to_text_file(file_path, text):
    """向文本文件末尾添加文本"""
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(text + '\n')

def main():
    # 从 JSON 文件读取所有需要处理的数据
    all_entries = read_json_file('link_map.json')

    # 从文本文件读取已完成的数据
    finished_entries = read_text_file('finish_line.txt')

    # 确定还需处理的数据
    index = 0
    need_to_process = []
    for entry in all_entries:
        index += 1
        name = entry[0]
        if name in finished_entries:
            print("SKIP, name: {}, link: {}".format(name, entry[1]))
            continue
        entry.append(index)
        need_to_process.append(entry)

    # 处理未完成的数
    for entry in need_to_process:
        name = entry[0]
        link = entry[1]
        index = entry[2]
        print(f"正在处理: {name} - {link}")
        process(name,link,index)
        # 将处理完成的条目追加到文件
        append_to_text_file('finish_line.txt', name)
        print(f"已完成: {name} - {link}")

if __name__ == '__main__':
    main()




# 示例调用
# process('example_directory', 'https://example.com/link_to_category')
