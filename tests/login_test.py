# tests/login_test.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

# Adiciona o diretório raiz ao caminho de pesquisa do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        self.driver.get(config.LOGIN_URL)

        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "text"))
        )
        email_input.send_keys(config.USER_EMAIL)
        email_input.send_keys(Keys.RETURN)

        # Verifica a presença da tela de verificação adicional
        try:
            verification_input = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.NAME, "text"))
            )
            verification_input.send_keys(config.USERNAME)
            verification_input.send_keys(Keys.RETURN)
        except:
            pass  # Se a tela não aparecer, continua normalmente

        # Aguarda o campo de senha aparecer
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(config.USER_PASSWORD)
        password_input.send_keys(Keys.RETURN)

        # Aguarda até que a página inicial seja carregada
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Página Inicial")
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
