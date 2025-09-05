import requests

# Função para salvar e exibir respostas
def salvar_e_exibir(etapa, dados):
    print(f"\n--- {etapa} ---")
    print(dados)
    with open("EvidenciaResponseAPI.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"--- {etapa} ---\n")
        arquivo.write(str(dados) + "\n\n")
    print(f"✅ {etapa} registrado no arquivo.\n")

# Criar usuário
def criar_usuario(usuario, senha):
    url = "https://demoqa.com/Account/v1/User"
    payload = {"userName": usuario, "password": senha}
    resposta = requests.post(url, json=payload)
    salvar_e_exibir("Criação de Usuário", {"status_code": resposta.status_code, "resposta": resposta.json()})
    return resposta

# Gerar token de acesso
def gerar_token(usuario, senha):
    url = "https://demoqa.com/Account/v1/GenerateToken"
    payload = {"userName": usuario, "password": senha}
    resposta = requests.post(url, json=payload)
    dados = resposta.json()
    token = dados.get("token")
    salvar_e_exibir("Geração de Token", {"status_code": resposta.status_code, "resposta": dados})
    return token

# Verificar autorização do usuário
def verificar_autorizacao(usuario, senha):
    url = "https://demoqa.com/Account/v1/Authorized"
    payload = {"userName": usuario, "password": senha}
    resposta = requests.post(url, json=payload)
    salvar_e_exibir("Verificação de Autorização", {"status_code": resposta.status_code, "resposta": resposta.json()})
    return resposta

# Listar todos os livros disponíveis
def listar_livros():
    url = "https://demoqa.com/BookStore/v1/Books"
    resposta = requests.get(url)
    salvar_e_exibir("Listagem de Livros", {
        "status_code": resposta.status_code,
        "headers": dict(resposta.headers),
        "resposta": resposta.json()
    })
    return resposta

# Alugar livros para o usuário
def alugar_livros(token, user_id, lista_isbns):
    url = "https://demoqa.com/BookStore/v1/Books"
    payload = {
        "userId": user_id,
        "collectionOfIsbns": [{"isbn": isbn} for isbn in lista_isbns]
    }
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    resposta = requests.post(url, json=payload, headers=headers)
    salvar_e_exibir("Aluguel de Livros", {"status_code": resposta.status_code, "resposta": resposta.json()})
    return resposta

# Consultar dados do usuário
def consultar_usuario(token, user_id):
    url = f"https://demoqa.com/Account/v1/User/{user_id}"
    headers = {"Authorization": f"Bearer {token}"}
    resposta = requests.get(url, headers=headers)
    salvar_e_exibir("Consulta de Usuário", {"status_code": resposta.status_code, "resposta": resposta.json()})
    return resposta

# ------------------- EXECUÇÃO -------------------
if __name__ == "__main__":
    usuario = "EduardoSantana"
    senha = "19820412@Aa"
    user_id = "89e62fed-e0a8-46c8-ac39-92a04c15b3fb"  # Substitua pelo ID real do usuário
    livros_para_alugar = ["9781449325862", "9781449337711"]

    criar_usuario(usuario, senha)
    token = gerar_token(usuario, senha)
    verificar_autorizacao(usuario, senha)
    listar_livros()
    alugar_livros(token, user_id, livros_para_alugar)
    consultar_usuario(token, user_id)

    print("\n✅ Todas as etapas concluídas com sucesso. Confira o arquivo response.txt para os detalhes.")
