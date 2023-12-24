from flask import Flask, jsonify, request

app = Flask(__name__)

# Списки для зберігання даних
users = []
categories = []
expenses = []

# Ендпойнт для створення користувача
@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    users.append(user_data)
    return jsonify(user_data), 201

# Ендпойнт для видалення користувача
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user.get('id') != user_id]
    return jsonify({'message': 'Користувача видалено'}), 200

# Ендпойнт для отримання списку користувачів
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Ендпойнт для створення категорії витрат
@app.route('/category', methods=['POST'])
def create_category():
    category_data = request.get_json()
    categories.append(category_data)
    return jsonify(category_data), 201

# Ендпойнт для видалення категорії витрат
@app.route('/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    global categories
    categories = [category for category in categories if category.get('id') != category_id]
    return jsonify({'message': 'Категорію видалено'}), 200

# Ендпойнт для отримання списку категорій
@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(categories)

# Ендпойнт для створення запису про витрати
@app.route('/expense', methods=['POST'])
def create_expense():
    expense_data = request.get_json()
    expenses.append(expense_data)
    return jsonify(expense_data), 201

# Ендпойнт для видалення запису про витрати
@app.route('/expense/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    global expenses
    expenses = [expense for expense in expenses if expense.get('id') != expense_id]
    return jsonify({'message': 'Запис про витрати видалено'}), 200

# Ендпойнт для отримання записів про витрати з певними параметрами
@app.route('/record', methods=['GET'])
def get_records():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')
    # Фільтрація записів за вказаними параметрами
    filtered_expenses = [expense for expense in expenses if 
                         (expense.get('user_id') == int(user_id) if user_id else True) and 
                         (expense.get('category_id') == int(category_id) if category_id else True)]
    return jsonify(filtered_expenses), 200

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True)
