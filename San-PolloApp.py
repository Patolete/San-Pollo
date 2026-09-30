from calendar import c
from datetime import datetime
from flask import Flask, request, render_template, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'caroAprobame'

def get_db():
    conexion = sqlite3.connect('sanpollo.db')
    conexion.row_factory = sqlite3.Row
    return conexion

def init_db():
    conexion = get_db()
    with open('schema.sql', encoding='utf-8') as f:
        conexion.executescript(f.read())
    conexion.commit()
    conexion.close()

@app.route('/agregar/<int:producto_id>', methods=['POST'])
def carro(producto_id):
    if 'carrito' not in session:
        session['carrito'] = []
    cantidad =int(request.form['cantidad'])
    session['carrito'].append({'producto_id': producto_id, 'cantidad': cantidad})
    session.modified = True
    return redirect(request.referrer or url_for('home'))

@app.route('/')
def home():
    return render_template('index.html')

#Rutas de paginas
@app.route('/platos')
def platos():
    conexion = get_db()
    platos = conexion.execute('SELECT * FROM productos where categoria = ?', ('comida',)).fetchall()
    conexion.close()
    return render_template('platos.html', platos=[dict(p) for p in platos])

@app.route('/cervezas')
def cervezas():
    conexion = get_db()
    cervezas = conexion.execute('SELECT * FROM productos WHERE categoria = ?', ('cerveza',)).fetchall()
    conexion.close()
    return render_template('cervezas.html', cervezas=[dict(c) for c in cervezas])

@app.route('/postres')
def postres():
    conexion = get_db()
    postres = conexion.execute('SELECT * FROM productos WHERE categoria = ?', ('postre',)).fetchall()
    conexion.close()
    return render_template('postres.html', postres=[dict(p) for p in postres])

@app.route('/bebidas')
def bebidas():
    conexion = get_db()
    bebidas = conexion.execute('SELECT * FROM productos WHERE categoria = ?', ('bebida',)).fetchall()
    conexion.close()
    return render_template('bebidas.html', bebidas=[dict(b) for b in bebidas])

@app.route('/carrito')
def carrito():
    carrito = session.get('carrito', [])
    conexion = get_db()
    produ = []
    total = 0
    for i in carrito:
        producto = conexion.execute('SELECT nombre, precio FROM productos WHERE id = ?', (i['producto_id'],)).fetchone()
        producto = dict(producto)
        producto['cantidad'] = i['cantidad']
        produ.append(producto)
        total += producto['precio'] * producto['cantidad']
    conexion.close()
    return render_template('carrito.html', productos=produ, total=total)

#----------------------

@app.route('/productos')
def listar_productos():
    conexion = get_db()
    productos = conexion.execute('SELECT * FROM productos').fetchall()
    conexion.close()
    return [dict(p) for p in productos]

@app.route('/pedido', methods=['POST'])
def crear_pedido():
    items = session.get('carrito', [])

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

    session['carrito'] = []

    return render_template('confirmacion.html', total=total, pedido_id=pedido_id)

@app.route('/jobView')
def ver_pedido():
    conexion = get_db()
    pedidos = conexion.execute(
        'SELECT * FROM pedidos where estado = ?', ('pendiente',)
    ).fetchall()
    conexion.close()
    return [dict(p) for p in pedidos]

@app.route('/ticket/<int:pedido_id>')
def ver_ticket(pedido_id):
    conexion = get_db()
    pedido = conexion.execute(
        'SELECT * FROM pedidos WHERE id = ?', (pedido_id,)
    ).fetchone()


    ticket = conexion.execute(
        '''SELECT productos.nombre, productos.precio, pedido_items.cantidad
        FROM pedido_items
        JOIN productos ON pedido_items.producto_id = productos.id
        WHERE pedido_items.pedido_id = ?''', (pedido_id,)
    ).fetchall()

    conexion.close()

    return {
        "pedido": dict(pedido),
        "items": [dict(t) for t in ticket]
    }


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
