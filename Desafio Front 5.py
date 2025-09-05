import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Pasta para guardar prints
caminho_prints = r"C:\Users\Eduardo Santana\Desktop\Desafio Accenture"
os.makedirs(caminho_prints, exist_ok=True)

# Inicializa navegador
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
navegador.maximize_window()
navegador.get("https://demoqa.com")

espera = WebDriverWait(navegador, 10)
acao = ActionChains(navegador)

# Mapeamento das palavras para números
mapa_palavras = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6
}

def centralizar_lista(driver, elemento):
    """Coloca o container da lista no centro da tela"""
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
        elemento
    )
    time.sleep(random.uniform(0.8, 1.5))  # pausa variável

def pegar_itens():
    """Retorna elementos da lista e seus textos"""
    lista = espera.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@id='demo-tabpane-list']//div[contains(@class,'list-group-item')]")
        )
    )
    return lista, [item.text for item in lista]

try:
    # Entrar no menu Interactions
    menu_interacoes = espera.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Interactions']")))
    navegador.execute_script("arguments[0].scrollIntoView({block:'center'});", menu_interacoes)
    menu_interacoes.click()
    print("Clicou em Interactions")
    time.sleep(random.uniform(0.5, 1.2))

    # Selecionar submenu Sortable
    menu_sortable = espera.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Sortable']")))
    navegador.execute_script("arguments[0].scrollIntoView({block:'center'});", menu_sortable)
    menu_sortable.click()
    print("Clicou em Sortable")
    time.sleep(random.uniform(0.5, 1.2))

    # Centraliza e trava container da lista
    container = espera.until(EC.presence_of_element_located((By.ID, "demo-tabpane-list")))
    centralizar_lista(navegador, container)
    print("Container da lista centralizado e travado")

    # Captura lista inicial
    elementos, textos = pegar_itens()
    print("Lista inicial:", textos)

    # Salvar print inicial
    caminho_inicial = os.path.join(caminho_prints, "Desfio_5_lista_inicial.png")
    navegador.save_screenshot(caminho_inicial)

    # Determinar ordem correta
    ordem_crescente = sorted(textos, key=lambda x: mapa_palavras[x])
    print("Ordem desejada:", ordem_crescente)

    # Organizar lista
    for indice, valor in enumerate(ordem_crescente):
        elementos, textos = pegar_itens()
        if textos[indice] != valor:
            origem = elementos[textos.index(valor)]
            destino = elementos[indice]
            centralizar_lista(navegador, container)
            acao.drag_and_drop(origem, destino).perform()
            time.sleep(random.uniform(0.7, 1.5))

    # Captura lista final
    _, textos_finais = pegar_itens()
    print("Lista final:", textos_finais)

    # Salvar print final
    caminho_final = os.path.join(caminho_prints, "Desafio_5_lista_ordenada.png")
    navegador.save_screenshot(caminho_final)
    print(f"Prints salvos em: {caminho_prints}")

    # Validação final
    if textos_finais == ordem_crescente:
        print("Lista organizada corretamente!")
    else:
        print("A lista não está totalmente correta!")

    time.sleep(2)

finally:
    navegador.quit()
