import json
import os

# 获取项目根目录（当前文件所在目录的父目录）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROLE_MEMORY_MAP = {
    "妹妹": "Liang_memory.json"
}

def load_role_memory(role_name):
    memory_content = ""
    memory_file = ROLE_MEMORY_MAP.get(role_name)
    if memory_file:
        # 从项目根目录读取记忆文件
        memory_path = os.path.join(BASE_DIR, memory_file)
        try:
            if os.path.exists(memory_path):
                with open(memory_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        contents = [item.get('content', '') for item in data if isinstance(item, dict) and item.get('content')]
                        memory_content = '\n'.join(contents)
                    elif isinstance(data, dict):
                        memory_content = data.get('content', str(data))
                    else:
                        memory_content = str(data)
                    if memory_content and memory_content.strip():
                        print(f"✓ 已加载角色 '{role_name}' 的记忆: {memory_file} ({len(data) if isinstance(data, list) else 1} 条记录)")
                return memory_content
            else:
                print(f"⚠ 记忆文件不存在: {memory_path}")
        except Exception as e:
            print(f"⚠ 加载记忆失败: {e}")
    return memory_content