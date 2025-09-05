from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import random

# ---------------- Funções de comportamento humano ----------------
def centralizar_travar(elemento):
    """Centraliza o elemento na tela suavemente."""
    navegador.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", elemento)
    time.sleep(random.uniform(0.3, 0.7))

def clicar_humano(elemento, min_pause=0.3, max_pause=0.8):
    """Clica no elemento simulando comportamento humano."""
    elemento.click()
    time.sleep(random.uniform(min_pause, max_pause))

# Pasta para salvar prints
caminho_prints = r"C:\Eduardo Santana - Desafio Accenture\Evidencias Front"
os.makedirs(caminho_prints, exist_ok=True)

# ---------------- Inicialização do navegador ----------------
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
navegador.maximize_window()
navegador.get("https://demoqa.com")
espera = WebDriverWait(navegador, 10)

try:
    # --- Clicar em Forms ---
    btn_forms = espera.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Forms']")))
    centralizar_travar(btn_forms)
    clicar_humano(btn_forms)
    espera.until(EC.url_contains("/forms"))
    print("✅ Botão 'Forms' clicado")

    # --- Clicar em Alerts, Frame & Windows ---
    btn_alerts = espera.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='header-text' and text()='Alerts, Frame & Windows']")))
    centralizar_travar(btn_alerts)
    clicar_humano(btn_alerts)
    print("✅ Clicou em 'Alerts, Frame & Windows'")

    # --- Clicar em Browser Windows ---
    btn_browser = espera.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Browser Windows']")))
    centralizar_travar(btn_browser)
    clicar_humano(btn_browser)
    print("✅ Clicou em 'Browser Windows'")

    # --- Clicar no botão New Window ---
    btn_new_window = espera.until(EC.element_to_be_clickable((By.ID, "windowButton")))
    centralizar_travar(btn_new_window)
    clicar_humano(btn_new_window)
    print("✅ Botão 'New Window' clicado")
    time.sleep(2)

    # --- Alternando janela ---
    janelas = navegador.window_handles
    janela_principal = navegador.current_window_handle
    for janela in janelas:
        if janela != janela_principal:
            navegador.switch_to.window(janela)
            time.sleep(1)
            break

    # --- Validar a frase ---
    try:
        corpo = navegador.find_element(By.TAG_NAME, "body")
        texto = corpo.text.strip()
        frase_esperada = "This is a sample page"
        if frase_esperada in texto:
            print(f"✅ Frase encontrada na nova janela: '{frase_esperada}'")
        else:
            print(f"⚠️ Frase diferente do esperado: '{texto}'")
    except Exception as e:
        print(f"⚠️ Não foi possível validar o texto: {e}")

    # --- Screenshot da nova janela ---
    screenshot_nova = os.path.join(caminho_prints, "Desafio_2_nova_janela.png")
    navegador.save_screenshot(screenshot_nova)
    print(f"📸 Screenshot da nova janela salva em: {screenshot_nova}")

    # --- Fechar a nova janela e voltar para a principal ---
    navegador.close()
    navegador.switch_to.window(janela_principal)
    print("✅ Voltou para a janela principal")

finally:
    navegador.quit()
    print("✅ Navegador fechado com segurança")
