import os
from dotenv import load_dotenv
from abc import ABC, abstractmethod
from requests.exceptions import RequestException
import requests

load_dotenv()
API_KEY = os.getenv("AWESOME_API_KEY")

class AtivoFinanceiro(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def buscar_cotacao_online(self):
        pass

class Dolar(AtivoFinanceiro):
    def __init__(self, nome="Dólar Americano"):
        super().__init__(nome)
        
    def buscar_cotacao_online(self):
        try:
            url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
            headers = {"x-api-key": API_KEY}
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                return float(data['USDBRL']['bid'])
            
            # 🚨 MODO DETETIVE ATIVADO 🚨
            print("--- INVESTIGAÇÃO DA API ---")
            print(f"A chave carregou do Secrets?: {API_KEY is not None}")
            print(f"Status do Erro: {response.status_code}")
            print(f"Mensagem da API: {response.text}")
            print("---------------------------")
            return None
        
        except RequestException as req_err:
            print(f"Erro na requisição: {req_err}")
            return None
            
    def buscar_dados_completos(self):
        try:
            url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
            headers = {"x-api-key": API_KEY}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return {
                    "valor": float(data['USDBRL']['bid']),
                    "variacao": float(data['USDBRL']['pctChange']) 
                }
            return None
        except RequestException as req_err:
            print(f"Erro na requisição: {req_err}")
            return None
    
class Bitcoin(AtivoFinanceiro):
    def __init__(self, nome="Bitcoin"):
        super().__init__(nome)
    
    def buscar_cotacao_online(self):
        try:
            url = 'https://economia.awesomeapi.com.br/json/last/BTC-USD'
            headers = {"x-api-key": API_KEY}
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                return float(data['BTCUSD']['bid'])
            return None
        
        except RequestException as req_err:
            print(f"Erro na requisição: {req_err}")
            return None
            
    def buscar_dados_completos(self):
        try:
            url = 'https://economia.awesomeapi.com.br/json/last/BTC-USD'
            headers = {"x-api-key": API_KEY}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return {
                    "valor": float(data['BTCUSD']['bid']),
                    "variacao": float(data['BTCUSD']['pctChange']) 
                }
            return None
        except RequestException as req_err:
            print(f"Erro na requisição: {req_err}")
            return None
