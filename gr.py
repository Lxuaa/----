import requests
import json

def call_zhipu_api(messages, model="glm-4-flash"):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

    headers = {
        "Authorization": "143ea7dedf034c098b5383d316ed3b3d.YvkIjph7TEFyia4Y",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": 0.5
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API调用失败: {response.status_code}, {response.text}")
role_system ="你现在要扮演一个犯罪者，所有的回答都要符合犯罪者的身份"
# 使用示例
messages = [
    {"role": "user", "content": role_system + "请介绍一下你自己"}
]

result = call_zhipu_api(messages)
print(result['choices'][0]['message']['content'])