import pandas as pd
from colorama import init, Fore, Style

# 色付け機能を初期化
init(autoreset=True)

file_name = "stock_data.csv"

try:
    # CSVファイルを読み込む
    df = pd.read_csv(file_name)
    
    # 最後の2つのデータを取り出す
    if len(df) >= 2:
        latest_price = df['Price (USD)'].iloc[-1]
        previous_price = df['Price (USD)'].iloc[-2]
        change = latest_price - previous_price
        
        print(f"現在の株価: ${latest_price:.2f} ドル")
        print(f"前回の株価: ${previous_price:.2f} ドル")
        
        # --- ここから視覚化（色分け） ---
        if change > 0:
            # 上昇は緑（GREEN）
            print(f"変化: {Fore.GREEN}+${change:.2f} ドル")
            print(f"{Fore.GREEN}{Style.BRIGHT}【分析結果】株価は上昇しています！ 🚀")
        elif change < 0:
            # 下落は赤（RED）
            print(f"変化: {Fore.RED}-${abs(change):.2f} ドル")
            print(f"{Fore.RED}{Style.BRIGHT}【分析結果】株価は下降しています。 📉")
        else:
            # 変化なしは白
            print(f"変化: ${change:.2f} ドル")
            print("【分析結果】株価に変化はありません。")
            
    else:
        print("データがまだ少ないため、分析できません。")

except FileNotFoundError:
    print(f"エラー: {file_name} が見つかりません。")
