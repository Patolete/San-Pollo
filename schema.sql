CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT NOT NULL,
    precio REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    total REAL NOT NULL,
    estado TEXT NOT NULL DEFAULT 'pendiente'
);

CREATE TABLE IF NOT EXISTS pedido_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- Cervezas
INSERT INTO productos (nombre, categoria, precio) VALUES ('Rubia clásica', 'cerveza', 1200.0);
INSERT INTO productos (nombre, categoria, precio) VALUES ('IPA', 'cerveza', 1400.0);
INSERT INTO productos (nombre, categoria, precio) VALUES ('Roja', 'cerveza', 1300.0);
INSERT INTO productos (nombre, categoria, precio) VALUES ('Negra', 'cerveza', 1300.0);

-- Bebidas sin alcohol
INSERT INTO productos (nombre, categoria, precio) VALUES ('Limonada', 'bebida', 600.0);
INSERT INTO productos (nombre, categoria, precio) VALUES ('Coca Cola', 'bebida', 500.0);
INSERT INTO productos (nombre, categoria, precio) VALUES ('Sprite', 'bebida', 500.0);
INSERT INTO productos (nombre, categoria, precio) VALUES ('Agua sin gas', 'bebida', 350.0);

-- Comidas
INSERT INTO productos (nombre, categoria, precio) VALUES ('Pizza mozzarella', 'comida', 2200.0);
INSERT INTO productos (nombre, categoria, precio) VALUES ('Pizza especial', 'comida', 2600.0);
INSERT INTO productos (nombre, categoria, precio) VALUES ('Hamburguesa completa', 'comida', 1900.0);
INSERT INTO productos (nombre, categoria, precio) VALUES ('Papas clásicas', 'comida', 900.0);
INSERT INTO productos (nombre, categoria, precio) VALUES ('Papas con cheddar', 'comida', 1100.0);

-- Postres
INSERT INTO productos (nombre, categoria, precio) VALUES ('Tiramisú', 'postre', 950.0);
INSERT INTO productos (nombre, categoria, precio) VALUES ('Cheesecake de frutos rojos', 'postre', 950.0);
INSERT INTO productos (nombre, categoria, precio) VALUES ('Copa helada', 'postre', 850.0);
