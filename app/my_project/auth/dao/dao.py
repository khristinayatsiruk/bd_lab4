from app import db
from app.my_project.auth.domain.models import (
    Country, City, WeatherConditionLabel, DailyWeather, HourlyWeather,
    WeatherAlert, WeatherForecast, User, UserPreferences, UserHasCity
)

# ------------------- COUNTRY -------------------
class CountryDAO:
    @staticmethod
    def get_all():
        return Country.query.all()

    @staticmethod
    def get_by_id(id_country):
        return Country.query.get(id_country)

    @staticmethod
    def create(data):
        new_country = Country(**data)
        db.session.add(new_country)
        db.session.commit()
        return new_country

    @staticmethod
    def update(id_country, data):
        country = Country.query.get(id_country)
        if country:
            for key, value in data.items():
                setattr(country, key, value)
            db.session.commit()
        return country

    @staticmethod
    def delete(id_country):
        country = Country.query.get(id_country)
        if country:
            db.session.delete(country)
            db.session.commit()

# ------------------- CITY -------------------
class CityDAO:
    @staticmethod
    def get_all():
        return City.query.all()

    @staticmethod
    def get_by_id(id_city):
        return City.query.get(id_city)

    @staticmethod
    def create(data):
        new_city = City(**data)
        db.session.add(new_city)
        db.session.commit()
        return new_city

    @staticmethod
    def update(id_city, data):
        city = City.query.get(id_city)
        if city:
            for key, value in data.items():
                setattr(city, key, value)
            db.session.commit()
        return city

    @staticmethod
    def delete(id_city):
        city = City.query.get(id_city)
        if city:
            db.session.delete(city)
            db.session.commit()

    @staticmethod
    def get_by_country(country_id):
        return City.query.filter_by(country_id_country=country_id).all()

# ------------------- WEATHER -------------------
class WeatherConditionLabelDAO:
    @staticmethod
    def get_all():
        return WeatherConditionLabel.query.all()

    @staticmethod
    def get_by_id(id_label):
        return WeatherConditionLabel.query.get(id_label)

    @staticmethod
    def create(data):
        label = WeatherConditionLabel(**data)
        db.session.add(label)
        db.session.commit()
        return label

# ------------------- DAILY WEATHER -------------------
class DailyWeatherDAO:
    @staticmethod
    def get_all():
        return DailyWeather.query.all()

    @staticmethod
    def get_by_id(id_daily_weather):
        return DailyWeather.query.get(id_daily_weather)

    @staticmethod
    def create(data):
        weather = DailyWeather(**data)
        db.session.add(weather)
        db.session.commit()
        return weather

    @staticmethod
    def update(id_daily_weather, data):
        weather = DailyWeather.query.get(id_daily_weather)
        if weather:
            for key, value in data.items():
                setattr(weather, key, value)
            db.session.commit()
        return weather

    @staticmethod
    def delete(id_daily_weather):
        weather = DailyWeather.query.get(id_daily_weather)
        if weather:
            db.session.delete(weather)
            db.session.commit()

# ------------------- HOURLY WEATHER -------------------
class HourlyWeatherDAO:
    @staticmethod
    def get_all():
        return HourlyWeather.query.all()

    @staticmethod
    def get_by_id(id_hourly_weather):
        return HourlyWeather.query.get(id_hourly_weather)

    @staticmethod
    def create(data):
        weather = HourlyWeather(**data)
        db.session.add(weather)
        db.session.commit()
        return weather

    @staticmethod
    def update(id_hourly_weather, data):
        weather = HourlyWeather.query.get(id_hourly_weather)
        if weather:
            for key, value in data.items():
                setattr(weather, key, value)
            db.session.commit()
        return weather

    @staticmethod
    def delete(id_hourly_weather):
        weather = HourlyWeather.query.get(id_hourly_weather)
        if weather:
            db.session.delete(weather)
            db.session.commit()

# ------------------- WEATHER ALERT -------------------
class WeatherAlertDAO:
    @staticmethod
    def get_all():
        return WeatherAlert.query.all()

    @staticmethod
    def get_by_id(id_alert):
        return WeatherAlert.query.get(id_alert)

    @staticmethod
    def create(data):
        alert = WeatherAlert(**data)
        db.session.add(alert)
        db.session.commit()
        return alert

    @staticmethod
    def delete(id_alert):
        alert = WeatherAlert.query.get(id_alert)
        if alert:
            db.session.delete(alert)
            db.session.commit()

# ------------------- WEATHER FORECAST -------------------
class WeatherForecastDAO:
    @staticmethod
    def get_all():
        return WeatherForecast.query.all()

    @staticmethod
    def get_by_id(id_forecast):
        return WeatherForecast.query.get(id_forecast)

    @staticmethod
    def create(data):
        forecast = WeatherForecast(**data)
        db.session.add(forecast)
        db.session.commit()
        return forecast

    @staticmethod
    def update(id_forecast, data):
        forecast = WeatherForecast.query.get(id_forecast)
        if forecast:
            for key, value in data.items():
                setattr(forecast, key, value)
            db.session.commit()
        return forecast

    @staticmethod
    def delete(id_forecast):
        forecast = WeatherForecast.query.get(id_forecast)
        if forecast:
            db.session.delete(forecast)
            db.session.commit()

# ------------------- USER -------------------
class UserDAO:
    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(id_user):
        return User.query.get(id_user)

    @staticmethod
    def create(data):
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def add_city(id_user, id_city):
        link = UserHasCity(user_id_user=id_user, city_id_city=id_city)
        db.session.add(link)
        db.session.commit()
        return True

    @staticmethod
    def get_cities(id_user):
        user = User.query.get(id_user)
        return user.cities if user else []

# ------------------- USER PREFERENCES -------------------
class UserPreferencesDAO:
    @staticmethod
    def get_all():
        return UserPreferences.query.all()

    @staticmethod
    def get_by_id(id_preferences):
        return UserPreferences.query.get(id_preferences)

    @staticmethod
    def create(data):
        pref = UserPreferences(**data)
        db.session.add(pref)
        db.session.commit()
        return pref
