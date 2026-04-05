import streamlit as st

st.set_page_config(page_title="號碼記錄器", layout="centered")

st.title("🎰 彩票記錄助手")
st.write("這是專為您打造的記錄 App")

# 模擬自動抓取的輸入框
st.divider()
period = st.text_input("📝 請輸入期數", placeholder="例如：2023101201")
numbers = st.text_input("🔢 請輸入號碼", placeholder="例如：01 02 03 04 05")

if st.button("確認記錄這筆資料"):
    if period and numbers:
        st.success(f"✅ 成功記錄！期數：{period}")
        st.balloons()
    else:
        st.error("❌ 抱歉，請先填寫完整喔！")

st.info("ℹ️ 我們之後可以整合 sc888.net 的 API 或自動抓取功能到這裡！")
