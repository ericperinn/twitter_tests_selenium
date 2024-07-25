from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config

def login(driver):
    driver.get(config.LOGIN_URL)

    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "text"))
    )
    email_input.send_keys(config.USER_EMAIL)
    email_input.send_keys(Keys.RETURN)

    try:
        # Verifica a presença da tela de verificação adicional
        verification_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.NAME, "text"))
        )
        verification_input.send_keys(config.USERNAME)
        verification_input.send_keys(Keys.RETURN)
    except:
        pass  # Se a tela não aparecer, continua normalmente

    # Aguarda o campo de senha aparecer
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys(config.USER_PASSWORD)
    password_input.send_keys(Keys.RETURN)

    # Aguarda até que a página inicial seja carregada
    WebDriverWait(driver, 10).until(
        EC.title_contains("Página Inicial")
    )
