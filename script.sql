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