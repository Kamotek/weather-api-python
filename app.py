from flask import Flask, render_template
import requests

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        # Współrzędne dla Warszawy
        lat = 52.2297
        lon = 21.0122
        # Budujemy URL do API z parametrem current_weather=true i jednostkami w stopniach Celsjusza
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&temperature_unit=celsius"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current = data.get("current_weather", {})
            temperature = current.get("temperature")
            windspeed = current.get("windspeed")
            winddirection = current.get("winddirection")
            weathercode = current.get("weathercode")
            time = current.get("time")
            
            return render_template("index.html", 
                                temperature=temperature, 
                                windspeed=windspeed, 
                                winddirection=winddirection, 
                                weathercode=weathercode,
                                time=time)
        else:
            return "Nie udało się pobrać danych pogodowych."

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
