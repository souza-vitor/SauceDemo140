# 1- Bibliotecas / Imports
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Edge()         #instanciar o obj do Selenium WebDriver especializado para o Chrome
    context.driver.maximize_window()            #maximizar a janela do navegador
    context.driver.implicitly_wait(10)          # esperar até 10 segundos por qualquer elemento
    # Passo em si
    context.driver.get("https://www.saucedemo.com") # abrir o navegador no endereço do site alvo

# com usuario e senha
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  #preencher usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)     #preencher senha
    context.driver.find_element(By.ID, "login-button").click()          #clicar no botão login

# sem usuario
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
    # não preenche usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)     #preencher senha
    context.driver.find_element(By.ID, "login-button").click()          #clicar no botão login

# sem senha
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)  #preencher usuario
    #não preenche senha
    context.driver.find_element(By.ID, "login-button").click()          #clicar no botão login

# sem usuario e senha
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
    #não preenche usuario
    #não preenche senha
    context.driver.find_element(By.ID, "login-button").click()          #clicar no botão login

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    #time.sleep(2) #remover depois

    # teardown / encerramento
    context.driver.quit()


@then(u'exibe uma mensagem de erro no login')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

    # teardown / encerramento
    context.driver.quit()

# mensagem de erro para o scenario outline
@then(u'exibe uma {mensagem} de erro no login')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem

    # teardown / encerramento
    context.driver.quit()


# cenario checagem de compra

@when(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"


@when(u'seleciono o produto Sauce Labs Backpack e clico no carrinho')
def step_impl(context):
    assert context.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack" # confirma se está escrito Sauce Labs Backpack no elemento
    assert context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").text == "Add to cart" # confirma se é o botão correto para adicionar a mochila no carrinho
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    context.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

@then(u'sou direcionado para a pagina Your Cart')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Your Cart"


@then(u'vejo o produto Sauce Labs Backpack com quantidade 1 e preço $29.99')
def step_impl(context):
     assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == "Sauce Labs Backpack"
     assert context.driver.find_element(By.CSS_SELECTOR, ".cart_quantity").text == "1"
     assert context.driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text == "$29.99"

@then(u'faço o logout')
def step_impl(context):
    context.driver.find_element(By.ID, "remove-sauce-labs-backpack").click() #remove o item
    context.driver.find_element(By.ID, "react-burger-menu-btn").click() # clica no menu
    context.driver.find_element(By.ID, "logout_sidebar_link").click() # faz o logout
    
    # teardown / encerramento
    context.driver.quit()