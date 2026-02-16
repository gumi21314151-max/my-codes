import yfinance as yf
import pandas as pd
from colorama import init, Fore, Style

# 色を初期化
init(autoreset=True)

def gumi_checker():
    ticker_symbol = "GOOGL"
    print(f"{Fore.CYAN}--- アルファベット(Google) リアルタイムチェック ---")

    try:
        # 1. データを取得（1ヶ月分、1日単位）
        ticker = yf.Ticker(ticker_symbol)
        df = ticker.history(period="1mo")

        if not df.empty and len(df) >= 2:
            # 最新と1日前の「終値」を取得
            latest_price = df['Close'].iloc[-1]
            previous_price = df['Close'].iloc[-2]
            change = latest_price - previous_price
            
            print(f"銘柄: {ticker_symbol}")
            print(f"現在価格: ${latest_price:.2f}")

            # 2. 君の「色分けロジック」発動！
            if change > 0:
                print(f"変化: {Fore.GREEN}+${change:.2f} 🚀")
                print(f"{Fore.GREEN}{Style.BRIGHT}分析：Google絶好調！")
            elif change < 0:
                print(f"変化: {Fore.RED}-${abs(change):.2f} 📉")
                print(f"{Fore.RED}{Style.BRIGHT}分析：今は我慢の時。")
            else:
                print(f"変化: $0.00")
        else:
            print("データが空っぽです。ネット接続を確認してね。")

    except Exception as e:
        # 3. 何のエラーか詳しく教えてくれる魔法
        print(f"{Fore.RED}エラー発生！内容はこちら：\n{e}")

if __name__ == "__main__":
    gumi_checker()
