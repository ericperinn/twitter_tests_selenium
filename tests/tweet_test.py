# tests/tweet_test.py
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

class TweetTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        # Login antes de testar tweet
        self.driver.get(config.LOGIN_URL)
        
        try:
            # Aguardar e inserir o e-mail
            print("Aguardando campo de e-mail...")
            email_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            print("Campo de e-mail encontrado.")
            email_input.send_keys(config.USER_EMAIL)
            email_input.send_keys(Keys.RETURN)
        except Exception as e:
            print("Erro ao encontrar o campo de e-mail:", e)
            self.driver.save_screenshot("login_error_email.png")
            raise e

        try:
            # Aguardar e inserir a senha
            print("Aguardando campo de senha...")
            password_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            print("Campo de senha encontrado.")
            password_input.send_keys(config.USER_PASSWORD)
            password_input.send_keys(Keys.RETURN)
        except Exception as e:
            print("Erro ao encontrar o campo de senha:", e)
            self.driver.save_screenshot("login_error_password.png")
            raise e

        try:
            # Aguardar a página inicial após o login
            print("Aguardando elementos da página inicial...")
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='primaryColumn']"))
            )
            print("Página inicial carregada.")
        except Exception as e:
            print("Erro ao aguardar a página inicial:", e)
            self.driver.save_screenshot("login_error_page.png")
            raise e

    def test_post_tweet(self):
        try:
            print("Aguardando o campo de texto do tweet...")
            # Atualize o seletor abaixo com o que você encontrar no DevTools
            tweet_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div"))
            )
            print("Campo de texto do tweet encontrado.")
            tweet_input.click()
            tweet_input.send_keys("Este é um tweet de teste automatizado.")
            tweet_input.send_keys(Keys.CONTROL, Keys.RETURN)

            print("Aguardando o tweet aparecer na linha do tempo...")
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='Este é um tweet de teste automatizado.']"))
            )
            print("Tweet postado com sucesso.")
        except Exception as e:
            print("Erro durante o teste de postagem do tweet.")
            self.driver.save_screenshot("tweet_test_error.png")
            raise e

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
