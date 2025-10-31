from flask import Blueprint, jsonify, request

controller = Blueprint('controller', __name__)

# --------------------
# Дані для прикладу
# --------------------
COUNTRIES = [{"id": 1, "name": "Sweden", "code": "SE"}]
CITIES = [{"id": 1, "name": "Stockholm", "country_id": 1, "longitude": 18.0686, "latitude": 59.3293}]

# --------------------
# Country CRUD
# --------------------
@controller.route("/countries", methods=["GET"])
def get_countries():
    """
    Get all countries
    ---
    responses:
      200:
        description: List of countries
        examples:
          application/json: [{"id": 1, "name": "Sweden", "code": "SE"}]
    """
    return jsonify(COUNTRIES)

@controller.route("/countries/<int:id_country>", methods=["GET"])
def get_country(id_country):
    """
    Get a country by ID
    ---
    parameters:
      - in: path
        name: id_country
        type: integer
        required: true
        description: ID of the country
    responses:
      200:
        description: Country found
      404:
        description: Country not found
    """
    country = next((c for c in COUNTRIES if c["id"] == id_country), None)
    if country:
        return jsonify(country)
    return jsonify({"error": "Country not found"}), 404

@controller.route("/countries", methods=["POST"])
def create_country():
    """
    Create a new country
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          id: Country
          required:
            - name
            - code
          properties:
            name:
              type: string
            code:
              type: string
    responses:
      201:
        description: Country created successfully
    """
    data = request.json
    new_id = max(c["id"] for c in COUNTRIES) + 1 if COUNTRIES else 1
    new_country = {"id": new_id, "name": data["name"], "code": data["code"]}
    COUNTRIES.append(new_country)
    return jsonify(new_country), 201

@controller.route("/countries/<int:id_country>", methods=["PUT"])
def update_country(id_country):
    """
    Update a country
    ---
    parameters:
      - in: path
        name: id_country
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          id: CountryUpdate
          properties:
            name:
              type: string
            code:
              type: string
    responses:
      200:
        description: Country updated
      404:
        description: Country not found
    """
    data = request.json
    country = next((c for c in COUNTRIES if c["id"] == id_country), None)
    if country:
        country.update(data)
        return jsonify(country)
    return jsonify({"error": "Country not found"}), 404

@controller.route("/countries/<int:id_country>", methods=["DELETE"])
def delete_country(id_country):
    """
    Delete a country
    ---
    parameters:
      - in: path
        name: id_country
        type: integer
        required: true
    responses:
      200:
        description: Country deleted
      404:
        description: Country not found
    """
    global COUNTRIES
    country = next((c for c in COUNTRIES if c["id"] == id_country), None)
    if country:
        COUNTRIES = [c for c in COUNTRIES if c["id"] != id_country]
        return jsonify({"message": "Country deleted successfully"})
    return jsonify({"error": "Country not found"}), 404

# --------------------
# City CRUD
# --------------------
@controller.route("/cities", methods=["GET"])
def get_cities():
    """
    Get all cities
    ---
    responses:
      200:
        description: List of cities
    """
    return jsonify(CITIES)

@controller.route("/cities/<int:id_city>", methods=["GET"])
def get_city(id_city):
    """
    Get a city by ID
    ---
    parameters:
      - in: path
        name: id_city
        type: integer
        required: true
    responses:
      200:
        description: City found
      404:
        description: City not found
    """
    city = next((c for c in CITIES if c["id"] == id_city), None)
    if city:
        return jsonify(city)
    return jsonify({"error": "City not found"}), 404

@controller.route("/cities", methods=["POST"])
def create_city():
    """
    Create a new city
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          id: City
          required:
            - name
            - country_id
            - longitude
            - latitude
          properties:
            name:
              type: string
            country_id:
              type: integer
            longitude:
              type: number
            latitude:
              type: number
    responses:
      201:
        description: City created
    """
    data = request.json
    new_id = max(c["id"] for c in CITIES) + 1 if CITIES else 1
    new_city = {
        "id": new_id,
        "name": data["name"],
        "country_id": data["country_id"],
        "longitude": data["longitude"],
        "latitude": data["latitude"]
    }
    CITIES.append(new_city)
    return jsonify(new_city), 201

@controller.route("/cities/<int:id_city>", methods=["PUT"])
def update_city(id_city):
    """
    Update a city
    ---
    parameters:
      - in: path
        name: id_city
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          id: CityUpdate
          properties:
            name:
              type: string
            longitude:
              type: number
            latitude:
              type: number
    responses:
      200:
        description: City updated
      404:
        description: City not found
    """
    data = request.json
    city = next((c for c in CITIES if c["id"] == id_city), None)
    if city:
        city.update(data)
        return jsonify(city)
    return jsonify({"error": "City not found"}), 404

@controller.route("/cities/<int:id_city>", methods=["DELETE"])
def delete_city(id_city):
    """
    Delete a city
    ---
    parameters:
      - in: path
        name: id_city
        type: integer
        required: true
    responses:
      200:
        description: City deleted
      404:
        description: City not found
    """
    global CITIES
    city = next((c for c in CITIES if c["id"] == id_city), None)
    if city:
        CITIES = [c for c in CITIES if c["id"] != id_city]
        return jsonify({"message": "City deleted successfully"})
    return jsonify({"error": "City not found"}), 404
