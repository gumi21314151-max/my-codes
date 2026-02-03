import os
from openai import OpenAI

# 🔑 ここにあなたの sk- から始まる鍵を貼り付ける
API_KEY = ""

client = OpenAI(api_key=API_KEY)

def speak(text, user_visible=True):
    if user_visible:
        print(f"🤖 秘書: {text}")
    os.system(f"say '{text}'")

print("--- 🌟 ビジネスAI秘書システム 起動 🌟 ---")
speak("お疲れ様です。本日の業務を開始します。何をお手伝いしましょうか？")

# 会話の記憶（ここがビジネスの肝！）
messages = [{"role": "system", "content": "あなたは超優秀なビジネス秘書です。丁寧な敬語で、ユーザーを元気づけながら的確に答えてください。"}]

while True:
    user_input = input("\nあなた > ")
    
    if user_input in ["終了", "バイバイ", "おやすみ"]:
        speak("本日も一日お疲れ様でした。ゆっくりお休みください。")
        break

    messages.append({"role": "user", "content": user_input})
    
    try:
        # AI（ChatGPT）に問い合わせ
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=300
        )
