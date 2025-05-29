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
        self.driver = webdriver.Edge()     # instancia o objeto do Selenium Webdriver como Chrome (Edge, Firefo, IE...)
        self.driver.implicitly_wait(10)      # define o tempo de espera padrão por elementos em 10 segundos

    def teardown_method(self, method):       # metodo de finalização dos testes
        self.driver.quit()                   # encerra o objeto do selenium webdrive da memoria
    
    def test_selecionar_produto(self):           # metodo de testes
        self.driver.get(self.url)                        # abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")     # localiza e controla o elemento
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce") # novamente, porem localizando e controlando a senha
        self.driver.find_element(By.ID, "login-button").click() #clique no botão login

        # transição de pagina
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products" # confirma se está escrito Products no elemento
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack" # confirma se está escrito Sauce Labs Backpack no elemento
        assert self.driver.find_element(By.CSS_SELECTOR, "div[class='inventory_list'] div:nth-child(1) div:nth-child(2) div:nth-child(2) div:nth-child(1)").text == "$29.99" # Confirma o preço da mochila
        assert self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").text == "Add to cart" # confirma se é o botão correto para adicionar a mochila no carrinho
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click() # adiciona no carrinho
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click() # clica no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Your Cart" # verifica se está na pagina de carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == "Sauce Labs Backpack" # verifica o nome do item
        assert self.driver.find_element(By.CSS_SELECTOR, ".cart_quantity").text == "1" # verifica a quantidade
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text == "$29.99" # verifica o preço
        assert self.driver.find_element(By.ID, "remove-sauce-labs-backpack").text == "Remove" # verifica se é o botão de remover
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click() #remove o item
        self.driver.find_element(By.ID, "react-burger-menu-btn").click() # clica no menu
        self.driver.find_element(By.ID, "logout_sidebar_link").click() # faz o logout
        
        
