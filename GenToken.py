import requests

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
print("Token:", token)
