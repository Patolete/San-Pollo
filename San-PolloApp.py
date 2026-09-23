from datetime import datetime
from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db():
    conexion = sqlite3.connect('sanpollo.db')
    conexion.row_factory = sqlite3.Row
    return conexion

def init_db():
    conexion = get_db()
    with open('schema.sql') as f:
        conexion.executescript(f.read())
    conexion.commit()
    conexion.close()

@app.route('/')
def home():
    return "Hola, funciona!"

@app.route('/productos')
def listar_productos():
    conexion = get_db()
    productos = conexion.execute('SELECT * FROM productos').fetchall()
    conexion.close()
    return [dict(p) for p in productos]

@app.route('/pedido', methods=['POST'])
def crear_pedido():
    datos = request.get_json()
    items = datos['items']

    conexion = get_db()
    total = 0

    for item in items:
        producto = conexion.execute(
            'SELECT precio FROM productos WHERE id = ?', (item['producto_id'],)
        ).fetchone()
        total += producto['precio'] * item['cantidad']

    fecha = datetime.now().isoformat()

    cursor = conexion.execute(
        'INSERT INTO pedidos (fecha, total) VALUES (?, ?)', (fecha, total)
    )

    pedido_id = cursor.lastrowid
    for item in items:
        conexion.execute(
            'INSERT INTO pedido_items (pedido_id, producto_id, cantidad) VALUES (?, ?, ?)',
            (pedido_id, item['producto_id'], item['cantidad'])
        )

    conexion.commit()
    conexion.close()

    return {"mensaje": "pedido creado", "pedido_id": pedido_id, "total": total}

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
