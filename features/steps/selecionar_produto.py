# 1- Bibliotecas / Imports
from behave import given, when, then
from selenium import webdriver

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Chrome()         #instanciar o obj do Selenium WebDriver especializado para o Chrome
    context.driver.maximize_window(1600, 500)   #maximizar a janela do navegador
    context.driver.implicitly_wait(10)          # esperar até 10 segundos por qualquer elemento
    # Passo em si
    context.driver.get("https://www.saucedemo.com") # abrir o navegador no endereço do site alvo

@when(u'preencho os campos de login com usuario standard_user e senha secret_sauce')
def step_impl(context):
    


@then(u'sou direcionado para pagina Home')
def step_impl(context):
    
