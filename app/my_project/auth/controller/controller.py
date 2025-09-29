from flask import Blueprint, jsonify, request
from app.my_project.auth.service.service import (
    CountryService, CityService, WeatherConditionLabelService, 
    DailyWeatherService, HourlyWeatherService, WeatherAlertService, 
    WeatherForecastService, UserService, UserPreferencesService
)

controller = Blueprint('controller', __name__)

from flask import Blueprint

controller = Blueprint('controller', __name__)

@controller.route("/test", methods=["GET"])
def test():
    return {"message": "Server is running without DB!"}

# --------------------
# Маршрути для Country
# --------------------
@controller.route('/countries/<int:id_country>/cities', methods=['GET'])
def get_cities_by_country(id_country):
    cities = CityService.get_cities_by_country(id_country)
    if cities:
        return jsonify([city.to_dict() for city in cities])
    return jsonify({"error": "No cities found for this country"}), 404
#1:m
@controller.route('/countries', methods=['GET'])
def get_countries():
    countries = CountryService.get_all_countries()
    return jsonify([{"id": country.id_country, "name": country.name, "code": country.code} for country in countries])

@controller.route('/countries/<int:id_country>', methods=['GET'])
def get_country(id_country):
    country = CountryService.get_country_by_id(id_country)
    if country:
        return jsonify({"id": country.id_country, "name": country.name, "code": country.code})
    return jsonify({"error": "Country not found"}), 404

@controller.route('/countries', methods=['POST'])
def create_country():
    data = request.json
    country = CountryService.create_country(data)
    return jsonify({"id": country.id_country, "name": country.name, "code": country.code}), 201

@controller.route('/countries/<int:id_country>', methods=['PUT'])
def update_country(id_country):
    data = request.json
    country = CountryService.update_country(id_country, data)
    if country:
        return jsonify({"id": country.id_country, "name": country.name, "code": country.code})
    return jsonify({"error": "Country not found"}), 404

@controller.route('/countries/<int:id_country>', methods=['DELETE'])
def delete_country(id_country):
    CountryService.delete_country(id_country)
    return jsonify({"message": "Country deleted successfully"})


# --------------------
# Маршрути для City
# --------------------

@controller.route('/cities', methods=['GET'])
def get_cities():
    cities = CityService.get_all_cities()
    return jsonify([{"id": city.id_city, "name": city.name, "longitude": city.longitude, "latitude": city.latitude} for city in cities])

@controller.route('/cities/<int:id_city>', methods=['GET'])
def get_city(id_city):
    city = CityService.get_city_by_id(id_city)
    if city:
        return jsonify({"id": city.id_city, "name": city.name, "longitude": city.longitude, "latitude": city.latitude})
    return jsonify({"error": "City not found"}), 404

@controller.route('/cities', methods=['POST'])
def create_city():
    data = request.json
    city = CityService.create_city(data)
    return jsonify({"id": city.id_city, "name": city.name, "longitude": city.longitude, "latitude": city.latitude}), 201

@controller.route('/cities/<int:id_city>', methods=['PUT'])
def update_city(id_city):
    data = request.json
    city = CityService.update_city(id_city, data)
    if city:
        return jsonify({"id": city.id_city, "name": city.name, "longitude": city.longitude, "latitude": city.latitude})
    return jsonify({"error": "City not found"}), 404

@controller.route('/cities/<int:id_city>', methods=['DELETE'])
def delete_city(id_city):
    CityService.delete_city(id_city)
    return jsonify({"message": "City deleted successfully"})


# --------------------
# Маршрути для WeatherConditionLabel
# --------------------

@controller.route('/weather_conditions', methods=['GET'])
def get_weather_conditions():
    labels = WeatherConditionLabelService.get_all_labels()
    return jsonify([{"id": label.id_weather_condition_label, "label": label.label} for label in labels])

