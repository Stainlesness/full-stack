from flask import Blueprint, request, jsonify, send_from_directory, current_app
from . import db
from .models import Student, Payment
from datetime import datetime
import logging
import os

routes = Blueprint('routes', __name__)

# Set up basic logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Serve React Frontend
@routes.route('/', defaults={'path': ''})
@routes.route('/<path:path>')
def serve_react(path):
    if path != "" and os.path.exists(os.path.join(current_app.static_folder, path)):
        return send_from_directory(current_app.static_folder, path)
    else:
        return send_from_directory(current_app.static_folder, 'index.html')

@routes.route('/students', methods=['GET'])
def get_students():
    try:
        logging.debug('Fetching students...')
        grade = request.args.get('grade')
        students = Student.query.filter_by(grade=grade).all() if grade else Student.query.all()
        return jsonify([{
            'id': student.id,
            'name': student.name,
            'admission_number': student.admission_number,
            'grade': student.grade,
            'balance': student.balance
        } for student in students])
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        return jsonify({'error': 'Internal Server Error'}), 500

@routes.route('/students', methods=['POST'])
def add_student():
    try:
        logging.debug('Adding student...')
        data = request.json
        new_student = Student(
            name=data['name'],
            admission_number=data['admission_number'],
            grade=data['grade']
        )
        new_student.initialize_balance()
        db.session.add(new_student)
        db.session.commit()
        logging.debug('Student added successfully')
        return jsonify({'status': 'success', 'student': new_student.id})
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        return jsonify({'error': 'Internal Server Error'}), 500

@routes.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    try:
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return jsonify({'status': 'success', 'student': id})
    except Exception as e:
        return jsonify({'error': 'Internal Server Error'}), 500

@routes.route('/payments', methods=['POST'])
def add_payment():
    try:
        data = request.json
        payment = Payment.record_payment(
            admission_number=data['admission_number'],
            amount=data['amount'],
            date=datetime.strptime(data['date'], '%Y-%m-%d').date()
        )
        return jsonify({'status': 'success', 'payment': payment.id})
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal Server Error'}), 500
