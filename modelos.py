from abc import ABC, abstractmethod
from requests.exceptions import RequestException
import requests

class AtivoFinanceiro(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def buscar_cotacao_online(self):
        pass

class Dolar(AtivoFinanceiro):
    def __init__(self, nome ="Dólar Americano"):
        super().__init__(nome)
        
   def buscar_cotacao_online(self):
        try:
            url = 'https://economia.awesomeapi.com.br/last/USD-BRL' # Mude para BTC-USD na do Bitcoin
            
            # 🎭 O DISFARCE: Fingindo ser o Google Chrome no Windows
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            }
            
            # Enviamos o disfarce junto com o GET
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                return float(data['USDBRL']['bid']) # Mude para BTCUSD na do Bitcoin
            return None
        
        except RequestException as req_err:
            print(f"Erro na requisição: {req_err}")
            return None
    
    def buscar_dados_completos(self):
        try:
            url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return {
                    "valor": float(data['USDBRL']['bid']),
                    "variacao": float(data['USDBRL']['pctChange']) # A mágica da API aqui!
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
            url = 'https://economia.awesomeapi.com.br/last/BTC-USD'
        
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            }
            
            # Enviamos o disfarce junto com o GET
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
            url = 'https://economia.awesomeapi.com.br/last/BTC-USD'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return {
                    "valor": float(data['BTCUSD']['bid']),
                    "variacao": float(data['BTCUSD']['pctChange']) # A mágica da API aqui!
                }
            return None
        except RequestException as req_err:
            print(f"Erro na requisição: {req_err}")
            return None
