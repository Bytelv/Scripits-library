import json
import requests

# 数据源链接
data_url = 'https://qexo.lvbyte.top/pub/friends/?token=071415'

# 使用requests获取JSON数据
response = requests.get(data_url)
if response.status_code == 200:
    source_data = response.json()

    # 转换函数
    def transform_data(data):
        return {
            "title": data["name"],
            "url": data["url"],
            "avatar": data["image"],
            "screenshot": "",  # 假设screenshot数据需要另外提供的情况
            "description": data["description"],
            # "keywords": "" # 如果原数据中没有keywords，可以添加自定义的关键字或留空
        }

    # 将原始数据转换为新格式
    transformed_content = [transform_data(item) for item in source_data['data']]

    # 创建新的JSON数据结构
    transformed_data = {
        "version": "v2",
        "content": transformed_content
    }

    # 将新的数据结构转换为JSON字符串并保存到文件
    with open('transformed_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(transformed_data, json_file, ensure_ascii=False, indent=4)

    print("数据转换成功，并已保存到文件 'transformed_data.json'")
else:
    print(f"获取数据失败，状态码：{response.status_code}")