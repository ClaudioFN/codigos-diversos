"""
Created Date: 11/12/2023
Last Update: 11/12/2023
Description: Operation test for an API using a store products as base
"""
# pip install flask
from flask import Flask, request

# Initialize the APP
app = Flask(__name__)

# Initialize the list of products
products = []

# Routes
## Route to create products ##
@app.route("/products/create", methods=['POST'])
def create():
    data = request.get_json()
    products.append(data)
    return {'product': data}

## Route to list the products ##
@app.route("/products", methods=['GET'])
def list():
    return {'products': products}

## Route to update a products ##
@app.route("/products/<int:id>/update", methods=['PUT'])
def update(id):
    data = request.get_json()
    productBefore = products[id]
    products[id] = data
    message = f'Product updated from {productBefore} to {products[id]}'
    return {'message': message }
    
## Route to delete a products ##
@app.route("/products/<int:id>/delete/", methods=['DELETE'])
def delete(id):
    productToDelete = products[id]
    products.pop(id)
    message =  'Product ', productToDelete, ' deleted!'
    return {'message': message }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)