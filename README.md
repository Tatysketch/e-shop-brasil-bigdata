# e-shop-brasil-bigdata 
Estudo de Caso: Aplicação de Tecnologias de Banco de Dados e Big Data na E-Shop Brasil.

## 🚀 Funcionalidades da Aplicação

O E-Shop Brasil oferece uma interface intuitiva e responsiva para explorar dados de vendas e produtos. As principais funcionalidades incluem:

* **Visualização do Catálogo de Produtos:** Exibe todos os produtos disponíveis, com informações detalhadas como nome, categoria, preço e quantidade em estoque.
* **Cadastro de Produtos:** Permite o registro de novos produtos no catálogo, incluindo informações essenciais como categoria, valor (preço) e quantidade.
* **Gerenciamento de Produtos:** Habilidade de remover produtos existentes do catálogo, útil para itens fora de estoque ou que não serão mais comercializados.
* **Cadastro de Clientes:** Funcionalidade para registrar novos clientes, solicitando informações como nome e e-mail.
* **Registro e Visualização de Pedidos:** Permite a criação de novos pedidos que são automaticamente registrados e exibidos em uma lista de "Pedidos Realizados", cada um identificado por um ID único.
* **Análise de Vendas:** Apresenta gráficos e métricas sobre o desempenho das vendas, como total de vendas, produtos mais vendidos, etc. (Esta funcionalidade será desenvolvida em etapas futuras).
* **Interatividade:** Gráficos e tabelas interativas que permitem explorar os dados de diferentes ângulos (Esta funcionalidade será desenvolvida em etapas futuras).

## ⚙️ Configuração e Instalação

Siga os passos abaixo para configurar e executar a aplicação E-Shop Brasil em seu ambiente local.

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em seu sistema:

* **Docker Desktop:** Essencial para gerenciar os contêineres Docker (incluindo o MongoDB).
    * [Baixar Docker Desktop](https://www.docker.com/products/docker-desktop/)
* **Git Bash (ou terminal compatível):** Para executar comandos Git e Docker.
    * [Baixar Git Bash](https://git-scm.com/downloads)
* **Python (versão 3.x):** Para executar a aplicação Streamlit.
    * [Baixar Python](https://www.python.org/downloads/)
* **Pip (gerenciador de pacotes Python):** Geralmente vem com a instalação do Python.

### Passos para Instalação

1.  **Clone o Repositório:**
    Abra seu Git Bash e clone o projeto para o seu computador:
    ```bash
    git clone https://github.com/Tatysketch/e-shop-brasil-bigdata.git
    ```

2.  **Navegue até a Pasta do Projeto:**
    Após clonar, entre na pasta do projeto. Use o caminho onde você salvou ou clonou o projeto. Lembre-se de usar aspas se houver espaços no caminho:
    ```bash
    cd "C:\Users\Ola chatinha\e-shop-brasil-bigdata"
    ```

3.  **Inicie o Serviço MongoDB com Docker Compose:**
    Com o Docker Desktop aberto e funcionando, execute o comando para iniciar o contêiner do MongoDB:
    ```bash
    docker-compose up -d
    ```
    Aguarde alguns segundos para o MongoDB iniciar completamente.

4.  **Instale as Dependências Python:**
    Instale as bibliotecas Python necessárias para a aplicação Streamlit. Certifique-se de estar na pasta do projeto:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute a Aplicação Streamlit:**
    Finalmente, inicie a interface da aplicação:
    ```bash
    streamlit run app.py
    ```
 🖼️ **Exemplos Visuais da Aplicação**

Abaixo estão capturas de tela que demonstram o funcionamento da aplicação, organizadas de acordo com o fluxo de uso:

🔹 **1. Cadastro de Produto**  
📂 `exemplos/cadastro/01_formulario_produto_preenchido.png`  
Tela de cadastro preenchido de um novo produto.

---

🔹 **2. Cadastro de Cliente**  
📂 `exemplos/cadastro/04_adicionar_cliente_interface.png`  
Interface para cadastro de um novo cliente.

---

🔹 **3. Visualização de Produtos**  
📂 `exemplos/visualizacao/01_produtos_cadastrados_dashboards.png`  
Visualização dos produtos cadastrados em formato de dashboard.

---

🔹 **4. Visualização de Clientes**  
📂 `exemplos/visualizacao/02_clientes_ativos.png`  
Lista de clientes ativos cadastrados no sistema.

---

🔹 **5. Adicionar Pedido**  
📂 `exemplos/pedidos/01_tela_adicionar_pedido_ativa.png`  
Tela de criação de um novo pedido.

---

🔹 **6. Visualização de Pedidos Realizados**  
📂 `exemplos/pedidos/02_resumo_pedido_completo.png`  
Resumo detalhado de um pedido já realizado.

---


### ✅ Organização Interna dos Prints

Os prints estão organizados em subpastas dentro da pasta `exemplos/`, conforme a funcionalidade:
```
exemplos/
    cadastro/
        produto_form.png
        cliente_form.png
    visualizacao/
        produtos_lista.png
        clientes_lista.png
    pedidos/
        adicionar_pedido.png
        resumo_pedido.png
```

---

👩‍💻 **Sou Tatielle Pereira**  
Estudante da disciplina **Advanced Database and Big Data**  
na faculdade **Unifecaf** 🚀💙  

---

📚 Este estudo de caso foi uma ótima oportunidade  
para mergulhar no universo do **Big Data** e **bancos de dados**. 🚀

---


