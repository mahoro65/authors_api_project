from flask import Blueprint, request, jsonify
from authors_app.status_code import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED
import validators
from authors_app.models.user import User
from authors_app.extensions import db, bcrypt

# auth blueprint
auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

# implementing the user registration
@auth.route('/register', methods=['POST'])
def register_user():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    contact = data.get('contact')
    email = data.get('email')
    password = data.get('password')

    # Validation of the incoming requests
    if not first_name or not last_name or not contact or not password or not email:
        return jsonify({'error': 'All fields are required'}), HTTP_400_BAD_REQUEST

    # Validation for the password
    if len(password) < 8:
        return jsonify({'error': 'Password is too short'}), HTTP_400_BAD_REQUEST
    
    # Validation for the Email
    if not validators.email(email):
        return jsonify({'error': 'Email is not valid'}), HTTP_400_BAD_REQUEST

    # Making a query from the users package
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error': 'Email address already in use'}), HTTP_409_CONFLICT

    if User.query.filter_by(contact=contact).first() is not None:
        return jsonify({'error': 'Contact already in use'}), HTTP_409_CONFLICT

    # Storing new users to the database
    try:
        hashed_password = bcrypt.generate_password_hash(password)
        new_user = User(first_name=first_name, contact=contact, last_name=last_name, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()

        username = new_user.get_full_name()

        return jsonify({
            'message': f'{username} has been successfully created',
            'user': {
                'id': new_user.id,
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email,
                'contact': new_user.contact,
                'password': new_user.password
            }
        }), HTTP_201_CREATED

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR

# Get all users
@auth.route('/users/', methods=['GET'])
def get_all_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'contact': user.contact,
        }
        output.append(user_data)
    return jsonify({'users': output})

# Get a specific user
@auth.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    user_data = {
        'id': user.id,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'contact': user.contact,
    }
    return jsonify(user_data)

# Update a user
@auth.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.get_or_404(id)
        data = request.get_json()
        user.email = data.get('email', user.email)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.contact = data.get('contact', user.contact)
        password = data.get('password')
        if password:
            user.password = bcrypt.generate_password_hash(password).decode('utf-8')
        db.session.commit()
        return jsonify({'message': 'User updated successfully'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Delete a user
@auth.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete user', 'details': str(e)}), 500
