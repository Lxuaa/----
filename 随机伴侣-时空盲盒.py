import streamlit as st
import random
import time

# 页面配置
st.set_page_config(page_title="随机唯一伴侣·时空盲盒", page_icon="🎁", layout="wide")
st.title("🎁 随机唯一伴侣·时空盲盒")
st.markdown("**主题：每个人只有1个随机匹配的知心伴侣——但TA可能在任何时空**")


# ---------------------- 1. 用户初始设置 ----------------------
st.sidebar.header("你的初始信息")
user_age = st.sidebar.slider("你的年龄", 10, 50, 20)
user_location = st.sidebar.selectbox("你所在的地区", ["小镇", "城市", "星际殖民地（未来）"])


# ---------------------- 2. 时空盲盒生成逻辑 ----------------------
def generate_soulmate_box():
    # 随机时空（覆盖古今未来+死亡状态）
    time_options = [
        ("公元前2000年·古埃及", "已离世"),
        ("公元1000年·北宋", "已离世"),
        ("1920年·民国", "已离世"),
        ("2025年·现代", "在世"),
        ("2150年·火星", "未出生"),
        ("3000年·银河联邦", "未出生")
    ]
    era, status = random.choice(time_options)
    
    # 随机年龄（贴合时空）
    if status == "在世":
        age = random.randint(user_age-10, user_age+10)
    else:
        age = random.randint(15, 40)  # 离世/未出生者的年龄
    
    # 随机特征（贴合时空）
    trait_map = {
        "公元前2000年·古埃及": "会画金字塔壁画",
        "公元1000年·北宋": "能写宋词小令",
        "1920年·民国": "擅长留声机维修",
        "2025年·现代": "收藏了50种奶茶配方",
        "2150年·火星": "能修太空舱供氧系统",
        "3000年·银河联邦": "会和外星植物对话"
    }
    trait = trait_map[era]
    
    return era, status, age, trait


# ---------------------- 3. 相遇概率计算（贴合原文逻辑） ----------------------
def calc_meet_prob(era, status, user_location):
    # 基础概率：时空+存活状态
    if status == "已离世" or status == "未出生":
        base_prob = 0.00001
        reason1 = "TA和你不在同一时空，相遇概率趋近于0"
    else:
        base_prob = 0.01  # 同年代基础概率
    
    # 地区修正：小镇接触的人更少
    if user_location == "小镇":
        base_prob *= 0.1
        reason2 = "你在小镇，一生接触的陌生人更少"
    else:
        reason2 = "你在城市/星际殖民地，接触的陌生人相对多"
    
    # 最终概率+原因
    final_prob = round(base_prob, 6)
    reasons = [reason1] if status != "在世" else [reason1, reason2]
    return final_prob, reasons


# ---------------------- 4. 互动逻辑：盲盒开箱 ----------------------
if st.button("🎲 开盲盒：抽取你的唯一伴侣", type="primary"):
    # 盲盒开箱动画
    with st.spinner("正在打开时空盲盒..."):
        time.sleep(2)
    
    # 生成伴侣信息
    era, status, sm_age, sm_trait = generate_soulmate_box()
    prob, prob_reasons = calc_meet_prob(era, status, user_location)
    
    # 展示盲盒结果（分栏可视化）
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("你的唯一伴侣信息")
        st.info(f"**时空**：{era}")
        st.warning(f"**状态**：{status}")
        st.success(f"**年龄**：{sm_age}岁")
        st.info(f"**专属技能**：{sm_trait}")
        
        # 概率展示（进度条+原因）
        st.subheader(f"相遇概率：{prob}%")
        st.progress(prob / 100)  # Streamlit进度条范围0-1
        st.markdown("**概率低的原因：**")
        for r in prob_reasons:
            st.caption(f"→ {r}")
    
    with col2:
        st.subheader("跨时空“无效互动”")
        # 不同状态的互动内容（贴合原文“孤独/伪装”）
        if status == "已离世":
            st.error("（来自古墓的回音）：“你的声音...好像穿过了千年，但我碰不到你...”")
            user_msg = st.text_input("你想对TA说什么？")
            if user_msg:
                st.info("（回音渐弱）：“...听到了，但风会把这句话吹散在历史里...”")
        elif status == "未出生":
            st.error("（来自未来的光斑）：“我还没来到这个世界，但好像感受到了你的期待...”")
            user_msg = st.text_input("你想对未来的TA说什么？")
            if user_msg:
                st.info("（光斑闪烁）：“这句话会存在时空里，等我出生后听到~”")
        else:
            st.success(f"（TA对你挥了挥手）：“我会{sm_trait}，你呢？”")
            user_msg = st.text_input("你想回复TA什么？")
            if user_msg:
                # 贴合原文“伪装”：即使同年代，也可能是“假装匹配”
                fake_chance = random.randint(1, 10)
                if fake_chance > 8:
                    st.warning("（TA突然低头）：“其实...我只是觉得你像我要找的人，抱歉...”")
                else:
                    st.info(f"（TA笑了笑）：“{user_msg}？好巧！我也喜欢这个~”")


# ---------------------- 5. 主题呼应：原文观点展示 ----------------------
st.divider()
st.markdown("### 📖 原文核心观点（这个设定是“噩梦”的原因）")
st.markdown("1. **时空矛盾**：人类历史1000亿人，当前仅70亿存活，90%伴侣已离世；")
st.markdown("2. **概率极低**：一生接触的人仅占“可选范围”的0.01%，匹配概率约万分之一；")
st.markdown("3. **社会扭曲**：多数人会“假装匹配”，掩饰矛盾以逃避孤独。")
