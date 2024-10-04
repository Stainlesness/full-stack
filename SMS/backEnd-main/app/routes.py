from flask import Flask, request, jsonify
from app.models import db, Staff, Student, Fee, Payment, BusPayment, BusDestinationCharges, BoardingFee, Assignment, Event, Gallery, Notification

routes = Blueprint('routes', __name__)

# Initialize the database here
# app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
# db.init_app(app)

# CRUD for Staff
@app.route('/staff', methods=['POST'])
def create_staff():
    data = request.json
    new_staff = Staff(
        name=data['name'],
        phone=data['phone'],
        role=data['role'],
        representing=data.get('representing')
    
    new_staff.set_password(data['password'])  # Hash the password
    db.session.add(new_staff)
    db.session.commit()
    return jsonify({'message': 'Staff member created'}), 201

@app.route('/staff/<int:id>', methods=['GET'])
def get_staff(id):
    staff = Staff.query.get_or_404(id)
    return jsonify({'id': staff.id, 'name': staff.name, 'phone': staff.phone, 'role': staff.role, 'representing': staff.representing})

@app.route('/staff/<int:id>', methods=['PUT'])
def update_staff(id):
    staff = Staff.query.get_or_404(id)
    data = request.json
    staff.name = data.get('name', staff.name)
    staff.phone = data.get('phone', staff.phone)
    staff.role = data.get('role', staff.role)
    staff.representing = data.get('representing', staff.representing)
    if 'password' in data:
        staff.set_password(data['password'])
    db.session.commit()
    return jsonify({'message': 'Staff member updated'})

@app.route('/staff/<int:id>', methods=['DELETE'])
def delete_staff(id):
    staff = Staff.query.get_or_404(id)
    db.session.delete(staff)
    db.session.commit()
    return jsonify({'message': 'Staff member deleted'})

# CRUD for Students
@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
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
    new_student.set_password(data['admission_number'])  # Hash the admission number as password
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student created'}), 201

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({'id': student.id, 'name': student.name, 'admission_number': student.admission_number, 'grade': student.grade, 'balance': student.balance})

@app.route('/students/<int:id>', methods=['PUT'])
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
        student.set_password(data['admission_number'])  # Update password
    db.session.commit()
    return jsonify({'message': 'Student updated'})

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted'})

# CRUD for Fees
@app.route('/fees', methods=['POST'])
def create_fee():
    data = request.json
    new_fee = Fee(
        grade=data['grade'],
        term_fee=data['term_fee']
    )
    db.session.add(new_fee)
    db.session.commit()
    return jsonify({'message': 'Fee created'}), 201

@app.route('/fees/<int:id>', methods=['GET'])
def get_fee(id):
    fee = Fee.query.get_or_404(id)
    return jsonify({'id': fee.id, 'grade': fee.grade, 'term_fee': fee.term_fee})

@app.route('/fees/<int:id>', methods=['PUT'])
def update_fee(id):
    fee = Fee.query.get_or_404(id)
    data = request.json
    fee.grade = data.get('grade', fee.grade)
    fee.term_fee = data.get('term_fee', fee.term_fee)
    db.session.commit()
    return jsonify({'message': 'Fee updated'})

@app.route('/fees/<int:id>', methods=['DELETE'])
def delete_fee(id):
    fee = Fee.query.get_or_404(id)
    db.session.delete(fee)
    db.session.commit()
    return jsonify({'message': 'Fee deleted'})

# CRUD for Bus Destinations
@app.route('/bus_destinations', methods=['POST'])
def create_bus_destination():
    data = request.json
    new_destination = BusDestinationCharges(
        destination=data['destination'],
        charge=data['charge']
    )
    db.session.add(new_destination)
    db.session.commit()
    return jsonify({'message': 'Bus destination created'}), 201

@app.route('/bus_destinations/<int:id>', methods=['GET'])
def get_bus_destination(id):
    destination = BusDestinationCharges.query.get_or_404(id)
    return jsonify({'id': destination.id, 'destination': destination.destination, 'charge': destination.charge})

@app.route('/bus_destinations/<int:id>', methods=['PUT'])
def update_bus_destination(id):
    destination = BusDestinationCharges.query.get_or_404(id)
    data = request.json
    destination.destination = data.get('destination', destination.destination)
    destination.charge = data.get('charge', destination.charge)
    db.session.commit()
    return jsonify({'message': 'Bus destination updated'})

@app.route('/bus_destinations/<int:id>', methods=['DELETE'])
def delete_bus_destination(id):
    destination = BusDestinationCharges.query.get_or_404(id)
    db.session.delete(destination)
    db.session.commit()
    return jsonify({'message': 'Bus destination deleted'})

# CRUD for Payments
@app.route('/payments', methods=['POST'])
def create_payment():
    data = request.json
    payment = Payment.record_payment(data['admission_number'], data['amount'], data['method'])
    return jsonify({'message': 'Payment recorded', 'payment_id': payment.id}), 201

# CRUD for Assignments
@app.route('/assignments', methods=['POST'])
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

@app.route('/assignments/<int:id>', methods=['GET'])
def get_assignment(id):
    assignment = Assignment.query.get_or_404(id)
    return jsonify({'id': assignment.id, 'title': assignment.title, 'grade': assignment.grade, 'description': assignment.description, 'due_date': assignment.due_date})

@app.route('/assignments/<int:id>', methods=['PUT'])
def update_assignment(id):
    assignment = Assignment.query.get_or_404(id)
    data = request.json
    assignment.title = data.get('title', assignment.title)
    assignment.grade = data.get('grade', assignment.grade)
    assignment.description = data.get('description', assignment.description)
    assignment.due_date = data.get('due_date', assignment.due_date)
    db.session.commit()
    return jsonify({'message': 'Assignment updated'})

@app.route('/assignments/<int:id>', methods=['DELETE'])
def delete_assignment(id):
    assignment = Assignment.query.get_or_404(id)
    db.session.delete(assignment)
    db.session.commit()
    return jsonify({'message': 'Assignment deleted'})

# CRUD for Events
@app.route('/events', methods=['POST'])
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

@app.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    event = Event.query.get_or_404(id)
    return jsonify({'id': event.id, 'title': event.title, 'date': event.date, 'destination': event.destination, 'description': event.description})

@app.route('/events/<int:id>', methods=['PUT'])
def update_event(id):
    event = Event.query.get_or_404(id)
    data = request.json
    event.title = data.get('title', event.title)
    event.date = data.get('date', event.date)
    event.destination = data.get('destination', event.destination)
    event.description = data.get('description', event.description)
    db.session.commit()
    return jsonify({'message': 'Event updated'})

@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'message': 'Event deleted'})

