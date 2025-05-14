import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import traceback


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("600x500")

        self.api_key = "d8e1fdd9b9e645189fe104202252004"
        self.base_url = "https://api.weatherapi.com/v1"  # تم التعديل هنا

        self.city_label = tk.Label(root, text="Enter City Name:", font=("Arial", 14))
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(root, font=("Arial", 14))
        self.city_entry.pack(pady=10)

        self.search_button = tk.Button(
            root, text="Get Weather", font=("Arial", 14), command=self.get_weather
        )
        self.search_button.pack(pady=10)

        self.tab_control = ttk.Notebook(root)

        self.current_tab = ttk.Frame(self.tab_control)
        self.forecast_tab = ttk.Frame(self.tab_control)
        self.astro_tab = ttk.Frame(self.tab_control)
        self.air_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.current_tab, text="Current Weather")
        self.tab_control.add(self.forecast_tab, text="3-Day Forecast")
        self.tab_control.add(self.astro_tab, text="Astronomy")
        self.tab_control.add(self.air_tab, text="Air Quality")

        self.tab_control.pack(expand=1, fill="both")

        # Current Weather Tab
        self.current_weather_label = tk.Label(
            self.current_tab, text="", font=("Arial", 16)
        )
        self.current_weather_label.pack(pady=10)
        self.icon_label = tk.Label(self.current_tab)
        self.icon_label.pack(pady=10)

        # Forecast Tab
        self.forecast_text = tk.Text(self.forecast_tab, font=("Arial", 12), wrap="word")
        self.forecast_text.pack(padx=10, pady=10, fill="both", expand=True)

        # Astronomy Tab
        self.astro_label = tk.Label(self.astro_tab, text="", font=("Arial", 14))
        self.astro_label.pack(pady=10)

        # Air Quality Tab
        self.air_label = tk.Label(self.air_tab, text="", font=("Arial", 14))
        self.air_label.pack(pady=10)
        self.pollutants = {}
        for pollutant in ["co", "o3", "no2", "so2", "pm2_5", "pm10"]:
            label = tk.Label(self.air_tab, text="", font=("Arial", 12))
            label.pack()
            self.pollutants[pollutant] = label

        self.status_label = tk.Label(self.air_tab, text="", font=("Arial", 14))
        self.status_label.pack(pady=10)

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city name.")
            return

        try:
            # Current weather
            current_url = (
                f"{self.base_url}/current.json?key={self.api_key}&q={city}&aqi=yes"
            )
            current_data = requests.get(current_url).json()

            if "error" in current_data:
                messagebox.showerror("Error", current_data["error"]["message"])
                return

            self.update_current_tab(current_data)

            # Forecast
            forecast_url = (
                f"{self.base_url}/forecast.json?key={self.api_key}&q={city}&days=3"
            )
            forecast_data = requests.get(forecast_url).json()
            self.update_forecast_tab(forecast_data)

            # Astronomy
            astro_url = f"{self.base_url}/astronomy.json?key={self.api_key}&q={city}"
            astro_data = requests.get(astro_url).json()
            self.update_astro_tab(astro_data)

            # Air Quality
            self.update_air_tab(current_data)

        except Exception as e:
            print(traceback.format_exc())  # طباعة الخطأ الكامل للمساعدة في التتبع
            messagebox.showerror("Error", f"An unexpected error occurred:\n{str(e)}")

    def update_current_tab(self, data):
        location = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        icon_url = "https:" + data["current"]["condition"]["icon"]

        self.current_weather_label.config(
            text=f"{location}, {region}, {country}\nTemperature: {temp_c}°C\nCondition: {condition}"
        )

        try:
            icon_image = Image.open(requests.get(icon_url, stream=True).raw)
            icon_image = icon_image.resize((64, 64), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(icon_image)
            self.icon_label.config(image=photo)
            self.icon_label.image = photo
        except Exception as e:
            print(f"Error loading image: {e}")
            self.icon_label.config(image="")

    def update_forecast_tab(self, data):
        self.forecast_text.delete(1.0, tk.END)
        forecast_days = data["forecast"]["forecastday"]
        for day in forecast_days:
            date = day["date"]
            condition = day["day"]["condition"]["text"]
            avg_temp = day["day"]["avgtemp_c"]
            self.forecast_text.insert(
                tk.END, f"{date}: {condition}, Avg Temp: {avg_temp}°C\n"
            )

    def update_astro_tab(self, data):
        astro = data["astronomy"]["astro"]
        sunrise = astro["sunrise"]
        sunset = astro["sunset"]
        moonrise = astro["moonrise"]
        moonset = astro["moonset"]
        self.astro_label.config(
            text=f"Sunrise: {sunrise}, Sunset: {sunset}\nMoonrise: {moonrise}, Moonset: {moonset}"
        )

    def update_air_tab(self, data):
        air_quality = data["current"].get("air_quality", {})
        self.air_label.config(text="Air Quality Index:")

        for pollutant in self.pollutants:
            value = air_quality.get(pollutant, 0.0)
            self.pollutants[pollutant].config(text=f"{pollutant.upper()}: {value:.1f}")

        aqi = air_quality.get("us-epa-index", 0)
        status_lookup = {
            1: ("Good", "green"),
            2: ("Moderate", "yellow"),
            3: ("Unhealthy for Sensitive Groups", "orange"),
            4: ("Unhealthy", "red"),
            5: ("Very Unhealthy", "purple"),
            6: ("Hazardous", "maroon"),
        }
        status, color = status_lookup.get(aqi, ("Unknown", "black"))
        self.status_label.config(text=f"Status: {status}", fg=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
