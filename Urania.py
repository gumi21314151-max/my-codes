<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>グミの100の運勢・究極占い</title>
    <style>
        /* 🌌 基本のデザイン */
        body { 
            text-align: center; 
            font-family: 'Hiragino Kaku Gothic ProN', sans-serif; 
            background: #0f0c29; 
            background: linear-gradient(to bottom, #24243e, #302b63, #0f0c29);
            color: white; 
            padding: 50px 20px; 
            transition: 1s; 
            overflow-x: hidden;
            height: 100vh;
        }
        .container { 
            background: rgba(0, 0, 0, 0.6); 
            padding: 40px; 
            border-radius: 30px; 
            border: 2px solid rgba(255,255,255,0.1);
            box-shadow: 0 0 30px rgba(0,0,0,0.8); 
            max-width: 600px; 
            margin: auto; 
            position: relative;
        }
        h1 { color: #00d2ff; text-shadow: 0 0 10px #00d2ff; }
        
        /* 🔘 ボタンのデザイン */
        button { 
            padding: 18px 40px; 
            font-size: 20px; 
            font-weight: bold;
            cursor: pointer; 
            background: linear-gradient(45deg, #e94560, #ff0055);
            color: white; 
            border: none; 
            border-radius: 50px; 
            box-shadow: 0 6px #a02040; 
            transition: 0.2s;
        }
        button:hover { transform: scale(1.05); }
        button:active { transform: translateY(4px); box-shadow: 0 2px #a02040; }
        button:disabled { background: #444; box-shadow: none; cursor: not-allowed; opacity: 0.5; }

        /* 🔮 結果表示エリア */
        #result { 
            font-size: 24px; 
            margin-top: 40px; 
            line-height: 1.8; 
            min-height: 120px; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            transition: 0.5s;
        }

        /* ✨ 究極のレア演出（レインボー背景） */
        @keyframes rainbow-bg {
            0% { background: #ff0000; } 16% { background: #ffff00; } 33% { background: #00ff00; }
            50% { background: #00ffff; } 66% { background: #0000ff; } 83% { background: #ff00ff; } 100% { background: #ff0000; }
        }
        .rare-mode { 
            animation: rainbow-bg 3s infinite linear !important; 
        }

        /* 🏆 レアテキスト：黄金の震え */
        @keyframes gold-shine {
            0% { text-shadow: 0 0 10px #fff, 0 0 20px #ffea00; color: #fff; }
            100% { text-shadow: 0 0 20px #ffea00, 0 0 40px #ffaa00; color: #ffeb3b; }
        }
        @keyframes shake {
            0% { transform: translate(0,0); } 10% { transform: translate(-3px, -3px); }
            30% { transform: translate(3px, 3px); } 50% { transform: translate(-3px, 3px); }
            70% { transform: translate(3px, -3px); } 100% { transform: translate(0,0); }
        }
        .rare-text { 
            animation: gold-shine 0.5s infinite alternate, shake 0.1s infinite; 
            font-size: 38px !important; 
            color: #ffeb3b !important;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔮 運命の100段階鑑定 🔮</h1>
        <p>1日1回。今日、あなたの運命が極まる。</p>
        <button id="uranaiBtn" onclick="uranai()">運勢を占う</button>
        <div id="result">心を決めてボタンを押せ</div>
    </div>

    <script>
        // ページ読み込み時のチェック
        window.onload = function() {
            const today = new Date().toLocaleDateString();
            const lastDate = localStorage.getItem("lastUranaiDate");
            const lastResult = localStorage.getItem("lastUranaiResult");

            if (lastDate === today) {
                renderResult(lastResult);
                document.getElementById("uranaiBtn").disabled = true;
            }
        };

        function uranai() {
            // --- 運勢リスト (100個のバリエーションに対応) ---
            const results = [
                "🌈奇跡：100個目の運勢！今日は伝説の一日になります。",
                "✨超大吉：宇宙があなたを祝福しています！",
                "✨大吉：最高の一日！何をやってもうまくいきます。",
                "✨大吉：欲しかったものが手に入るチャンス！",
                "🌿中吉：穏やかで優しい時間が流れるでしょう。",
                "☀️吉：いつもの日常が少しだけ輝く、そんな日です。",
                "🌱小吉：小さな幸せをたくさん見つけられるはず。",
                "☁️末吉：今日は無理せず、現状維持でOK！",
                "☔️要注意：今日はゆっくり休んでエネルギーを貯めよう。"
                // ... ここに以前のリストを自由に足してください
            ];

            // 🎲 運命の抽選
            const n = Math.floor(Math.random() * results.length);
            const finalResult = results[n];

            renderResult(finalResult);

            // 記憶
            const today = new Date().toLocaleDateString();
            localStorage.setItem("lastUranaiDate", today);
            localStorage.setItem("lastUranaiResult", finalResult);
            document.getElementById("uranaiBtn").disabled = true;
        }

        function renderResult(text) {
            const resDiv = document.getElementById("result");
            resDiv.innerText = text;

            // 💎 レア演出の判定
            if (text.includes("奇跡") || text.includes("超大吉")) {
                document.body.classList.add("rare-mode");
                resDiv.classList.add("rare-text");
            }
        }
    </script>
</body>
</html>
