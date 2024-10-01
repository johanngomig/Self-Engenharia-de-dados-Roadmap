-- Criação de Joins

-- Recuperar todos os pedidos feitos por cada cliente
SELECT clientes.nome, pedidos.id_pedido, pedidos.valor_total
FROM CLIENTES
INNER JOIN PEDIDOS ON clientes.cpf = pedidos.cpf_cliente;

-- Listar todos os produtos comprados em cada pedido
SELECT pedidos.id_pedido, clientes.nome, produtos.nome, itens_pedido.quantidade
FROM PEDIDOS
INNER JOIN ITENS_PEDIDO ON pedidos.id_pedido = itens_pedido.id_pedido
INNER JOIN PRODUTOS ON itens_pedido.id_produto = produtos.id_produto
INNER JOIN CLIENTES ON pedidos.cpf_cliente = clientes.cpf;

-- Recuperar clientes que ainda não fizeram nenhum pedido
SELECT clientes.nome
FROM CLIENTES
LEFT JOIN PEDIDOS ON clientes.cpf = pedidos.cpf_cliente
WHERE pedidos.id_pedido IS NULL;

-- Produtos que ainda não foram comprados em nenhum pedido
SELECT produtos.nome
FROM PRODUTOS
LEFT JOIN ITENS_PEDIDO ON produtos.id_produto = itens_pedido.id_produto
WHERE itens_pedido.id_produto IS NULL;

-- Total gasto por cada cliente
SELECT clientes.nome, SUM(pedidos.valor_total) AS total_gasto
FROM CLIENTES
INNER JOIN PEDIDOS ON clientes.cpf = pedidos.cpf_cliente
GROUP BY clientes.nome;

-- Recuperar o nome dos clientes e o status de seus pedidos
SELECT clientes.nome, pedidos.status_pedido AS status
from CLIENTES
INNER JOIN PEDIDOS ON clientes.cpf = pedidos.cpf_cliente

-- Identificar os clientes que compraram um produto específico
SELECT clientes.nome
FROM CLIENTES
INNER JOIN PEDIDOS ON clientes.cpf = pedidos.cpf_cliente
INNER JOIN ITENS_PEDIDO ON pedidos.id_pedido = itens_pedido.id_pedido
INNER JOIN PRODUTOS ON itens_pedido.id_produto = produtos.id_produto
WHERE produtos.nome = 'Notebook';

-- Contabilizar o número de pedidos feitos por cada cliente
SELECT clientes.nome, COUNT(pedidos.id_pedido) AS total_pedidos
FROM CLIENTES
INNER JOIN PEDIDOS ON clientes.cpf = pedidos.cpf_cliente
GROUP BY clientes.nome

-- Listar os produtos mais vendidos
SELECT produtos.nome, SUM(itens_pedido.quantidade) AS total_vendido
FROM PRODUTOS
INNER JOIN ITENS_PEDIDO ON produtos.id_produto = itens_pedido.id_produto
GROUP BY produtos.nome
ORDER BY total_vendido DESC
