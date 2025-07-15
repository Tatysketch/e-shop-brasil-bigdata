import streamlit as st
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime # Importar datetime no topo

# Função para conectar ao MongoDB
@st.cache_resource
def get_database():
    # A conexão usa 'localhost' pois a aplicação Streamlit roda na sua máquina host
    # e se conecta à porta mapeada do contêiner MongoDB (27017)
    client = MongoClient("mongodb://mongodb:27017/")
    db = client['e_shop_db'] # Nome do banco de dados
    return db

# Conectar ao banco de dados e coleções
db = get_database()
collection = db['produtos'] # Coleção de produtos
clientes_collection = db['clientes']
pedidos_collection = db['pedidos'] # Coleção de pedidos (espaço removido)

st.title("E-Shop Brasil - Catálogo de Produtos")

st.write("---")
st.subheader("Adicionar Novo Produto")

with st.form("produto_form"):
    nome = st.text_input("Nome do Produto")
    categoria = st.text_input("Categoria")
    preco = st.number_input("Preço", min_value=0.01, format="%.2f")
    quantidade = st.number_input("Quantidade em Estoque", min_value=0, step=1)
    
    submitted = st.form_submit_button("Adicionar Produto")
    if submitted:
        produto_data = {
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade_estoque": quantidade
        }
        try:
            collection.insert_one(produto_data)
            st.success(f"Produto '{nome}' adicionado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao adicionar produto: {e}")

st.write("---")
st.subheader("Produtos no Catálogo")

# Exibir produtos existentes
produtos = list(collection.find())
if produtos:
    for produto in produtos:
        st.write(f"Nome: {produto.get('nome')}")
        st.write(f"Categoria: {produto.get('categoria')}")
        st.write(f"Preço: R$ {produto.get('preco'):.2f}")
        st.write(f"Estoque: {produto.get('quantidade_estoque')}")
        st.write("---")
else:
    st.info("Nenhum produto cadastrado ainda.")

st.write("---")
st.subheader("Remover Produto")

with st.form("remover_produto_form"):
    nome_remover = st.text_input("Nome do Produto para Remover")

    submitted_remove = st.form_submit_button("Remover Produto")
    if submitted_remove:
        if nome_remover:
            resultado = collection.delete_one({"nome": nome_remover})
            if resultado.deleted_count > 0:
                st.success(f"Produto '{nome_remover}' removido com sucesso!")
            else:
                st.warning(f"Produto '{nome_remover}' não encontrado no catálogo.")
        else:
            st.error("Por favor, digite o nome do produto para remover.")

st.write("---")
st.subheader("Gerenciar Clientes")

with st.form("cliente_form"):
    cliente_nome = st.text_input("Nome do Cliente")
    cliente_email = st.text_input("Email do Cliente")

    submitted_cliente = st.form_submit_button("Adicionar Cliente")
    if submitted_cliente:
        if cliente_nome and cliente_email:
            cliente_data = {
                "nome": cliente_nome,
                "email": cliente_email
            }
            try:
                clientes_collection.insert_one(cliente_data)
                st.success(f"Cliente '{cliente_nome}' adicionado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao adicionar cliente: {e}")
        else:
            st.error("Por favor, preencha o nome e o email do cliente.")

st.write("---")
st.subheader("Clientes Cadastrados")

clientes = list(clientes_collection.find())
if clientes:
    for cliente in clientes:
        st.write(f"Nome: {cliente.get('nome')}, Email: {cliente.get('email')}")
    st.write("---")
else:
    st.info("Nenhum cliente cadastrado ainda.")
    
st.write("---")
st.subheader("Adicionar Novo Pedido")

# Para adicionar um pedido, precisamos de clientes e produtos existentes.
todos_clientes = list(clientes_collection.find({}, {"_id": 1, "nome": 1}))
todos_produtos = list(collection.find({}, {"_id": 1, "nome": 1}))

