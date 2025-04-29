# Defines API endpoints (Booking API Logic)
# Includes JWT protection and exposes GET /bookings/<booking_id>
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Booking

# Blueprint lets us organize routes into modular files.
bp = Blueprint("booking_bp", __name__)


# /book – Create a booking
@bp.route("/book", methods=["POST"])
@jwt_required()
def book():
    try:
        data = request.get_json()

        # Validate input data
        if not data or "user_id" not in data or "driver_id" not in data:
            return jsonify({"error": "Invalid input: user_id and driver_id required"}), 400

        booking = Booking(
            user_id=data["user_id"],
            driver_id=data["driver_id"],
            status=data.get("status", "booked")
        )

        db.session.add(booking)
        db.session.commit()

        return jsonify({"message": "Booking created", "booking_id": booking.id}), 201

    except KeyError as e:  # Handle missing keys explicitly
        return jsonify({"error": f"Missing key: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


# Public route to get all bookings
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

# return all active bookings
@bp.route('/active-bookings', methods=['GET'])
def active_bookings():
    bookings = Booking.query.all()
    result = []
    for booking in bookings:
        result.append({
            "booking_id": booking.id,
            "user_id": booking.user_id,
            "driver_id": booking.driver_id
        })
    return jsonify(result)