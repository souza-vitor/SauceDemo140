Feature: Selecionar Produto

    Scenario: Selecionar produto "Sauce Labs Backpack"
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha secret_sauce
        Then sou direcionado para pagina Home

    Scenario: Selecionar produto e checar carrinho
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha secret_sauce
        And sou direcionado para pagina Home
        And seleciono o produto Sauce Labs Backpack e clico no carrinho
        Then sou direcionado para a pagina Your Cart
        And vejo o produto Sauce Labs Backpack com quantidade 1 e preço $29.99
        And faço o logout

    Scenario: Login com a senha invalida
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha errada
        Then exibe uma mensagem de erro no login

    Scenario Outline: Login Negativo
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario <usuario> e senha <senha> 
        Then exibe uma <mensagem> de erro no login

        Examples:
        | id | usuario       | senha         | mensagem                                                                  |
        | 1  | standard_user | laranja       | Epic sadface: Username and password do not match any user in this service |
        | 2  | standard_user |               | Epic sadface: Password is required                                        |
        | 3  |               | secret_sauce  | Epic sadface: Username is required                                        |
        | 4  | juca          | secret_sauce  | Epic sadface: Username and password do not match any user in this service |
        | 5  | juca          | laranja       | Epic sadface: Username and password do not match any user in this service |
        | 6  | juca          |               | Epic sadface: Password is required                                        |
        | 7  |               |               | Epic sadface: Username is required                                        |
        | 8  |               | laranja       | Epic sadface: Username is required                                        |