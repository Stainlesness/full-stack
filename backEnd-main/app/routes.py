from flask import request, jsonify, Blueprint
from .models import db, Staff, Student, Fee, Payment, BusPayment, BusDestinationCharges, BoardingFee, Assignment, Event, Gallery, Notification
from flask_bcrypt import Bcrypt
from . import db
from flask import current_app as app
import logging


routes = Blueprint('routes', __name__)
bcrypt = Bcrypt()

logging.basicConfig(level=logging.DEBUG)

# CRUD for Staff
@routes.route('/staff', methods=['POST'])
def create_staff():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')  # Hash the password
    new_staff = Staff(
        name=data['name'],
        phone=data['phone'],
        role=data['role'],
        representing=data.get('representing')
    )
    new_staff.password = hashed_password  # Set hashed password
    db.session.add(new_staff)
    db.session.commit()
    return jsonify({'message': 'Staff member created'}), 201

@routes.route('/staff', methods=['GET'])
def get_all_staff():
    staff_members = Staff.query.all()  # Fetch all staff members
    staff_list = []
    
    for staff in staff_members:
        staff_data = {
            'id': staff.id,
            'name': staff.name,
            'phone': staff.phone,
            'role': staff.role,
            'representing': staff.representing,
            'created_at': staff.created_at
        }
        staff_list.append(staff_data)

    return jsonify(staff_list), 200
    

@routes.route('/staff/<int:id>', methods=['GET'])
def get_staff(id):
    staff = Staff.query.get_or_404(id)
    return jsonify({'id': staff.id, 'name': staff.name, 'phone': staff.phone, 'role': staff.role, 'representing': staff.representing})

# Get all students
@routes.route('/students', methods=['GET'])
def get_all_students():
    students = Student.query.all()  # Fetch all students
    result = []
    for student in students:
        result.append({
            'id': student.id,
            'name': student.name,
            'admission_number': student.admission_number,
            'grade': student.grade,
            'balance': student.balance,
            'arrears': student.arrears,
            'term_fee': student.term_fee,
            'use_bus': student.use_bus,
            'bus_balance': student.bus_balance
        })
    return jsonify(result), 200


@routes.route('/staff/<int:id>', methods=['PUT'])
def update_staff(id):
    staff = Staff.query.get_or_404(id)
    data = request.json
    staff.name = data.get('name', staff.name)
    staff.phone = data.get('phone', staff.phone)
    staff.role = data.get('role', staff.role)
    staff.representing = data.get('representing', staff.representing)
    if 'password' in data:
        staff.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')  # Update hashed password
    db.session.commit()
    return jsonify({'message': 'Staff member updated'})

@routes.route('/staff/<int:id>', methods=['DELETE'])
def delete_staff(id):
    staff = Staff.query.get_or_404(id)
    db.session.delete(staff)
    db.session.commit()
    return jsonify({'message': 'Staff member deleted'})

# CRUD for Students
@routes.route('/students', methods=['POST'])
def create_student():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['admission_number']).decode('utf-8')  # Hash the admission number as password
    new_student = Student(
        name=data['name'],
        admission_number=data['admission_number'],
        grade=data['grade'],
        balance=data.get('balance', 0.0),
        arrears=data.get('arrears', 0.0),
        term_fee=data['term_fee'],
        use_bus=data['use_bus'],
        bus_balance=data.get('bus_balance', 0.0)
    )
    new_student.password = hashed_password  # Set hashed password
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student created'}), 201

@routes.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({'id': student.id, 'name': student.name, 'admission_number': student.admission_number, 'grade': student.grade, 'balance': student.balance})

@routes.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.json
    student.name = data.get('name', student.name)
    student.grade = data.get('grade', student.grade)
    student.balance = data.get('balance', student.balance)
    student.arrears = data.get('arrears', student.arrears)
    student.term_fee = data.get('term_fee', student.term_fee)
    student.use_bus = data.get('use_bus', student.use_bus)
    student.bus_balance = data.get('bus_balance', student.bus_balance)
    if 'admission_number' in data:
        student.password = bcrypt.generate_password_hash(data['admission_number']).decode('utf-8')  # Update hashed password
    db.session.commit()
    return jsonify({'message': 'Student updated'})

