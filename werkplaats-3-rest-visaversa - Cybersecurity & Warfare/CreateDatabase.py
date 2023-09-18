from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Replace with your desired database URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy instance
db = SQLAlchemy(app)

# Define the model classes
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    checktime = db.Column(db.DateTime)
    persoon_id = db.Column(db.Integer, db.ForeignKey('personen.persoon_id'))
    event_id = db.Column(db.String, db.ForeignKey('events.id'))

class CheckIns(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.String, db.ForeignKey('events.id'))
    student_name = db.Column(db.String)
    other_details = db.Column(db.String)
    event = db.relationship('Events', backref='check_ins')

class DeletedUsers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.String)
    achternaam = db.Column(db.String)
    rol = db.Column(db.String)

class EventComposition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    klas_id = db.Column(db.Integer, db.ForeignKey('klas.klas_id'))
    persoon_id = db.Column(db.Integer, db.ForeignKey('personen.persoon_id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    location = db.Column(db.String)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    link = db.Column(db.String)

class Klas(db.Model):
    klas_id = db.Column(db.Integer, primary_key=True)
    coach_id = db.Column(db.Integer, db.ForeignKey('personen.persoon_id'))
    klas_naam = db.Column(db.String)
    klas_opleiding = db.Column(db.String)
    klas_leerjaar = db.Column(db.Integer)
    coach = db.relationship('Personen', foreign_keys=[coach_id], backref='klas')

class Personen(db.Model):
    persoon_id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String)
    voornaam = db.Column(db.String)
    achternaam = db.Column(db.String)
    rol = db.Column(db.String)
    klas_id = db.Column(db.Integer, db.ForeignKey('klas.klas_id'))

class Vak(db.Model):
    vak_id = db.Column(db.Integer, primary_key=True)
    vak_naam = db.Column(db.String)

with app.app_context():
    db.create_all()

print("Database created successfully!")

# Insert sample data into the tables
with app.app_context():
    # Insert data into the `attendance` table
    attendance_data = [
        {'checktime': datetime.strptime('2023-06-01 09:00:00', '%Y-%m-%d %H:%M:%S'), 'persoon_id': 1, 'event_id': 'ABC123'},
        {'checktime': datetime.strptime('2023-06-02 10:30:00', '%Y-%m-%d %H:%M:%S'), 'persoon_id': 2, 'event_id': 'DEF456'},
        # Add more sample data as needed
    ]
    for data in attendance_data:
        attendance = Attendance(**data)
        db.session.add(attendance)

    # Insert data into the `check_ins` table
    check_ins_data = [
        {'event_id': 1, 'student_name': 'John Doe', 'other_details': 'Some details'},
        {'event_id': 2, 'student_name': 'Jane Smith', 'other_details': 'More details'},
        # Add more sample data as needed
    ]
    for data in check_ins_data:
        check_ins = CheckIns(**data)
        db.session.add(check_ins)

    # Insert data into the `deletedusers` table
    deletedusers_data = [
        {'voornaam': 'Alice', 'achternaam': 'Johnson', 'rol': 'User'},
        {'voornaam': 'Bob', 'achternaam': 'Smith', 'rol': 'Admin'},
        # Add more sample data as needed
    ]
    for data in deletedusers_data:
        deletedusers = DeletedUsers(**data)
        db.session.add(deletedusers)

    # Insert data into the `event_composition` table
    event_composition_data = [
        {'klas_id': 1, 'persoon_id': 1, 'event_id': 1},
        {'klas_id': 2, 'persoon_id': 2, 'event_id': 2},
        # Add more sample data as needed
    ]
    for data in event_composition_data:
        event_composition = EventComposition(**data)
        db.session.add(event_composition)

    # Insert data into the `events` table
    events_data = [
        {'title': 'Event 1', 'location': 'Location 1', 'start': datetime.strptime('2023-06-01 10:00:00', '%Y-%m-%d %H:%M:%S'), 'end': datetime.strptime('2023-06-01 12:00:00', '%Y-%m-%d %H:%M:%S'), 'link': 'https://example.com/event1'},
        {'title': 'Event 2', 'location': 'Location 2', 'start': datetime.strptime('2023-06-02 14:00:00', '%Y-%m-%d %H:%M:%S'), 'end': datetime.strptime('2023-06-02 16:00:00', '%Y-%m-%d %H:%M:%S'), 'link': 'https://example.com/event2'},
        # Add more sample data as needed
    ]
    for data in events_data:
        events = Events(**data)
        db.session.add(events)

    # Insert data into the `klas` table
    klas_data = [
        {'coach_id': 1, 'klas_naam': 'Klas A', 'klas_opleiding': 'Opleiding A', 'klas_leerjaar': 1},
        {'coach_id': 2, 'klas_naam': 'Klas B', 'klas_opleiding': 'Opleiding B', 'klas_leerjaar': 2},
        # Add more sample data as needed
    ]
    for data in klas_data:
        klas = Klas(**data)
        db.session.add(klas)

    # Insert data into the `personen` table
    personen_data = [
        {'password': 'password1', 'voornaam': 'John', 'achternaam': 'Doe', 'rol': 'Student', 'klas_id': 1},
        {'password': 'password2', 'voornaam': 'Jane', 'achternaam': 'Smith', 'rol': 'Student', 'klas_id': 2},
        # Add more sample data as needed
    ]
    for data in personen_data:
        personen = Personen(**data)
        db.session.add(personen)

    # Insert data into the `vak` table
    vak_data = [
        {'vak_naam': 'Vak 1'},
        {'vak_naam': 'Vak 2'},
        # Add more sample data as needed
    ]
    for data in vak_data:
        vak = Vak(**data)
        db.session.add(vak)

    # Commit the changes to the database
    db.session.commit()

print("Data inserted successfully!")