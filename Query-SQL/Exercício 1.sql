-- Criação das tabelas

CREATE TABLE CLIENTES (
    nome				varchar(250) NOT NULL,
    data_nascimento	date NOT NULL,
    data_atualizacao	date,
    data_cadastro		date NOT NULL,
    nome_pai			varchar(250) NOT NULL,
    nome_mae			varchar(250) NOT NULL,
    cpf				text NOT NULL,
    rg				text,
    cidade			varchar(50),
    bairro			varchar(50),
    estado			varchar(50),
    cep				text,
    idade				int,
    sexo				varchar(1),
    PRIMARY KEY (cpf)
);

CREATE TABLE PRODUTOS (
    id_produto        serial,
    nome              varchar(250) NOT NULL,
    descricao         text,
    preco             numeric(10, 2) NOT NULL,
    estoque           int NOT NULL,
    data_cadastro     date NOT NULL
    PRIMARY KEY (id_produto)
);

CREATE TABLE PEDIDOS (
    id_pedido         serial,
    cpf_cliente       text NOT NULL,
    data_pedido       date NOT NULL,
    valor_total       numeric(10, 2) NOT NULL,
    data_entrega      date,
    status_pedido     varchar(50),
    data_atualizacao  date,
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (cpf_cliente) REFERENCES CLIENTES (cpf)
);

CREATE TABLE ITENS_PEDIDO (
    id_item           serial,
    id_pedido         int NOT NULL,
    id_produto        int NOT NULL,
    quantidade        int NOT NULL,
    preco_unitario    numeric(10, 2) NOT NULL,
    PRIMARY KEY (id_item),
    FOREIGN KEY (id_pedido) REFERENCES PEDIDOS (id_pedido),
    FOREIGN KEY (id_produto) REFERENCES PRODUTOS (id_produto)
);
