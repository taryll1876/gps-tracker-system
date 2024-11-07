from flask import jsonify, request
from models import GPSData, db

def setup_routes(app):

    @app.route('/api/track', methods=['POST'])
    def track():
        # Endpoint for posting GPS data
        data = request.json
        lat, lon = data.get("lat"), data.get("lon")
        if lat and lon:
            gps_data = GPSData(latitude=lat, longitude=lon)
            db.session.add(gps_data)
            db.session.commit()
            return jsonify({"status": "success", "message": "Data saved"}), 201
        return jsonify({"status": "error", "message": "Invalid data"}), 400

    @app.route('/api/locations', methods=['GET'])
    def get_locations():
        # Fetch all GPS locations
        gps_data = GPSData.query.all()
        return jsonify([{"lat": data.latitude, "lon": data.longitude} for data in gps_data]), 200
