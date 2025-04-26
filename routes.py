#Booking API Logic
# Includes JWT protection and exposes GET /bookings/<booking_id>
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Booking

bp = Blueprint("booking_bp", __name__)

#/book – Create a booking
@bp.route("/book", methods=["POST"])
# Secure route to create booking
@jwt_required()
def book():
    data = request.get_json()
    try:
        booking = Booking(
            user_id=data["user_id"],
            driver_id=data["driver_id"],
            status=data.get("status", "booked")
        )
        db.session.add(booking)
        db.session.commit()
        return jsonify({"message": "Booking created", "booking_id": booking.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Public route to get all bookings
#/bookings – Get all bookings
@bp.route("/bookings", methods=["GET"])
def get_bookings():
    bookings = Booking.query.all()
    return jsonify([b.to_dict() for b in bookings])

# Public route for inter-service call (e.g. payment-service)
@bp.route("/bookings/<int:booking_id>", methods=["GET"])
def get_booking_by_id(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    return jsonify(booking.to_dict())