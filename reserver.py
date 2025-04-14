from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to represent database
users = []
classes = [
    {'id': 1, 'name': 'English Basics', 'date': '2025-04-01', 'time': '10:00', 'capacity': 10, 'teacher': 'John Smith'}
]
reservations = []


@app.route('/register', methods=['POST'])
def register():
    """User Registration"""
    data = request.json
    user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone'],
        'password': data['password']
    }
    users.append(user)
    return jsonify({'message': 'User registered successfully', 'user': user})


@app.route('/classes', methods=['GET'])
def get_classes():
    """Get Available Classes"""
    return jsonify(classes)


@app.route('/reserve', methods=['POST'])
def reserve_class():
    """Reserve a Class"""
    data = request.json
    class_id = data['class_id']
    user_id = data['user_id']

    # Check if class is available
    for cls in classes:
        if cls['id'] == class_id and cls['capacity'] > 0:
            reservations.append({'id': len(reservations) + 1, 'user_id': user_id, 'class_id': class_id})
            cls['capacity'] -= 1
            return jsonify({'message': 'Reservation successful', 'reservation': reservations[-1]})

    return jsonify({'message': 'Class fully booked or not found'}), 400


if __name__ == '__main__':
    app.run(debug=True)
