# notifications_test.py
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Adicionada importação de Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Adiciona o diretório raiz ao caminho de pesquisa do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from login_helper import login  # Importe a função de login do módulo correto

def click_search_tab(driver):
    # Aguarda até que o botão de pesquisa esteja visível e clica nele
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Search and explore"]'))
    )
    search_button.click()

def search_for(driver, query):
    # Aguarda até que o campo de busca esteja visível e envia a consulta
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@aria-label="Search query"]'))
    )
    search_input.send_keys(query)
    search_input.send_keys(Keys.RETURN)

if __name__ == "__main__":
    driver = webdriver.Chrome()

    try:
        # Realiza o login usando a função importada
        login(driver)

        # Clica na aba de pesquisa
        click_search_tab(driver)

        # Realiza uma pesquisa
        search_for(driver, "OpenAI")
    finally:
        # Fecha o driver
        driver.quit()
