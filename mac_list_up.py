import os
import subprocess
import time
import sys

# 1. 準備（今いる場所のファイルをチェック）
all_files = [f for f in os.listdir('.') if not f.startswith('.') and f != 'list_up.py']
total_count = len(all_files)
selected_contents = [] # 選んだ「ファイルの中身」を溜める場所
index = 0

print(f"\n🚀 仕分け開始（全 {total_count} 件）")

# 2. 実行（y:入れる / n:入れない / b:戻る）
while index < total_count:
    name = all_files[index]
    remaining = total_count - index
    
    print("-" * 30)
    print(f"📦 [残り {remaining}件]  対象：{name}")
    choice = input("👉 [ y:入れる / n:入れない / b:戻る ] -> ")

    # 【b】戻る
    if choice.lower() == 'b' and index > 0:
        index -= 1
        if selected_contents:
            selected_contents.pop()
        print("   ⬅️ 1つ前に戻ったよ")
        continue
    
    # 【y】入れる（中身を読み取る）
    if choice.lower() == 'y':
        try:
            # ファイル名じゃなく「中身」を読み込む [Python公式: open](https://docs.python.org)
            with open(name, 'r', encoding='utf-8') as f:
                content = f.read()
            selected_contents.append(f"【ファイル名: {name}】\n{content}")
            print(f"   ✅ 『{name}』の中身をキープ！")
        except Exception:
            print("   ⚠️ テキストじゃないから中身は読み込めなかったよ")
    
    index += 1

# 3. 【一括コピー ＋ 挨拶 ＋ 画面掃除】
if selected_contents:
    # 選んだ全部の中身をつなぎ、最後に「以上です！」を添える
    final_text = "\n\n".join(selected_contents) + "\n\n以上です！ご確認よろしくお願いします。"
    
    # Macのクリップボードへ送る (pbcopy) [Apple公式: ターミナルでコピー](https://support.apple.com)
    process = subprocess.Popen('pbcopy', stdin=subprocess.PIPE)
    process.communicate(final_text.encode('utf-8'))

    print("\n✅ 中身と挨拶をコピー完了！ 2秒後に画面を掃除するよ...")
    time.sleep(2)

    # 画面を綺麗にする [Apple公式: clearコマンド](https://support.apple.com)
    os.system('clear')
    print("✨ 掃除完了！好きな場所に Cmd+V で貼り付けてね！")
else:
    os.system('clear')
    print("何も選ばれなかったよ。")
