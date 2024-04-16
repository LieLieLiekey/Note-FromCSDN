from bs4 import BeautifulSoup
import os, json

file_path = 'xxx.html'

# 从文件中读取 HTML 数据
with open(file_path, 'r', encoding='utf-8') as file:
    html_data = file.read()


# 解析 HTML
soup = BeautifulSoup(html_data, 'html.parser')

# 寻找所有的<li>标签
categories = soup.find_all('li')


res = []
# 遍历每个<li>标签，提取分类名称和链接
for category in categories:
    a_tag = category.find('a', class_='clearfix special-column-name')
    if a_tag:
        category_name = a_tag.find('span', class_='title oneline').text.strip()
        category_link = a_tag['href']
        res.append((category_name, category_link))

with open('link_map.json', 'w', encoding='utf-8') as file:
    json.dump(res, file, ensure_ascii=False, indent=4)
