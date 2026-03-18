from modelos import Dolar, Bitcoin
from alerta_telegram import enviar_alerta
import time

def monitorar_mercado():
    moeda_dolar = Dolar()
    moeda_btc = Bitcoin()

    # Buscando o pacote completo (Valor + Variação)
    dados_dolar = moeda_dolar.buscar_dados_completos()
    dados_btc = moeda_btc.buscar_dados_completos()
    
    # Defesa caso a API caia
    if dados_dolar is None or dados_btc is None:
        print("Falha ao buscar dados na API. Tentando novamente na próxima hora.")
        return

    # Extraindo as variações
    var_dolar = dados_dolar['variacao']
    var_btc = dados_btc['variacao']

    # Regra de Negócio: Se variar mais de 2% (para cima ou para baixo) nas últimas 24h
    if (var_dolar >= 2.0 or var_dolar <= -2.0) or (var_btc >= 2.0 or var_btc <= -2.0):
        mensagem = (f"🚨 ALERTA ARKAD (Variação Diária)!\n"
                    f"💵 Dólar: R$ {dados_dolar['valor']:.2f} ({var_dolar}%)\n"
                    f"🪙 Bitcoin: USD {dados_btc['valor']:,.2f} ({var_btc}%)")
        
        enviar_alerta(mensagem)
        print("Alerta enviado com sucesso!")
    else:
        print(f"Mercado estável. Dólar variou {var_dolar}% e BTC {var_btc}%. Nenhum alerta necessário.")

while True:
    monitorar_mercado()
    print("Checagem concluída. Dormindo por 1 hora...\n")
    time.sleep(3600)