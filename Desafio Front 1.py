from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import random

# ---------------- Funções para comportamento humano ----------------
def centralizar_travar(elemento):
    """Centraliza suavemente o elemento na tela"""
    navegador.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", elemento)
    time.sleep(random.uniform(0.3, 0.7))

def clicar_humano(elemento, min_pause=0.3, max_pause=0.8):
    """Clica no elemento simulando comportamento humano"""
    elemento.click()
    time.sleep(random.uniform(min_pause, max_pause))

# ---------------- Configurações ----------------
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

    # --- Clicar em Practice Form ---
    btn_practice = espera.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Practice Form']")))
    centralizar_travar(btn_practice)
    clicar_humano(btn_practice)
    print("✅ Botão 'Practice Form' clicado")

    # --- Preencher Nome e Sobrenome ---
    navegador.find_element(By.ID, "firstName").send_keys("Eduardo")
    time.sleep(random.uniform(0.2,0.5))
    navegador.find_element(By.ID, "lastName").send_keys("Santana")
    time.sleep(random.uniform(0.2,0.5))

    # --- Email ---
    navegador.find_element(By.ID, "userEmail").send_keys("eduardo.santana@example.com")
    time.sleep(random.uniform(0.2,0.5))

    # --- Gender ---
    male_label = espera.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Male']")))
    centralizar_travar(male_label)
    clicar_humano(male_label)

    # --- Mobile ---
    navegador.find_element(By.ID, "userNumber").send_keys("11999999999")
    time.sleep(random.uniform(0.2,0.5))

    # --- Data de nascimento ---
    dob_input = navegador.find_element(By.ID, "dateOfBirthInput")
    centralizar_travar(dob_input)
    dob_input.click()
    dob_input.send_keys("04/12/82")
    dob_input.send_keys(Keys.ENTER)
    time.sleep(random.uniform(0.3,0.6))

    # --- Subjects ---
    subjects_input = navegador.find_element(By.ID, "subjectsInput")
    subjects_input.send_keys("Maths")
    subjects_input.send_keys(Keys.ENTER)
    time.sleep(0.3)
    subjects_input.send_keys("Physics")
    subjects_input.send_keys(Keys.ENTER)
    time.sleep(0.3)

    # --- Hobbies ---
    hobbies_sports = navegador.find_element(By.XPATH, "//label[text()='Sports']")
    hobbies_music = navegador.find_element(By.XPATH, "//label[text()='Music']")
    centralizar_travar(hobbies_sports)
    hobbies_sports.click()
    time.sleep(0.3)
    hobbies_music.click()
    time.sleep(0.3)

    # --- State e City ---
    state_input = navegador.find_element(By.ID, "react-select-3-input")
    state_input.send_keys("NCR")
    state_input.send_keys(Keys.ENTER)
    time.sleep(0.3)
    city_input = navegador.find_element(By.ID, "react-select-4-input")
    city_input.send_keys("Delhi")
    city_input.send_keys(Keys.ENTER)
    time.sleep(0.3)

    # --- Upload de arquivo ---
    upload_input = navegador.find_element(By.ID, "uploadPicture")
    arquivo_caminho = os.path.join(caminho_prints, "C:\Eduardo Santana - Desafio Accenture\Anexar ao desafio.txt")
    upload_input.send_keys(arquivo_caminho)
    print("✅ Arquivo anexado com sucesso!")

    # --- Endereço ---
    navegador.find_element(By.ID, "currentAddress").send_keys("Av. Beira Rio, 41 - Jardim Jordão")
    time.sleep(0.3)

    print("✅ Formulário preenchido com sucesso!")

    # --- Scroll e submit ---
    submit_button = navegador.find_element(By.ID, "submit")
    centralizar_travar(submit_button)
    clicar_humano(submit_button)
    print("✅ Formulário enviado com sucesso!")

    time.sleep(1)

    # --- Screenshot do formulário enviado ---
    screenshot_path = os.path.join(caminho_prints, "Desafio_1_formulario_enviado.png")
    navegador.save_screenshot(screenshot_path)
    print(f"📸 Screenshot salva em: {screenshot_path}")

    # --- esperar o popup aparecer ---
    popup_close_button = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.ID, "closeLargeModal"))
)

    # --- clicar no popup usando JavaScript para evitar interferência do iframe ---
    navegador.execute_script("arguments[0].click();", popup_close_button)
    print("✅ Popup fechado com sucesso via JS!")

    time.sleep(2)
    print("✅ Fluxo completo finalizado")

finally:
    navegador.quit()
    print("✅ Navegador fechado")
