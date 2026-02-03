<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>グミの1000日に一度の奇跡占い</title>
    <style>
        /* 🌌 宇宙をイメージした背景 */
        body { 
            text-align: center; 
            font-family: 'Hiragino Kaku Gothic ProN', sans-serif; 
            background: #0f0c29; 
            background: linear-gradient(to bottom, #24243e, #302b63, #0f0c29);
            color: white; 
            padding: 50px 20px; 
            transition: 1.5s; 
            overflow: hidden;
            height: 100vh;
        }
        .container { 
            background: rgba(0, 0, 0, 0.7); 
            padding: 40px; 
            border-radius: 30px; 
            border: 1px solid rgba(255,255,255,0.2);
            box-shadow: 0 0 40px rgba(0,0,0,0.9); 
            max-width: 550px; 
            margin: auto; 
        }
        h1 { color: #00d2ff; text-shadow: 0 0 15px #00d2ff; letter-spacing: 2px; }
        
        /* 🔘 ボタンのデザイン */
        button { 
            padding: 20px 50px; 
            font-size: 22px; 
            font-weight: bold;
            cursor: pointer; 
            background: linear-gradient(45deg, #e94560, #ff0055);
            color: white; 
            border: none; 
            border-radius: 50px; 
            box-shadow: 0 6px #a02040; 
            transition: 0.3s;
        }
        button:hover { transform: scale(1.1); box-shadow: 0 8px #c03050; }
        button:active { transform: translateY(4px); box-shadow: 0 2px #a02040; }
        button:disabled { background: #444; box-shadow: none; cursor: not-allowed; opacity: 0.6; }

        /* 🔮 結果表示 */
        #result { 
            font-size: 26px; 
            margin-top: 40px; 
            line-height: 1.8; 
            min-height: 150px; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            font-weight: bold;
        }

        /* ✨ 0.1%の奇跡：虹色爆発演出 */
        @keyframes rainbow-bg {
            0% { background: #ff0000; } 16% { background: #ffff00; } 33% { background: #00ff00; }
            50% { background: #00ffff; } 66% { background: #0000ff; } 83% { background: #ff00ff; } 100% { background: #ff0000; }
        }
        @keyframes shake {
            0% { transform: translate(0,0); } 10% { transform: translate(-5px, -5px); }
            30% { transform: translate(5px, 5px); } 50% { transform: translate(-5px, 5px); }
            70% { transform: translate(5px, -5px); } 100% { transform: translate(0,0); }
        }
        .rare-mode { 
            animation: rainbow-bg 0.5s infinite linear !important; /* 高速虹色 */
        }
        .rare-text { 
            animation: shake 0.1s infinite; 
            font-size: 40px !important; 
            color: #fff !important;
            text-shadow: 0 0 20px #000, 0 0 40px #fff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔮 1000日に一度の奇跡鑑定 🔮</h1>
        <p>1日1回。0.1%の「奇跡」を掴み取れ。</p>
        <button id="uranaiBtn" onclick="uranai()">運命を占う</button>
        <div id="result">心を研ぎ澄ませて待て</div>
    </div>

    <script>
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
            const r = Math.random() * 100; // 0.000〜100.000の乱数
            let finalResult = "";

            // 🎲 究極の確率抽選
            if (r < 0.1) { 
                // 【0.1%：伝説】
                finalResult = "🌈奇跡：1000日に一度の神引き！今日は伝説の一日になります。";
            } else if (r < 3.0) { 
                // 【2.9%：超大吉】
                finalResult = "✨超大吉：宇宙があなたを祝福しています！";
            } else if (r < 20.0) { 
                // 【17%：大吉】
                finalResult = "✨大吉：最高の一日！何をやってもうまくいきます。";
            } else if (r < 50.0) { 
                // 【30%：中吉】
                finalResult = "🌿中吉：穏やかで優しい時間が流れるでしょう。";
            } else { 
                // 【50%：吉・その他】
                finalResult = "☀️吉：いつもの日常が少しだけ輝く、そんな日です。";
            }

            renderResult(finalResult);

            // 保存
            const today = new Date().toLocaleDateString();
            localStorage.setItem("lastUranaiDate", today);
            localStorage.setItem("lastUranaiResult", finalResult);
            document.getElementById("uranaiBtn").disabled = true;
        }

        function renderResult(text) {
            const resDiv = document.getElementById("result");
            resDiv.innerText = text;

            // 💎 0.1%を引き当てた時の演出
            if (text.includes("奇跡")) {
                document.body.classList.add("rare-mode");
                resDiv.classList.add("rare-text");
            } else if (text.includes("超大吉")) {
                // 超大吉はゆっくり虹色
                document.body.style.animation = "rainbow-bg 5s infinite linear";
            }
        }
    </script>
</body>
</html>
