import time
import pyperclip
import threading
from pynput import keyboard

# 履歴を8個保存（Aが最新、Lが一番古い）
# A, S, D, F, G, H, J, K, L の順番に対応
history = ["空っぽ"] * 9
key_map = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
ctrl_pressed = False
controller = keyboard.Controller()

def on_press(key):
    global ctrl_pressed
    if key == keyboard.Key.ctrl:
        ctrl_pressed = True

    try:
        if ctrl_pressed:
            # A, S, D, F, G, H, J, K, L のどれかが押されたかチェック
            if key.char in key_map:
                idx = key_map.index(key.char)
                paste_from_history(idx)
    except AttributeError:
        pass

def paste_from_history(idx):
    if history[idx] != "空っぽ":
        pyperclip.copy(history[idx])
        print(f"【呼び出し({key_map[idx].upper()}番)】: {history[idx][:15]}...")
        time.sleep(0.1)
        # 自動貼り付け(Command + V)
        with controller.pressed(keyboard.Key.cmd):
            controller.press('v')
            controller.release('v')

def on_release(key):
    global ctrl_pressed
    if key == keyboard.Key.ctrl:
        ctrl_pressed = False

def clipboard_monitor():
    last_text = pyperclip.paste()
    while True:
        try:
            current_text = pyperclip.paste()
            if current_text != last_text and current_text != "":
                # 最新を先頭に追加して、古い(9個目以降)を消す
                history.insert(0, current_text)
                if len(history) > 9:
                    history.pop()
                last_text = current_text
                print(f"【保存 A番】: {current_text[:15]}...")
        except: pass
        time.sleep(0.5)

threading.Thread(target=clipboard_monitor, daemon=True).start()

print("--- コピペの神様：8連弾 (kopi.py) ---")
print("・Control + A (最新) / S / D / F / G / H / J / K / L (最古)")
print("・Command + C でどんどん貯まるぞ！")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
