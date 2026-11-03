import os
import json
import urllib.request

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

def telegram(method):
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"
    with urllib.request.urlopen(url, timeout=20) as response:
        return json.loads(response.read())

updates = telegram("getUpdates")

messages = updates.get("result", [])

if messages:
    chat_id = messages[-1]["message"]["chat"]["id"]
    telegram(f"sendMessage?chat_id={chat_id}&text=¡Tu bot de citas de Barcelona está conectado!")
    print("Mensaje de prueba enviado.")
else:
    print("Primero debes enviar /start a tu bot de Telegram.")