@routes.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted'})

# CRUD for Fees
@routes.route('/fees', methods=['POST'])
def create_fee():
    data = request.json
    new_fee = Fee(
        grade=data['grade'],
        term_fee=data['term_fee']
    )
    db.session.add(new_fee)
    db.session.commit()
    return jsonify({'message': 'Fee created'}), 201

@routes.route('/fees/<int:id>', methods=['GET'])
def get_fee(id):
    fee = Fee.query.get_or_404(id)
    return jsonify({'id': fee.id, 'grade': fee.grade, 'term_fee': fee.term_fee})

@routes.route('/fees/<int:id>', methods=['PUT'])
def update_fee(id):
    fee = Fee.query.get_or_404(id)
    data = request.json
    fee.grade = data.get('grade', fee.grade)
    fee.term_fee = data.get('term_fee', fee.term_fee)
    db.session.commit()
    return jsonify({'message': 'Fee updated'})

@routes.route('/fees/<int:id>', methods=['DELETE'])
def delete_fee(id):
    fee = Fee.query.get_or_404(id)
    db.session.delete(fee)
    db.session.commit()
    return jsonify({'message': 'Fee deleted'})

# CRUD for Bus Destinations
@routes.route('/bus_destinations', methods=['POST'])
def create_bus_destination():
    data = request.json
    new_destination = BusDestinationCharges(
        destination=data['destination'],
        charge=data['charge']
    )
    db.session.add(new_destination)
    db.session.commit()
    return jsonify({'message': 'Bus destination created'}), 201

@routes.route('/bus_destinations/<int:id>', methods=['GET'])
def get_bus_destination(id):
    destination = BusDestinationCharges.query.get_or_404(id)
    return jsonify({'id': destination.id, 'destination': destination.destination, 'charge': destination.charge})

@routes.route('/bus_destinations/<int:id>', methods=['PUT'])
def update_bus_destination(id):
    destination = BusDestinationCharges.query.get_or_404(id)
    data = request.json
    destination.destination = data.get('destination', destination.destination)
    destination.charge = data.get('charge', destination.charge)
    db.session.commit()
    return jsonify({'message': 'Bus destination updated'})

@routes.route('/bus_destinations/<int:id>', methods=['DELETE'])
def delete_bus_destination(id):
    destination = BusDestinationCharges.query.get_or_404(id)
    db.session.delete(destination)
    db.session.commit()
    return jsonify({'message': 'Bus destination deleted'})

# CRUD for Payments
@routes.route('/payments', methods=['POST'])
def create_payment():
    data = request.json
    payment = Payment.record_payment(data['admission_number'], data['amount'], data['method'])
    return jsonify({'message': 'Payment recorded', 'payment_id': payment.id}), 201

# CRUD for Assignments
@routes.route('/assignments', methods=['POST'])
def create_assignment():
    data = request.json
    new_assignment = Assignment(
        title=data['title'],
        grade=data['grade'],
        description=data.get('description', ''),
        due_date=data['due_date']
    )
    db.session.add(new_assignment)
    db.session.commit()
    return jsonify({'message': 'Assignment created'}), 201

@routes.route('/assignments/<int:id>', methods=['GET'])
def get_assignment(id):
    assignment = Assignment.query.get_or_404(id)
    return jsonify({'id': assignment.id, 'title': assignment.title, 'grade': assignment.grade, 'description': assignment.description, 'due_date': assignment.due_date})

@routes.route('/assignments/<int:id>', methods=['PUT'])
def update_assignment(id):
    assignment = Assignment.query.get_or_404(id)
    data = request.json
    assignment.title = data.get('title', assignment.title)
    assignment.grade = data.get('grade', assignment.grade)
    assignment.description = data.get('description', assignment.description)
    assignment.due_date = data.get('due_date', assignment.due_date)
    db.session.commit()
    return jsonify({'message': 'Assignment updated'})

@routes.route('/assignments/<int:id>', methods=['DELETE'])
def delete_assignment(id):
    assignment = Assignment.query.get_or_404(id)
    db.session.delete(assignment)
    db.session.commit()
    return jsonify({'message': 'Assignment deleted'})

