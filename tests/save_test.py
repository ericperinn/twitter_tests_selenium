import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
import time


# Adiciona o diretório raiz ao caminho de pesquisa do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

class SaveTweetTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config.LOGIN_URL)

        try:
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
            print("Aguardando elementos da página inicial...")
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='primaryColumn']"))
            )
            print("Página inicial carregada.")
        except Exception as e:
            print("Erro ao aguardar a página inicial:", e)
            self.driver.save_screenshot("login_error_page.png")
            raise e

    def test_save_tweet(self):
        try:
            # Aguardar e clicar no ícone do perfil
            print("Aguardando o ícone do perfil...")
            profile_icon = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[10]/div"))
            )
            profile_icon.click()
            print("Perfil acessado.")

            # Aguardar e localizar o tweet na timeline do perfil
            print("Aguardando o tweet aparecer no perfil...")
            tweet = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='ola mundo']"))
            )
            print("Tweet encontrado.")
            tweet.click()
        

            like_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[6]/div/div/div[4]/button"))
            )
            
            like_button.click()

           

            
            time.sleep(5)

        except Exception as e:
            print("Erro durante o teste de save do tweet.")
            self.driver.save_screenshot("save_tweet_test_error.png")
            raise e
    

        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
