# 确保导入路径正确，并且处理可能的模块加载问题
try:
    from chat import start_chat
except ImportError as e:
    print(f"导入 chat 模块失败: {e}")
    print("请检查 chat.py 是否存在，且文件名正确（小写chat.py）")
    exit(1)

if __name__ == "__main__":
    # 启动对话，默认角色是“妹妹”
    try:
        start_chat(role_name="妹妹")
    except Exception as e:
        print(f"启动对话时发生错误: {e}")