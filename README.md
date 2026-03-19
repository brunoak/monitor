# 📈 Monitor de Cotação Dolar/Bitcoin

Este é um microsserviço de monitoramento da cotação e conversor de dolar e Bitcoin desenvolvido em Python.

O projeto é dividido em duas frentes independentes: uma **Interface Web** para consulta em tempo real e um **Bot Autônomo** no Telegram, alertando sobre volatilidades do mercado.

## 🚀 Funcionalidades

* **Dashboard Web:** Interface interativa e minimalista desenvolvida com Streamlit para conversão de moedas (Dólar e Bitcoin) em tempo real.
* **Monitoramento Autônomo:** Robô rodando em nuvem (Serverless) que analisa o mercado de hora em hora.
* **Alertas Inteligentes:** O sistema não faz spam. Ele calcula a variação percentual dos ativos e dispara mensagens no Telegram apenas quando detecta movimentações atípicas (altas ou baixas iguais ou superiores a 2%).
* **Resiliência:** Tratamento de exceções contra falhas de rede e bloqueios de API.

## 🛠️ Tecnologias e Arquitetura

* **Linguagem:** Python 3.10+
* **Front-end:** Streamlit & Streamlit Cloud
* **Integração Externa:** AwesomeAPI (Autenticada via API Key) e Telegram Bot API
* **Infraestrutura/Deploy:** GitHub Actions (CRON Jobs / Serverless)
* **Design Pattern:** Programação Orientada a Objetos (POO) com uso de Classes Abstratas, Herança e Encapsulamento.
* **Segurança:** Uso de variáveis de ambiente (`.env` e Secrets) para proteção de tokens e chaves de API.
