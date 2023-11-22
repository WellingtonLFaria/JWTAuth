import requests
import time
from settings import TEMPO_EXPIRACAO_SEGUNDOS

# URL do API
url = "http://127.0.0.1:5000/"

# Usuário e senha
data = {
    "username": "user",
    "password": "pass"
}

# Registrando o usuário
print("Registrando o usuário")
response = requests.post(url + "register", json=data)
print("Retorno:", response.json())

# Logando o usuário
print()
print("Logando o usuário")
response = requests.post(url + "login", json=data)
print("Retorno:", response.json())

# Salvando o token
token = response.json()['token']

# Verificação do usuário
print()
print("Verificando o usuário")
response = requests.post(url + "verificar", json={"token": token})
print(response.json())

# Esperando o token expirar
print()
for c in range(TEMPO_EXPIRACAO_SEGUNDOS):
    print(f"Esperando {TEMPO_EXPIRACAO_SEGUNDOS - c} segundos para o token expirar")
    time.sleep(1)

# Verificando o usuário novamente após o token expirar
print()
print("Verificando o usuário novamente após o token expirar")
response = requests.post(url + "verificar", json={"token": token})
print("Retorno:", response.json())