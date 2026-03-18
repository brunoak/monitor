import streamlit as st
from modelos import Dolar, Bitcoin

st.title("Meu :blue[Conversor] :sunglasses:")

moeda_dolar = Dolar()
moeda_btc = Bitcoin()

dolar = moeda_dolar.buscar_cotacao_online()
bitcoin = moeda_btc.buscar_cotacao_online()

if dolar is None or bitcoin is None:
    st.error("Ops! A API de cotações está temporariamente indisponível. Tente atualizar a página daqui a pouco.")
else:
    bitcoin_formatado = f"{bitcoin:,.2f}".replace(".","x").replace(".", ",").replace("x", ".")
    dolar_formatado = f"{dolar:,.4f}".replace(".", ",")

    st.metric(label="Cotacão Bitcoin (USD)", value=bitcoin_formatado)
    st.metric(label="Cotacão Dólar", value=dolar_formatado)

    valor_digitado = st.number_input("Digite o valor para converter:")

    if dolar > 0:
        calculo_dolar = dolar * valor_digitado
        calculo_real = valor_digitado / dolar

        st.success(f"USD {valor_digitado:.2f} está valendo R$ {calculo_dolar:.2f}")
        st.success(f"R$ {valor_digitado:.2f} está valendo USD {calculo_real:.2f}")