with st.form("adicionar_pedido_form"):
    if not todos_clientes:
        st.warning("Adicione clientes antes de criar pedidos.")
    if not todos_produtos:
        st.warning("Adicione produtos antes de criar pedidos.")

    if todos_clientes and todos_produtos:
        cliente_nomes = {str(c['_id']): c['nome'] for c in todos_clientes}
        produto_nomes = {str(p['_id']): p['nome'] for p in todos_produtos}

        cliente_id_selecionado_str = st.selectbox(
            "Selecione o Cliente:",
            options=list(cliente_nomes.keys()),
            format_func=lambda x: cliente_nomes[x],
            key="pedido_cliente_select"
        )

        produtos_ids_selecionados_str = st.multiselect(
            "Selecione os Produtos:",
            options=list(produto_nomes.keys()),
            format_func=lambda x: produto_nomes[x],
            key="pedido_produtos_multiselect"
        )

        quantidade_pedido = st.number_input(
            "Quantidade para cada produto no pedido",
            min_value=1,
            value=1,
            step=1,
            key="pedido_quantidade_input"
        )

    submitted_pedido = st.form_submit_button("Adicionar Pedido")

    if submitted_pedido:
        if not todos_clientes or not todos_produtos:
            st.error("Não é possível criar pedidos sem clientes e produtos.")
        elif cliente_id_selecionado_str and produtos_ids_selecionados_str:
            cliente_id_obj = ObjectId(cliente_id_selecionado_str)
            produtos_para_pedido = []
            for p_id_str in produtos_ids_selecionados_str:
                produtos_para_pedido.append({
                    "produto_id": ObjectId(p_id_str),
                    "quantidade": quantidade_pedido
                })

            pedido_data = {
                "cliente_id": cliente_id_obj,
                "produtos": produtos_para_pedido,
                "data_pedido": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            try:
                pedidos_collection.insert_one(pedido_data)
                st.success("Pedido adicionado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao adicionar pedido: {e}")
        else:
            st.error("Por favor, selecione um cliente e pelo menos um produto.")

    else:
        pass


st.write("---")
st.subheader("Pedidos Realizados (Concatenado)")

# Para a concatenação, vamos usar o pipeline de agregação do MongoDB
pipeline = [
    {
        "$lookup": {
            "from": "clientes",
            "localField": "cliente_id",
            "foreignField": "_id",
            "as": "cliente_info"
        }
    },
    {
        "$unwind": "$cliente_info"
    },
    {
        "$unwind": "$produtos"
    },
    {
        "$lookup": {
            "from": "produtos",
            "localField": "produtos.produto_id",
            "foreignField": "_id",
            "as": "produto_info"
        }
    },
    {
        "$unwind": "$produto_info"
    },
    {
        "$project": {
            "_id": 0,
            "ID_Pedido": "$_id",
            "Cliente": "$cliente_info.nome",
            "Email_Cliente": "$cliente_info.email",
            "Produto_Nome": "$produto_info.nome",
            "Produto_Preco": "$produto_info.preco",
            "Quantidade_Comprada": "$produtos.quantidade",
            "Data_Pedido": "$data_pedido"
        }
    }
]

pedidos_com_detalhes = list(pedidos_collection.aggregate(pipeline))

if pedidos_com_detalhes:
    st.write("### Detalhes de Pedidos:")
    for pedido in pedidos_com_detalhes:
        st.write(f"Pedido ID: {pedido.get('ID_Pedido')}")
        st.write(f"Cliente: {pedido.get('Cliente')} ({pedido.get('Email_Cliente')})")
        st.write(f"Produto: {pedido.get('Produto_Nome')} - R$ {pedido.get('Produto_Preco'):.2f}")
        st.write(f"Quantidade: {pedido.get('Quantidade_Comprada')}")
        st.write(f"Data do Pedido: {pedido.get('Data_Pedido')}")
        st.write("---")
else:
    st.info("Nenhum pedido registrado ainda.")