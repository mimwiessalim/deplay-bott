import requests
from telegram import Bot
import time
import os

# --- CONFIGURACIÓN SEGURA ---
TOKEN = os.getenv("7709737711:AAHCN8hgp27p_LSw9rLqjQhw6LffGd0swME")
CHAT_ID = os.getenv("5217879590")
INTERVALO = 60 * 10  # cada 10 minutos

if not TOKEN or not CHAT_ID:
    raise ValueError("⚠️ Faltan variables de entorno: TELEGRAM_BOT_TOKEN y/o TELEGRAM_CHAT_ID")

bot = Bot(token=TOKEN)

def obtener_criptos_top():
    url = 'https://api.bitget.com/api/v2/spot/market/tickers'
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
    except Exception as e:
        print(f"❌ Error al conectar con Bitget: {e}")
        return []

    if 'data' not in data or data.get('code') != '00000':
        print(f"❌ Respuesta inesperada de Bitget: {data}")
        return []

    criptos = []
    for item in data['data']:
        try:
            cambio = float(item.get('change24h', 0)) * 100
            volumen = float(item.get('usdtVolume', 0))
            
            if cambio > 10 and volumen > 10_000_000:
                criptos.append({
                    'symbol': item['symbol'],
                    'precio': item['lastPr'],
                    'cambio': cambio,
                    'volumen': volumen
                })
        except Exception as e:
            continue

    return criptos

def enviar_alertas():
    criptos = obtener_criptos_top()
    if not criptos:
        print("⏳ No hay criptos con +10% y volumen > 10M en este momento.")
        return

    mensaje = "🚀 *Criptos destacadas en Bitget:*\n\n"
    for c in criptos:
        mensaje += f"💰 {c['symbol']}\n📈 +{c['cambio']:.2f}%\n💵 Vol: ${c['volumen']:,.0f}\n💲 Precio: {c['precio']}\n\n"

    try:
        bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode='Markdown')
        print(f"✅ Alerta enviada: {len(criptos)} criptos encontradas")
    except Exception as e:
        print(f"❌ Error al enviar mensaje: {e}")

# --- LOOP PRINCIPAL ---
print("🤖 Bot de alertas Bitget ejecutándose...")
print(f"📊 Monitoreando criptos cada {INTERVALO//60} minutos")

while True:
    enviar_alertas()
    time.sleep(INTERVALO)
