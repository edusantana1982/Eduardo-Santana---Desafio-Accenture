
import requests

# Criar Usuário

url = "https://demoqa.com/Account/v1/User"
dados = {
  "userName": "EduardoSantana",
  "password": "19820412@Aa"
}

response = requests.post(url, json=dados)

print("Status code:", response.status_code)
print("Resposta:", response.json())

print("✅ Usuário criado ou ja existe!")
#--------------------------------------------------

# Gerar Token de Acesso

url = "https://demoqa.com/Account/v1/GenerateToken"
dados = {
    "userName": "EduardoSantana",
    "password": "19820412@Aa"
}

response = requests.post(url, json=dados)

print("Status code:", response.status_code)
print("Resposta:", response.json())

# Extrair o token da resposta e salvar em uma variável
resposta_json = response.json()
token = resposta_json.get("token")

print("✅ Token gerado com sucesso!")
#print("Token:", token)
#----------------------------------------------------

# Confirmar se o usuário criado está autorizado
url = "https://demoqa.com/Account/v1/Authorized"
dados = {
  "userName": "EduardoSantana",
  "password": "19820412@Aa"
}

response = requests.post(url, json=dados)

print("Status code:", response.status_code)
print("Resposta:", response.json())

print("✅ Usuário autorizado!")

#------------------------------------------------------
#Listar Livros disponiveis

import requests

url = "https://demoqa.com/BookStore/v1/Books"

response = requests.get(url)

print("Status code:", response.status_code)
print("Headers:", dict(response.headers))
print("Resposta:", response.json())

print("✅ Livros Disponiveis")
#------------------------------------------------------

# Alugando dois Livros

# URL da API
url = "https://demoqa.com/BookStore/v1/Books"

# Dados que você quer enviar
data = {
  "userId": "89e62fed-e0a8-46c8-ac39-92a04c15b3fb",
  "collectionOfIsbns": [
    {
      "isbn": "9781449325862"
    },
    {
      "isbn": "9781449337711"
    }
  ]
}

# Token de autenticação
#token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IkVkdWFyZG9TYW50YW5hIiwicGFzc3dvcmQiOiIxOTgyMDQxMkBBYSIsImlhdCI6MTc1NzAyMjk4OH0.9Ec2uiMnodFZkiZFkRI8Y7tjBLOHIqRDIldoR9nl9FU"

# Cabeçalhos, incluindo o Bearer Token
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Fazendo a requisição POST
response = requests.post(url, json=data, headers=headers)

# Mostrando o status e o retorno
print("Status:", response.status_code)
print("Retorno:", response.json())

#-------------------------------------------------------------------------------
#Listar o Usuário com os livros Locados

import os

# URL da API
url = "https://demoqa.com/Account/v1/User/89e62fed-e0a8-46c8-ac39-92a04c15b3fb"  # exemplo

# Token de autenticação
#token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IkVkdWFyZG9TYW50YW5hIiwicGFzc3dvcmQiOiIxOTgyMDQxMkBBYSIsImlhdCI6MTc1NzAyMjk4OH0.9Ec2uiMnodFZkiZFkRI8Y7tjBLOHIqRDIldoR9nl9FU"

# Cabeçalhos
headers = {
    "Authorization": f"Bearer {token}"
}

# Fazendo a requisição GET
response = requests.get(url, headers=headers)

# Verificando se a requisição deu certo
if response.status_code == 200:
    # Caminho do arquivo na pasta do projeto
    file_path = os.path.join(os.getcwd(), "response.txt")
    
    # Salvando o conteúdo em um arquivo .txt
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response.text)
    
    print(f"Resposta salva em: {file_path}")
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)
print("✅ Livros ALugados pelo usuário!")