from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
import os
import time
import random

fake = Faker()

# Pasta para salvar prints
caminho_prints = r"C:\Users\Eduardo Santana\Desktop\Desafio Accenture"
os.makedirs(caminho_prints, exist_ok=True)

# Inicializa navegador
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
navegador.maximize_window()
navegador.get("https://demoqa.com")

espera = WebDriverWait(navegador, 10)

def clicar_humano(elemento, min_pause=0.3, max_pause=0.8):
    """Clica no elemento simulando comportamento humano"""
    elemento.click()
    time.sleep(random.uniform(min_pause, max_pause))

def centralizar_travar(elemento):
    """Mantém o elemento centralizado na tela"""
    navegador.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", elemento)
    time.sleep(random.uniform(0.3, 0.7))

def digitar_humano(elemento, texto):
    """Digita simulando velocidade humana"""
    for char in texto:
        elemento.send_keys(char)
        time.sleep(random.uniform(0.05, 0.15))

try:
    # Entrar em Elements
    btn_elements = espera.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
    centralizar_travar(btn_elements)
    clicar_humano(btn_elements)
    print("✅ Clicou em 'Elements'")

    # Entrar em Web Tables
    btn_webtables = espera.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Web Tables']")))
    centralizar_travar(btn_webtables)
    clicar_humano(btn_webtables)
    print("✅ Clicou em 'Web Tables'")

    # Função para adicionar usuário
    def adicionar_usuario():
        add_btn = espera.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
        centralizar_travar(add_btn)
        clicar_humano(add_btn)

        espera.until(EC.visibility_of_element_located((By.ID, "firstName")))

        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        age = str(fake.random_int(18, 65))
        salary = str(fake.random_int(1000, 10000))
        department = fake.word()

        digitar_humano(navegador.find_element(By.ID, "firstName"), first_name)
        digitar_humano(navegador.find_element(By.ID, "lastName"), last_name)
        digitar_humano(navegador.find_element(By.ID, "userEmail"), email)
        digitar_humano(navegador.find_element(By.ID, "age"), age)
        digitar_humano(navegador.find_element(By.ID, "salary"), salary)
        digitar_humano(navegador.find_element(By.ID, "department"), department)

        btn_submit = navegador.find_element(By.ID, "submit")
        centralizar_travar(btn_submit)
        clicar_humano(btn_submit)

        print(f"✅ Usuário adicionado: {first_name} {last_name}, salário: {salary}")

        # Print de evidência
        caminho_usuario = os.path.join(caminho_prints, f"user_added_{first_name}.png")
        navegador.save_screenshot(caminho_usuario)
        print(f"📸 Screenshot do usuário adicionado salva em: {caminho_usuario}")

        return first_name, last_name, salary

    usuarios = []

    # Adicionar 12 usuários
    for _ in range(12):
        usuarios.append(adicionar_usuario())
        time.sleep(random.uniform(0.3, 0.7))

    # Editar usuários
    for first_name, last_name, salary in usuarios:
        edit_btn = espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[title='Edit']")))
        centralizar_travar(edit_btn)
        clicar_humano(edit_btn)

        espera.until(EC.visibility_of_element_located((By.ID, "firstName")))

        new_first_name = first_name + "_Edit"
        new_salary = str(int(salary) + 1000)

        first_input = navegador.find_element(By.ID, "firstName")
        first_input.clear()
        digitar_humano(first_input, new_first_name)

        salary_input = navegador.find_element(By.ID, "salary")
        salary_input.clear()
        digitar_humano(salary_input, new_salary)

        btn_submit = navegador.find_element(By.ID, "submit")
        centralizar_travar(btn_submit)
        clicar_humano(btn_submit)

        print(f"✅ Usuário editado: {new_first_name}, salário: {new_salary}")

        # Print de evidência
        caminho_edit = os.path.join(caminho_prints, f"user_edited_{new_first_name}.png")
        navegador.save_screenshot(caminho_edit)
        print(f"📸 Screenshot do usuário editado salva em: {caminho_edit}")

        time.sleep(random.uniform(0.3, 0.6))

    # Deletar todos os usuários
    while True:
        delete_buttons = navegador.find_elements(By.CSS_SELECTOR, "span[title='Delete']")
        if not delete_buttons:
            break
        btn = delete_buttons[0]
        centralizar_travar(btn)
        clicar_humano(btn, 0.2, 0.5)
        print("✅ Usuário deletado")
        time.sleep(random.uniform(0.2, 0.5))

    # Screenshot final da tabela vazia
    caminho_final = os.path.join(caminho_prints, "webtables_final.png")
    navegador.save_screenshot(caminho_final)
    print(f"📸 Screenshot final salva em: {caminho_final}")

finally:
    navegador.quit()
