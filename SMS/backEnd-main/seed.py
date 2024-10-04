from datetime import datetime
from app import create_app, db
from app.models import Student, Fee, Payment, Staff, Assignment, Event, Gallery, Notification, BoardingFee, BusDestinationCharges, BusPayment

app = create_app()

with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # Create fees
    fees = [
        Fee(grade="1", term_fee=5000.0),
        Fee(grade="2", term_fee=5500.0),
        Fee(grade="3", term_fee=6000.0),
        Fee(grade="4", term_fee=6500.0),
        Fee(grade="5", term_fee=7000.0),
        Fee(grade="6", term_fee=7500.0),
        Fee(grade="7", term_fee=8000.0),
        Fee(grade="8", term_fee=8500.0),
    ]

    # Add fees to the session
    db.session.add_all(fees)
    db.session.commit()  # Commit fees first to ensure they exist for balance initialization

    # Create students
    students = [
        Student(name="Alice Smith", admission_number="5561", grade="1", use_bus=False, term_fee=5000.0),
        Student(name="Bob Jones", admission_number="5562", grade="2", use_bus=True, term_fee=5500.0),
        Student(name="Charlie Brown", admission_number="5563", grade="3", use_bus=False, term_fee=6000.0),
        Student(name="Daisy Johnson", admission_number="5564", grade="4", use_bus=True, term_fee=6500.0),
        Student(name="Eve Adams", admission_number="5565", grade="5", use_bus=False, term_fee=7000.0),
        Student(name="Frank Miller", admission_number="5566", grade="6", use_bus=True, term_fee=7500.0),
        Student(name="Grace Lee", admission_number="5567", grade="7", use_bus=False, term_fee=8000.0),
        Student(name="Henry Davis", admission_number="5568", grade="8", use_bus=True, term_fee=8500.0),
    ]

    # Initialize student balances
    for student in students:
        student.initialize_balance()  # Set balance based on the fee for their grade

    # Add all student data to the session
    db.session.add_all(students)

    # Commit the student data
    try:
        db.session.commit()
        print("Database seeded successfully!")
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of an error
        print(f"Error seeding database: {e}")

    # Create staff members
    staff_members = [
        Staff(name="Principal Smith", phone="0712345678", role="Principal", representing="All grades"),
        Staff(name="Bursar Jane", phone="0712345679", role="Bursar", representing="Finance"),
        Staff(name="Teacher Tom", phone="0712345680", role="Teacher", representing="Grade 1"),
    ]

    # Set passwords for staff
    for staff in staff_members:
        staff.set_password("password123")  # Use a default password for simplicity

    # Add staff members to the session
    db.session.add_all(staff_members)

    # Commit the staff data
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding staff: {e}")

    # Create assignments
    assignments = [
        Assignment(title="Math Homework", grade="1", description="Complete exercises 1 to 10", due_date=datetime(2024, 10, 10)),
        Assignment(title="Science Project", grade="2", description="Create a model of the solar system", due_date=datetime(2024, 10, 15)),
    ]

    # Add assignments to the session
    db.session.add_all(assignments)

    # Commit the assignment data
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding assignments: {e}")

    # Create events
    events = [
        Event(title="School Sports Day", date=datetime(2024, 10, 20), destination="School Grounds", description="Annual sports competition for all grades"),
        Event(title="Parent-Teacher Meeting", date=datetime(2024, 10, 25), destination="School Hall", description="Discuss student progress with parents"),
    ]

    # Add events to the session
    db.session.add_all(events)

    # Commit the event data
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding events: {e}")

    # Create gallery images
    galleries = [
        Gallery(image_url="http://example.com/image1.jpg", description="Sports Day 2023"),
        Gallery(image_url="http://example.com/image2.jpg", description="School Trip to the Museum"),
    ]

    # Add gallery images to the session
    db.session.add_all(galleries)

    # Commit the gallery data
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding galleries: {e}")

    # Create notifications
    notifications = [
        Notification(message="School will be closed on 2024-10-15 for a public holiday."),
        Notification(message="Reminder: Parent-Teacher meeting on 2024-10-25."),
    ]

    # Add notifications to the session
    db.session.add_all(notifications)

    # Commit the notification data
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding notifications: {e}")

    print("Seeding completed.")
    