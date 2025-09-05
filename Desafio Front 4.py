from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# pasta para salvar screenshots
screenshot_folder = r"C:\Users\Eduardo Santana\Desktop\Desafio Accenture"

# abrir navegador
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    navegador.maximize_window()
    navegador.get("https://demoqa.com")

    wait = WebDriverWait(navegador, 10)

    # --- clicar no botão Widgets ---
    widgets_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//h5[text()='Widgets']"))
    )
    navegador.execute_script("arguments[0].scrollIntoView();", widgets_button)
    widgets_button.click()
    print("✅ Clicou em 'Widgets'.")

    wait.until(EC.url_contains("/widgets"))

    # --- clicar no submenu "Progress Bar" ---
    progress_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Progress Bar']"))
    )
    navegador.execute_script("arguments[0].scrollIntoView();", progress_button)
    progress_button.click()
    print("✅ Clicou em 'Progress Bar'.")

    # --- clicar no botão Start ---
    start_button = wait.until(
        EC.element_to_be_clickable((By.ID, "startStopButton"))
    )
    start_button.click()
    print("▶️ Clicou em 'Start'.")

    # --- parar abaixo de 25% ---
    while True:
        progress_text = navegador.find_element(By.CSS_SELECTOR, ".progress-bar").text
        if progress_text != "" and int(progress_text.replace("%", "")) >= 20:
            stop_button = navegador.find_element(By.ID, "startStopButton")
            stop_button.click()
            print(f"⏸️ Stop acionado em {progress_text}.")
            
            # --- tirar screenshot no momento da pausa ---
            desafio_4_path_pause = os.path.join(screenshot_folder, "desafio-4_pause.png")
            navegador.save_screenshot(desafio_4_path_pause)
            print(f"📸 Screenshot de pausa salva em: {desafio_4_path_pause}")
            break
        time.sleep(0.2)

    # --- esperar 5 segundos ---
    print("⏳ Aguardando 5 segundos...")
    time.sleep(5)

    # --- continuar até 100% ---
    start_again = navegador.find_element(By.ID, "startStopButton")
    start_again.click()
    print("▶️ Start novamente, aguardando até 100%.")

    while True:
        progress_text = navegador.find_element(By.CSS_SELECTOR, ".progress-bar").text
        if progress_text == "100%":
            print("🏁 Progresso chegou em 100%.")
            break
        time.sleep(0.3)

    # --- tirar screenshot final ---
    desafio_4_path_final = os.path.join(screenshot_folder, "desafio_4_final.png")
    navegador.save_screenshot(desafio_4_path_final)
    print(f"📸 Screenshot final salva em: {desafio_4_path_final}")

    # --- clicar em Reset ---
    reset_button = navegador.find_element(By.ID, "resetButton")
    reset_button.click()
    print("🔄 Reset acionado.")

    time.sleep(2)

finally:
    navegador.quit()
