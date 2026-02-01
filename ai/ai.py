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
        
        reply = response.choices.message.content.strip()
        speak(reply)
        messages.append({"role": "assistant", "content": reply})
        
    except Exception as e:
        # 💡 ここが「雇う側」のこだわり！ユーザーを困らせないエラー対応
        error_msg = str(e)
        print(f"DEBUG(開発者のみ表示): {error_msg}") # あなただけが見るログ

        if "insufficient_quota" in error_msg:
            # 残高不足の時（5ドルのチャージが必要な時）
            speak("申し訳ございません。現在、窓口が大変混み合っております。時間を置いてもう一度お試しいただくか、管理者へお問い合わせください。")
        else:
            # それ以外のエラー
            speak("少々考え込んでしまいました。もう一度同じことをおっしゃっていただけますか？")
