import os
from dotenv import load_dotenv
import requests

load_dotenv()

token = os.getenv("TELEGRAM_TOKEN")
meu_id = os.getenv("MEU_CHAT_ID")

def enviar_alerta(mensagem):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={meu_id}&text={mensagem}"
    response = requests.get(url)
    print(url)
    
    if response.status_code == 200:
        print("✅ Mensagem enviada com sucesso para o Telegram!")
    else:
        print(f"❌ Falha ao enviar: {response.text}")

if __name__=="__main__":
    mensagem = input("Diga algo: ")
    enviar_alerta(mensagem)