# CRUD for Gallery
@app.route('/gallery', methods=['POST'])
def create_gallery():
    data = request.json
    new_image = Gallery(
        image_url=data['image_url'],
        description=data.get('description', '')
    )
    db.session.add(new_image)
    db.session.commit()
    return jsonify({'message': 'Gallery image created'}), 201

@app.route('/gallery/<int:id>', methods=['GET'])
def get_gallery_image(id):
    image = Gallery.query.get_or_404(id)
    return jsonify({'id': image.id, 'image_url': image.image_url, 'description': image.description})

@app.route('/gallery/<int:id>', methods=['PUT'])
def update_gallery_image(id):
    image = Gallery.query.get_or_404(id)
    data = request.json
    image.image_url = data.get('image_url', image.image_url)
    image.description = data.get('description', image.description)
    db.session.commit()
    return jsonify({'message': 'Gallery image updated'})

@app.route('/gallery/<int:id>', methods=['DELETE'])
def delete_gallery_image(id):
    image = Gallery.query.get_or_404(id)
    db.session.delete(image)
    db.session.commit()
    return jsonify({'message': 'Gallery image deleted'})

# CRUD for Notifications
@app.route('/notifications', methods=['POST'])
def create_notification():
    data = request.json
    new_notification = Notification(
        message=data['message']
    )
    db.session.add(new_notification)
    db.session.commit()
    return jsonify({'message': 'Notification created'}), 201

@app.route('/notifications/<int:id>', methods=['GET'])
def get_notification(id):
    notification = Notification.query.get_or_404(id)
    return jsonify({'id': notification.id, 'message': notification.message, 'date': notification.date})

@app.route('/notifications/<int:id>', methods=['PUT'])
def update_notification(id):
    notification = Notification.query.get_or_404(id)
    data = request.json
    notification.message = data.get('message', notification.message)
    db.session.commit()
    return jsonify({'message': 'Notification updated'})

@app.route('/notifications/<int:id>', methods=['DELETE'])
def delete_notification(id):
    notification = Notification.query.get_or_404(id)
    db.session.delete(notification)
    db.session.commit()
    return jsonify({'message': 'Notification deleted'})

if __name__ == '__main__':
    app.run(debug=True)


