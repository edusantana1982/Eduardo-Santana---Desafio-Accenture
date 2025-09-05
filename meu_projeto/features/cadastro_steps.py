from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from faker import Faker
import time

fake = Faker()

@given('que o usuário acessa a página de webtables')
def step_given_acessa_pagina(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demoqa.com/webtables")
    context.driver.maximize_window()
    time.sleep(2)  # espera a página carregar

@when('ele cadastra 12 usuários aleatórios')
def step_when_cadastra_usuarios(context):
    driver = context.driver

    for i in range(12):
        # Clicar no botão Add
        driver.find_element(By.ID, "addNewRecordButton").click()
        time.sleep(1)

        # Preencher os campos do formulário
        driver.find_element(By.ID, "firstName").send_keys(fake.first_name())
        driver.find_element(By.ID, "lastName").send_keys(fake.last_name())
        driver.find_element(By.ID, "userEmail").send_keys(fake.email())
        driver.find_element(By.ID, "age").send_keys(str(fake.random_int(min=18, max=65)))
        driver.find_element(By.ID, "salary").send_keys(str(fake.random_int(min=1000, max=10000)))
        driver.find_element(By.ID, "department").send_keys(fake.word())

        # Enviar o formulário
        driver.find_element(By.ID, "submit").click()
        time.sleep(1)

@then('ele deve ver os 12 usuários cadastrados na tabela')
def step_then_verifica_usuarios(context):
    driver = context.driver
    rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
    assert len(rows) >= 12
    print(f"{len(rows)} usuários cadastrados na tabela")
    driver.quit()