@controller.route('/weather_conditions', methods=['POST'])
def create_weather_condition():
    data = request.json
    label = WeatherConditionLabelService.create_label(data)
    return jsonify({"id": label.id_weather_condition_label, "label": label.label}), 201


# --------------------
# Маршрути для DailyWeather
# --------------------

@controller.route('/daily_weather', methods=['GET'])
def get_daily_weather():
    weather_entries = DailyWeatherService.get_all_daily_weather()
    return jsonify([{"id": entry.id_daily_weather, "date": entry.date, "min_temp": entry.min_temp, "max_temp": entry.max_temp} for entry in weather_entries])

@controller.route('/daily_weather', methods=['POST'])
def create_daily_weather():
    data = request.json
    entry = DailyWeatherService.create_daily_weather(data)
    return jsonify({"id": entry.id_daily_weather, "date": entry.date, "min_temp": entry.min_temp, "max_temp": entry.max_temp}), 201


# --------------------
# Маршрути для HourlyWeather
# --------------------

@controller.route('/hourly_weather', methods=['GET'])
def get_hourly_weather():
    weather_entries = HourlyWeatherService.get_all_hourly_weather()
    return jsonify([{"id": entry.id_hourly_weather, "date": entry.date, "hour": entry.hour, "temperature": entry.temperature} for entry in weather_entries])

@controller.route('/hourly_weather', methods=['POST'])
def create_hourly_weather():
    data = request.json
    entry = HourlyWeatherService.create_hourly_weather(data)
    return jsonify({"id": entry.id_hourly_weather, "date": entry.date, "hour": entry.hour, "temperature": entry.temperature}), 201


# --------------------
# Маршрути для WeatherAlert
# --------------------

@controller.route('/weather_alerts', methods=['GET'])
def get_weather_alerts():
    alerts = WeatherAlertService.get_all_alerts()
    return jsonify([{"id": alert.id_weather_alert, "alert_type": alert.alert_type, "start_time": alert.start_time} for alert in alerts])

@controller.route('/weather_alerts', methods=['POST'])
def create_weather_alert():
    data = request.json
    alert = WeatherAlertService.create_alert(data)
    return jsonify({"id": alert.id_weather_alert, "alert_type": alert.alert_type, "start_time": alert.start_time}), 201


# --------------------
# Маршрути для WeatherForecast
# --------------------

@controller.route('/weather_forecasts', methods=['GET'])
def get_weather_forecasts():
    forecasts = WeatherForecastService.get_all_forecasts()
    return jsonify([{"id": forecast.id_weather_forecast, "forecast_date": forecast.forecast_date} for forecast in forecasts])

@controller.route('/weather_forecasts', methods=['POST'])
def create_weather_forecast():
    data = request.json
    forecast = WeatherForecastService.create_forecast(data)
    return jsonify({"id": forecast.id_weather_forecast, "forecast_date": forecast.forecast_date}), 201

# --------------------
# Маршрути для User

# --------------------
@controller.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all()
    return jsonify([user.to_dict() for user in users])

@controller.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = UserService.create(data)
    return jsonify(user.to_dict()), 201

@controller.route('/user/<int:id_user>/city/<int:id_city>', methods=['POST'])
def add_city_to_user(id_user, id_city):
    UserService.add_city_to_user(id_user, id_city)
    return jsonify({"message": "City added to user successfully"}), 201

@controller.route('/user/<int:id_user>/cities', methods=['GET'])
def get_cities_by_user(id_user):
    cities = UserService.get_cities_by_user(id_user)
    return jsonify([city.to_dict() for city in cities]), 200

# --------------------
# Маршрути для UserPreferences
# --------------------
@controller.route('/user_preferences', methods=['GET'])
def get_user_preferences():
    preferences = UserPreferencesService.get_all()
    return jsonify([preference.to_dict() for preference in preferences])

@controller.route('/user_preferences', methods=['POST'])
def create_user_preference():
    data = request.json
    preference = UserPreferencesService.create(data)
    return jsonify(preference.to_dict()), 201