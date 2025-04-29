from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    driver_id = db.Column(db.Integer, ForeignKey('drivers.id'), nullable=False)
    status = db.Column(db.String(20), default="booked", nullable=False)

    def __repr__(self):
        return f"<Booking {self.id} - User {self.user_id} - Driver {self.driver_id}>"