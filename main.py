from modelos import Dolar, Bitcoin

print("Iniciando Monitor de Cotações...\n")

moeda_dolar = Dolar()
moeda_btc = Bitcoin()

dolar = moeda_dolar.buscar_cotacao_online()
bitcoin = moeda_btc.buscar_cotacao_online()

if dolar and bitcoin:    
    print(f"O {moeda_dolar.nome} está: R${dolar:.2f}")
    print(f"O {moeda_btc.nome} está: USD{bitcoin:.2f}")
    
    valor = float(input("Digite um valor para converter:"))

    calculo_dolar = dolar * valor
    calculo_real = valor/dolar

    print("\n--- Resultado da Conversão ---")
    print(f"USD {valor:.2f} está valendo R$ {calculo_dolar:.2f}")
    print(f"R$ {valor:.2f} está valendo USD {calculo_real:.2f}")
else:
    print("Falha ao buscar as cotações")
