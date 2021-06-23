# Importar librería Flask 
from flask import Flask, jsonify, request

# Ejecutar aplicación Flask
app = Flask(__name__)

# Importar lista de productos
from products import products


# Ruta de prueba
@app.route('/ping')

# Método de prueba
def ping():
    return jsonify({"response": "Pong!"}) 


# Ruta para obtener todos los productos
@app.route('/products', methods=['GET'])

# Método para obtener todos los productos
def get_products():
    return jsonify({"response": "Product's List", "products": products})


# Ruta para obtener un producto
@app.route('/products/<string:product_name>')

# Método para obtener un producto
def get_product(product_name):
    products_found = [product for product in products if product['name'] == product_name]
    if (len(products_found) > 0):
        return jsonify({"response": "Product", "name": products_found})
    return jsonify({"response": "Product not found"}) 


# Ruta para añadir un producto
@app.route('/products', methods=['POST'])

# Método para añadir un producto
def add_product():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"response": "Product added successfully", "products": products}) 


# Ruta para editar un producto
@app.route('/products/<string:product_name>', methods=['PUT'])

# Método para editar un producto
def edit_product(product_name):
    products_found = [product for product in products if product['name'] == product_name]
    if (len(products_found) > 0):
        products_found[0]['name'] = request.json['name']
        products_found[0]['price'] = request.json['price']
        products_found[0]['quantity'] = request.json['quantity']
        return jsonify({
            "response": "Product updated",
            "product": products_found[0]})
    return jsonify({"response": "Product not found"}) 


# Ruta para eliminar un producto
@app.route('/products/<string:product_name>', methods=['DELETE'])

# Método para eliminar un producto
def delete_product(product_name):
    products_found = [product for product in products if product['name'] == product_name]
    if (len(products_found) > 0):
        products.remove(products_found[0])
        return jsonify({
            "response": "Product deleted",
            "products": products})
    return jsonify({"response": "Product not found"}) 


if __name__ == '__main__':
    app.run(debug=True, port=4000)