# CRUD for Events
@routes.route('/events', methods=['POST'])
def create_event():
    data = request.json
    new_event = Event(
        title=data['title'],
        date=data['date'],
        destination=data['destination'],
        description=data.get('description', '')
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event created'}), 201

@routes.route('/events', methods=['GET'])
def get_all_events():
    events = Event.query.all()  # Fetch all events
    event_list = []
    
    for event in events:
        event_data = {
            'id': event.id,
            'title': event.title,
            'date': event.date,
            'destination': event.destination,
            'description': event.description
        }
        event_list.append(event_data)

    return jsonify(event_list), 200
    

@routes.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    event = Event.query.get_or_404(id)
    return jsonify({'id': event.id, 'title': event.title, 'date': event.date, 'destination': event.destination, 'description': event.description})

@routes.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    event = Event.query.get_or_404(id)
    data = request.json
    event.title = data.get('title', event.title)
    event.date = data.get('date', event.date)
    event.destination = data.get('destination', event.destination)
    event.description = data.get('description', event.description)
    db.session.commit()
    return jsonify({'message': 'Event updated'})

@routes.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Event deleted'})

# CRUD for Gallery
@routes.route('/gallery', methods=['POST'])
def create_gallery_entry():
    data = request.json
    new_entry = Gallery(
        title=data['title'],
        description=data['description'],
        image_url=data['image_url']
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({'message': 'Gallery entry created'}), 201

@routes.route('/gallery', methods=['GET'])
def get_all_gallery():
    gallery_items = Gallery.query.all()  # Fetch all gallery items
    gallery_list = []
    
    for gallery_item in gallery_items:
        gallery_data = {
            'id': gallery_item.id,
            'image_url': gallery_item.image_url,
            'description': gallery_item.description
        }
        gallery_list.append(gallery_data)

    return jsonify(gallery_list), 200
    

@routes.route('/gallery/<int:id>', methods=['GET'])
def get_gallery_entry(id):
    entry = Gallery.query.get_or_404(id)
    return jsonify({'id': entry.id, 'title': entry.title, 'description': entry.description, 'image_url': entry.image_url})

@routes.route('/gallery/<int:id>', methods=['PUT'])
def update_gallery_entry(id):
    entry = Gallery.query.get_or_404(id)
    data = request.json
    entry.title = data.get('title', entry.title)
    entry.description = data.get('description', entry.description)
    entry.image_url = data.get('image_url', entry.image_url)
    db.session.commit()
    return jsonify({'message': 'Gallery entry updated'})

@routes.route('/gallery/<int:id>', methods=['DELETE'])
def delete_gallery_entry(id):
    entry = Gallery.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Gallery entry deleted'})

# CRUD for Notifications
@routes.route('/notifications', methods=['POST'])
def create_notification():
    data = request.json
    new_notification = Notification(
        message=data['message'],
        date=data['date']
    )
    db.session.add(new_notification)
    db.session.commit()
    return jsonify({'message': 'Notification created'}), 201

@routes.route('/notifications', methods=['GET'])
def get_all_notifications():
    notifications = Notification.query.all()  # Fetch all notifications
    notification_list = []
    
    for notification in notifications:
        notification_data = {
            'id': notification.id,
            'message': notification.message,
            'date': notification.date
        }
        notification_list.append(notification_data)

    return jsonify(notification_list), 200

@routes.route('/notifications/<int:id>', methods=['GET'])
def get_notification(id):
    notification = Notification.query.get_or_404(id)
    return jsonify({'id': notification.id, 'message': notification.message, 'date': notification.date})

@routes.route('/notifications/<int:id>', methods=['PUT'])
def update_notification(id):
    notification = Notification.query.get_or_404(id)
    data = request.json
    notification.message = data.get('message', notification.message)
    notification.date = data.get('date', notification.date)
    db.session.commit()
    return jsonify({'message': 'Notification updated'})

@routes.route('/notifications/<int:id>', methods=['DELETE'])
def delete_notification(id):
    notification = Notification.query.get_or_404(id)
    db.session.delete(notification)
    db.session.commit()
    return jsonify({'message': 'Notification deleted'})



# Route to get all events


# Route to get all gallery items


# Route to get all notifications



# Route to get all staff members
