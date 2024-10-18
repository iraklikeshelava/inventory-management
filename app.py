from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__, static_url_path='')

# Serve the index.html for the root route
@app.route('/')
def index():
    return render_template('index.html')

# API to get inventory items
@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    conn.close()
    return jsonify(items)


# Connect to database
def connect_db():
    conn = sqlite3.connect('inventory.db')
    return conn

# Add new inventory item
@app.route('/api/inventory', methods=['POST'])
def add_inventory():
    data = request.get_json()
    name = data['name']
    quantity = data['quantity']
    warehouse_id = data['warehouseId']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory (name, quantity, warehouseId) VALUES (?, ?, ?)",
                   (name, quantity, warehouse_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Item added successfully"}), 201

# Update inventory item
@app.route('/api/inventory/<int:item_id>', methods=['PUT'])
def update_inventory(item_id):
    data = request.get_json()
    name = data['name']
    quantity = data['quantity']
    warehouse_id = data['warehouseId']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE inventory SET name = ?, quantity = ?, warehouseId = ? WHERE id = ?",
                   (name, quantity, warehouse_id, item_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Item updated successfully"})

# Delete inventory item
@app.route('/api/inventory/<int:item_id>', methods=['DELETE'])
def delete_inventory(item_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Item deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True, port= 8000)
