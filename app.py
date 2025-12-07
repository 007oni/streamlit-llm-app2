from dotenv import load_dotenv

load_dotenv()


import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage


# LLMからの回答を取得する関数
def get_llm_response(input_text, expert_type):
    expert_prompts = {
        "筋トレのプロ": "あなたは筋トレのプロフェッショナルです。筋トレに関する質問に答えてください。",
        "スイーツ専門家": "あなたは東京都内のスイーツを知り尽くしたスイーツ専門家です。スイーツに関する質問に答えてください。",
        "AIプログラミング専門家": "あなたはAIプログラミングに詳しいものです。AIプログラミングに関する質問に答えてください。"
    }

    system_message = expert_prompts.get(expert_type, "あなたは知識豊富なアシスタントです。")

    chat = ChatOpenAI(temperature=0)
    messages = [
        SystemMessage(content=str(system_message)),
        HumanMessage(content=str(input_text))
    ]

    # デバッグ用ログ
    st.write("Debug: Messages", messages)

    response = chat.generate(messages)
    return response.content

# Streamlitアプリケーション
st.title("専門家に質問しよう！")

# 入力フォーム
input_text = st.text_area("質問を入力してください：", "")

# ラジオボタンで専門家の種類を選択
expert_type = st.radio(
    "専門家の種類を選択してください：",
    ("筋トレのプロ", "スイーツ専門家", "AIプログラミング専門家")
)

# 送信ボタン
if st.button("送信"):
    if input_text.strip():
        # LLMからの回答を取得
        response = get_llm_response(input_text, expert_type)
        # 結果を表示
        st.subheader("回答：")
        st.write(response)
    else:
        st.warning("質問を入力してください！")