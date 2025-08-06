CREATE DATABASE db_facturas;
USE db_facturas;
SHOW TABLES;
CREATE TABLE factura (
    fecha_factura DATE,
    cantidad INT,
    descripcion VARCHAR(255),
    valor_unitario FLOAT,
    descuento FLOAT
);
SELECT * FROM factura;
SELECT numero_factura, COUNT(*) FROM factura 
GROUP BY numero_factura;
ALTER TABLE factura
MODIFY COLUMN cantidad FLOAT;
ALTER TABLE factura
ADD COLUMN numero_factura VARCHAR(255);
ALTER TABLE factura
ADD COLUMN proveedor VARCHAR(255);

DELETE FROM factura; 


SELECT 
    DATE_FORMAT(fecha_factura, '%Y-%m') AS mes,
    COUNT(*) AS total_facturas,
    SUM(cantidad) AS total_productos,
    SUM(cantidad*valor_unitario*1.18) AS 'Total a pagar'
FROM 
    factura
GROUP BY 
    DATE_FORMAT(fecha_factura, '%Y-%m')
ORDER BY 
    mes;
    
DELETE FROM factura WHERE numero_factura = 'E0018320566145678';