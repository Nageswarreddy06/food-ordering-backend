from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Function to safely connect to your local MySQL server
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",         
        password="password", 
        port=3307,          # Add this line!
        database="food_ordering"
    )
# Updated Endpoint: Fetches live data from MySQL!
@app.route('/menu', methods=['GET'])
def get_menu():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True) # Returns data as a clean dictionary
        
        cursor.execute("SELECT * FROM menu_items")
        menu_data = cursor.fetchall()
        
        cursor.close()
        conn.close()
        return jsonify({"menu": menu_data}), 200
    except Exception as e:
        return jsonify({"error": "Database connection failed", "details": str(e)}), 500

@app.route('/order', methods=['POST'])
def place_order():
    data = request.get_json()
    if not data or 'item_id' not in data or 'quantity' not in data:
        return jsonify({"error": "Bad Request: Missing item_id or quantity"}), 400
        
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Insert the order directly into your database rows
        query = "INSERT INTO orders (item_id, quantity, status) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['item_id'], data['quantity'], 'Pending'))
        conn.commit()
        
        order_id = cursor.lastrowid
        cursor.close()
        conn.close()
        
        return jsonify({"message": "Order saved to database!", "order_id": order_id}), 201
    except Exception as e:
        return jsonify({"error": "Failed to save order", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)