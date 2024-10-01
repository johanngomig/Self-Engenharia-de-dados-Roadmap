-- Inserindo valores nas tabelas

INSERT INTO CLIENTES (nome, data_nascimento, data_cadastro, nome_pai, nome_mae, cpf, rg, cidade, bairro, estado, cep, idade, sexo)
VALUES 
('João Silva', '1985-04-23', '2024-01-01', 'Carlos Silva', 'Maria Silva', '12345678901', 'MG1234567', 'Belo Horizonte', 'Centro', 'MG', '30140000', 39, 'M'),
('Ana Oliveira', '1990-06-15', '2024-02-10', 'José Oliveira', 'Clara Oliveira', '98765432100', 'SP1234567', 'São Paulo', 'Pinheiros', 'SP', '05422000', 34, 'F'),
('Pedro Santos', '1979-08-12', '2024-03-20', 'Rui Santos', 'Elena Santos', '32165498712', 'RJ9876543', 'Rio de Janeiro', 'Copacabana', 'RJ', '22041010', 45, 'M');

INSERT INTO PRODUTOS (nome, descricao, preco, estoque, data_cadastro)
VALUES
('Notebook', 'Notebook Dell Inspiron 15', 3500.00, 10, '2024-01-05'),
('Smartphone', 'iPhone 12', 4500.00, 20, '2024-01-10'),
('Tablet', 'Samsung Galaxy Tab S6', 2200.00, 15, '2024-01-15');

INSERT INTO PEDIDOS (cpf_cliente, data_pedido, valor_total, data_entrega, status_pedido, data_atualizacao)
VALUES
('12345678901', '2024-04-01', 3500.00, '2024-04-05', 'Entregue', '2024-04-06'),
('98765432100', '2024-04-10', 4500.00, '2024-04-12', 'Entregue', '2024-04-13'),
('32165498712', '2024-04-15', 2200.00, '2024-04-18', 'Em processamento', '2024-04-16');

INSERT INTO ITENS_PEDIDO (id_pedido, id_produto, quantidade, preco_unitario)
VALUES
(1, 1, 1, 3500.00),  -- Notebook para João Silva
(2, 2, 1, 4500.00),  -- iPhone para Ana Oliveira
(3, 3, 1, 2200.00);  -- Tablet para Pedro Santos

