# 1 - Bibliotecas
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


# 2 - Classe (Opcional)
class Teste_Produtos:
    # 2.1 Atributos
    url = "https://www.saucedemo.com"

    # 2.2 Funções e Métodos
    # Função faz e retorna algo
    # Métodos não precisam retornar valores
    def setup_method(self,method):           # metodo de inicialização dos testes
        self.driver = webdriver.Chrome()     # instancia o objeto do Selenium Webdriver como Chrome (Edge, Firefo, IE...)
        self.driver.implicitly_wait(10)      # define o tempo de espera padrão por elementos em 10 segundos

    def teardown_method(self, method):       # metodo de finalização dos testes
        self.driver.quit()                   # encerra o objeto do selenium webdrive da memoria
    
    def test_selecionar_produto(self):           # metodo de testes
        self.driver.get(self.url)                        # abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard-user")     # localiza e controla o elemento
        self.driver.find_element(By.ID, "password").send_keys("secret-sauce") # novamente, porem localizando e controlando a senha



# continua na proxima aula