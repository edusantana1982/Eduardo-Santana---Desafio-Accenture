from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
import os
import time

fake = Faker()

# Pasta para salvar prints
caminho_prints = r"C:\Eduardo Santana - Desafio Accenture\Evidencias Front"
os.makedirs(caminho_prints, exist_ok=True)

# Inicializa navegador
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
navegador.maximize_window()
navegador.get("https://demoqa.com")

espera = WebDriverWait(navegador, 10)

# Funções rápidas
def clicar(elemento):
    elemento.click()
    time.sleep(0.01)

def centralizar(elemento):
    navegador.execute_script(
        "arguments[0].scrollIntoView({behavior:'auto', block:'center'});", elemento
    )
    time.sleep(0.01)

def digitar(elemento, texto):
    elemento.send_keys(texto)
    time.sleep(0.01)

try:
    # Entrar em Elements
    btn_elements = espera.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
    centralizar(btn_elements)
    clicar(btn_elements)

    # Entrar em Web Tables
    btn_webtables = espera.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Web Tables']")))
    centralizar(btn_webtables)
    clicar(btn_webtables)

    # Função para adicionar usuário
    def adicionar_usuario():
        add_btn = espera.until(EC.element_to_be_clickable((By.ID, "addNewRecordButton")))
        centralizar(add_btn)
        clicar(add_btn)

        espera.until(EC.visibility_of_element_located((By.ID, "firstName")))

        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        age = str(fake.random_int(18, 65))
        salary = str(fake.random_int(1000, 10000))
        department = fake.word()

        digitar(navegador.find_element(By.ID, "firstName"), first_name)
        digitar(navegador.find_element(By.ID, "lastName"), last_name)
        digitar(navegador.find_element(By.ID, "userEmail"), email)
        digitar(navegador.find_element(By.ID, "age"), age)
        digitar(navegador.find_element(By.ID, "salary"), salary)
        digitar(navegador.find_element(By.ID, "department"), department)

        btn_submit = navegador.find_element(By.ID, "submit")
        centralizar(btn_submit)
        clicar(btn_submit)

        return first_name, salary

    usuarios = []

    # 1 Adicionar 12 usuários
    for _ in range(12):
        usuarios.append(adicionar_usuario())

    # Print da tabela com 12 usuários
    caminho_12_usuarios = os.path.join(caminho_prints, "Desafio_3_com_12_usuarios.png")
    navegador.save_screenshot(caminho_12_usuarios)
    print(f"📸 Screenshot da tabela com 12 usuários salva em: {caminho_12_usuarios}")

    # 2 Editar os 12 usuários
    for first_name, salary in usuarios:
        edit_buttons = navegador.find_elements(By.CSS_SELECTOR, "span[title='Edit']")
        if not edit_buttons:
            break
        btn_edit = edit_buttons[0]  # sempre pega o primeiro botão disponível
        centralizar(btn_edit)
        clicar(btn_edit)

        espera.until(EC.visibility_of_element_located((By.ID, "firstName")))

        new_first_name = first_name + "_Edit"
        new_salary = str(int(salary) + 1000)

        first_input = navegador.find_element(By.ID, "firstName")
        first_input.clear()
        digitar(first_input, new_first_name)

        salary_input = navegador.find_element(By.ID, "salary")
        salary_input.clear()
        digitar(salary_input, new_salary)

        btn_submit = navegador.find_element(By.ID, "submit")
        centralizar(btn_submit)
        clicar(btn_submit)

    # 3 Deletar todos os usuários
    while True:
        delete_buttons = navegador.find_elements(By.CSS_SELECTOR, "span[title='Delete']")
        if not delete_buttons:
            break
        centralizar(delete_buttons[0])
        clicar(delete_buttons[0])

    # Print da tabela vazia
    caminho_final = os.path.join(caminho_prints, "Desafio_3_Tabela_vazia.png")
    navegador.save_screenshot(caminho_final)
    print(f"📸 Screenshot final (tabela vazia) salva em: {caminho_final}")

finally:
    navegador.quit()
