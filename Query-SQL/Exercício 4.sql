-- Criação de CTEs

-- Recuperar o total de produtos vendidos por cada cliente
WITH Total_Itens AS (
    SELECT pedidos.cpf_cliente, SUM(itens_pedido.quantidade) AS total_produtos
    FROM PEDIDOS
    INNER JOIN ITENS_PEDIDO ON pedidos.id_pedido = itens_pedido.id_pedido
    GROUP BY pedidos.cpf_cliente
)
SELECT clientes.nome, Total_Itens.total_produtos
FROM CLIENTES
INNER JOIN Total_Itens ON clientes.cpf = Total_Itens.cpf_cliente;

-- Econtrar o cliente que gastou mais em pedidos
WITH Total_Gasto AS (
    SELECT pedidos.cpf_cliente, SUM(pedidos.valor_total) AS total_gasto
    FROM PEDIDOS
    GROUP BY pedidos.cpf_cliente
)
SELECT clientes.nome, Total_Gasto.total_gasto
FROM CLIENTES
INNER JOIN Total_Gasto ON clientes.cpf = Total_Gasto.cpf_cliente
ORDER BY Total_Gasto.total_gasto DESC
LIMIT 1;
