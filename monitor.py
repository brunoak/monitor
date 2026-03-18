import os
from dotenv import load_dotenv
from modelos import Dolar, Bitcoin
from alerta_telegram import enviar_alerta

# Carrega as variáveis de ambiente na memória central
load_dotenv()

def vigiar_mercado():
    print("Arkad acordou. Analisando o mercado...")
    
    # Parâmetro de sensibilidade do mentor
    GATILHO_ALERTA = 2.0 
    
    moeda_dolar = Dolar()
    moeda_btc = Bitcoin()
    
    dados_dolar = moeda_dolar.buscar_dados_completos()
    dados_btc = moeda_btc.buscar_dados_completos()
    
    # 🕵️‍♂️ ANÁLISE DO DÓLAR
    if dados_dolar:
        variacao_dolar = dados_dolar['variacao']
        valor_dolar = dados_dolar['valor']
        
        if abs(variacao_dolar) >= GATILHO_ALERTA:
            icone = "🚀" if variacao_dolar > 0 else "📉"
            msg = f"🚨 *ALERTA DÓLAR* {icone}\n\nMovimentação detectada!\nVariação: *{variacao_dolar:.2f}%*\nCotação atual: *R$ {valor_dolar:.4f}*"
            enviar_alerta(msg)
        else:
            print(f"Dólar estável. Variação atual: {variacao_dolar:.2f}%. Nenhuma ação necessária.")

    # 🕵️‍♂️ ANÁLISE DO BITCOIN
    if dados_btc:
        variacao_btc = dados_btc['variacao']
        valor_btc = dados_btc['valor']
        
        if abs(variacao_btc) >= GATILHO_ALERTA:
            icone = "🚀" if variacao_btc > 0 else "📉"
            # Formatando BTC com separador de milhar
            msg = f"🚨 *ALERTA BITCOIN* {icone}\n\nMovimentação detectada!\nVariação: *{variacao_btc:.2f}%*\nCotação atual: *USD {valor_btc:,.2f}*"
            enviar_alerta(msg)
        else:
            print(f"Bitcoin estável. Variação atual: {variacao_btc:.2f}%. Nenhuma ação necessária.")
            
    print("Análise concluída. Arkad voltando a dormir.")

if __name__ == "__main__":
    vigiar_mercado()