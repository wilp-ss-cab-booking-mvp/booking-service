from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    driver_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default="booked", nullable=False)

    def __repr__(self):
        return f"<Booking {self.id} - User {self.user_id} - Driver {self.driver_id} - Status {self.status}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "driver_id": self.driver_id,
            "status": self.status
        }