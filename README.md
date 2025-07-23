# Sauce Demo - Testes Automatizados

Este projeto contém testes automatizados para o site [Sauce Demo](https://www.saucedemo.com), utilizando as ferramentas Selenium WebDriver, Behave (BDD) e Pytest. O objetivo é validar o fluxo de login, seleção de produto e operações no carrinho de compras.

## Ferramentas Utilizadas

- **Python**: Linguagem principal dos testes.
- **Selenium WebDriver**: Automação de browsers para testes end-to-end.
- **Behave**: Framework BDD para escrita de cenários em linguagem natural.
- **Pytest**: Framework para execução de testes automatizados.
- **Edge WebDriver**: Driver utilizado para automação do navegador Microsoft Edge.

## Estrutura do Projeto

```
.gitignore
test_selecionar_produto_swd.py
test_selecionar_produto.py
features/
    selecionar_produto.feature
    steps/
        selecionar_produto.py
```

- Os testes BDD estão em `features/` e implementados em `features/steps/selecionar_produto.py`.
- Testes diretos com Selenium estão em `test_selecionar_produto.py` e `test_selecionar_produto_swd.py`.

## Como Executar Localmente

1. **Clone o repositório e acesse a pasta do projeto:**
   ```sh
   git clone <url-do-repositorio>
   cd SauceDemo140
   ```

2. **Crie um ambiente virtual e ative:**
   ```sh
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/Mac:
   source .venv/bin/activate
   ```

3. **Instale as dependências:**
   ```sh
   pip install selenium behave pytest
   ```

4. **Baixe o Edge WebDriver** compatível com sua versão do navegador e adicione ao PATH.

5. **Execute os testes:**

   - **Testes BDD (Behave):**
     ```sh
     behave features/selecionar_produto.feature
     ```

   - **Testes Pytest:**
     ```sh
     pytest test_selecionar_produto.py
     pytest test_selecionar_produto_swd.py
     ```

## Observações

- Certifique-se de que o Edge WebDriver está instalado e configurado no PATH do sistema.
- Os testes abrem o navegador automaticamente e realizam as ações conforme os cenários definidos.

---
