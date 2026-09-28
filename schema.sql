CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    categoria TEXT NOT NULL,
    precio REAL NOT NULL,
    imagen TEXT
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
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Rubia clásica', 'cerveza', 1200.0, NULL);
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('IPA', 'cerveza', 1400.0, NULL);
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Roja', 'cerveza', 1300.0, NULL);
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Negra', 'cerveza', 1300.0, NULL);

-- Bebidas sin alcohol
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Limonada', 'bebida', 600.0, NULL);
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Coca Cola', 'bebida', 500.0, NULL);
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Sprite', 'bebida', 500.0, NULL);
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Agua sin gas', 'bebida', 350.0, NULL);

-- Comidas
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Pizza mozzarella', 'comida', 2200.0, NULL);
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Pizza especial', 'comida', 2600.0, NULL);
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Hamburguesa completa', 'comida', 1900.0, NULL);
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Papas clásicas', 'comida', 900.0, NULL);
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Papas con cheddar', 'comida', 1100.0, NULL);

-- Postres
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Tiramisú', 'postre', 950.0, NULL);
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Cheesecake de frutos rojos', 'postre', 950.0, NULL);
INSERT OR IGNORE INTO productos (nombre, categoria, precio, imagen) VALUES ('Copa helada', 'postre', 850.0, NULL);
