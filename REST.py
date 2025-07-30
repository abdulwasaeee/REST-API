from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

items={
    1:{"name": "pen"},
    2:{"name": "pencil"},
    3:{"name": "eraser"},
    4:{"name": "sharpner"},
}

@app.route('/')
def home():
    return "Home Page"

@app.route('/items',methods=['GET'])
def allitems():
    return jsonify(items)

@app.route('/items/<int:itemid>',methods=['GET'])
def anitem(itemid):
    item=items.get(itemid)
    if item:
        return jsonify({itemid:item})
    return jsonify({"error": "Item not found"})


@app.route('/items',methods=['POST'])
def additem():
    item=request.get_json()
    if not item or 'name' not in item:
        return jsonify({"error": "Invalid item data"})
    id= max(items.keys()) + 1
    items[id] = {"name": item['name']}
    return jsonify({id: items[id]})

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Missing item name"}), 400

    items[item_id]["name"] = data["name"]
    return jsonify({item_id: items[item_id]})

# Delete item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in items:
        deleted = items.pop(item_id)
        return jsonify({"message": "Item deleted", item_id: deleted})
    return jsonify({"error": "Item not found"})


    

if __name__ == '__main__':
    app.run(debug=True)
