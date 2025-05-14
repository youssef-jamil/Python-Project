import requests
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import io
from datetime import datetime
import pytz


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Complete Weather Application")
        self.root.geometry("850x650")
        self.root.resizable(True, True)

        # API Configuration
        self.api_key = (
            "d8e1fdd9b9e645189fe104202252004"  # Replace with your weatherapi.com key
        )
        self.base_url = "http://api.weatherapi.com/v1"

        # GUI Setup
        self.setup_ui()

    def setup_ui(self):
        # Configure styles
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f5f5f5")
        self.style.configure("TLabel", background="#f5f5f5", font=("Arial", 10))
        self.style.configure("Header.TLabel", font=("Arial", 16, "bold"))
        self.style.configure("Temp.TLabel", font=("Arial", 28, "bold"))
        self.style.configure("TButton", font=("Arial", 10))
        self.style.configure("TNotebook", background="#f5f5f5")
        self.style.configure("TNotebook.Tab", font=("Arial", 10, "bold"))

        # Main container
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Input Section
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)

        ttk.Label(input_frame, text="Enter City:").pack(side=tk.LEFT, padx=5)
        self.city_entry = ttk.Entry(input_frame, width=25, font=("Arial", 12))
        self.city_entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.city_entry.bind("<Return>", lambda e: self.get_weather())

        self.search_btn = ttk.Button(
            input_frame, text="Get Weather", command=self.get_weather
        )
        self.search_btn.pack(side=tk.LEFT, padx=5)

        # Notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Current Weather Tab
        self.current_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.current_tab, text="Current Weather")

        # Forecast Tab
        self.forecast_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.forecast_tab, text="3-Day Forecast")

        # Astronomy Tab
        self.astro_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.astro_tab, text="Astronomy")

        # Air Quality Tab
        self.air_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.air_tab, text="Air Quality")

        # Setup current weather tab
        self.setup_current_tab()

        # Setup forecast tab
        self.setup_forecast_tab()

        # Setup astronomy tab
        self.setup_astro_tab()

        # Setup air quality tab
        self.setup_air_tab()

        # Set default city
        self.city_entry.insert(0, "New York")

    def setup_current_tab(self):
        # Current weather display
        current_frame = ttk.Frame(self.current_tab)
        current_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Top section (icon, temp, condition)
        top_frame = ttk.Frame(current_frame)
        top_frame.pack(fill=tk.X, pady=10)

        self.weather_icon = ttk.Label(top_frame)
        self.weather_icon.pack(side=tk.LEFT, padx=20)

        info_frame = ttk.Frame(top_frame)
        info_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.location_label = ttk.Label(info_frame, style="Header.TLabel")
        self.location_label.pack(anchor="w")

        self.local_time = ttk.Label(info_frame)
        self.local_time.pack(anchor="w")

        self.temp_label = ttk.Label(info_frame, style="Temp.TLabel")
        self.temp_label.pack(anchor="w")

        self.condition_label = ttk.Label(info_frame)
        self.condition_label.pack(anchor="w")

        # Details section
        details_frame = ttk.LabelFrame(
            current_frame, text="Weather Details", padding=10
        )
        details_frame.pack(fill=tk.BOTH, expand=True)

        # Create grid for details
        self.current_details = {}
        params = [
            ("Humidity", "humidity", "%"),
            ("Wind Speed", "wind_kph", "km/h"),
            ("Wind Direction", "wind_dir", ""),
            ("Pressure", "pressure_mb", "mb"),
            ("Precipitation", "precip_mm", "mm"),
            ("Cloud Cover", "cloud", "%"),
            ("Visibility", "vis_km", "km"),
            ("Feels Like", "feelslike_c", "°C"),
            ("UV Index", "uv", ""),
            ("Last Updated", "last_updated", ""),
        ]

        for i, (name, key, unit) in enumerate(params):
            row = i % 5
            col = i // 5

            frame = ttk.Frame(details_frame)
            frame.grid(row=row, column=col, sticky="w", padx=10, pady=5)

            ttk.Label(frame, text=f"{name}:").pack(side=tk.LEFT)
            value_label = ttk.Label(frame, font=("Arial", 10, "bold"))
            value_label.pack(side=tk.LEFT)
            ttk.Label(frame, text=unit).pack(side=tk.LEFT)

            self.current_details[key] = value_label

    def setup_forecast_tab(self):
        # Forecast display (3 days)
        self.forecast_days = []

        for i in range(3):
            day_frame = ttk.Frame(self.forecast_tab)
            day_frame.pack(fill=tk.X, padx=10, pady=5)

            # Day header
            header = ttk.Label(day_frame, font=("Arial", 12, "bold"))
            header.pack(anchor="w")

            # Forecast details
            details_frame = ttk.Frame(day_frame)
            details_frame.pack(fill=tk.X)

            # Morning
            morn_frame = ttk.LabelFrame(details_frame, text="Morning", padding=5)
            morn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

            # Afternoon
            aft_frame = ttk.LabelFrame(details_frame, text="Afternoon", padding=5)
            aft_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

            # Evening
            eve_frame = ttk.LabelFrame(details_frame, text="Evening", padding=5)
            eve_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

            # Night
            night_frame = ttk.LabelFrame(details_frame, text="Night", padding=5)
            night_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

            self.forecast_days.append(
                {
                    "header": header,
                    "morning": morn_frame,
                    "afternoon": aft_frame,
                    "evening": eve_frame,
                    "night": night_frame,
                }
            )

    def setup_astro_tab(self):
        # Astronomy information
        astro_frame = ttk.Frame(self.astro_tab)
        astro_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(astro_frame, text="Today's Astronomy", style="Header.TLabel").pack(
            anchor="w"
        )

        # Sun and moon frames
        sun_frame = ttk.LabelFrame(astro_frame, text="Sun", padding=10)
        sun_frame.pack(fill=tk.X, pady=5)

        moon_frame = ttk.LabelFrame(astro_frame, text="Moon", padding=10)
        moon_frame.pack(fill=tk.X, pady=5)

        # Sun times
        self.sun_times = {}
        sun_events = [
            ("Sunrise", "sunrise"),
            ("Solar Noon", "sunrise"),  # Placeholder
            ("Sunset", "sunset"),
            ("Twilight", "sunset"),  # Placeholder
        ]

        for i, (name, key) in enumerate(sun_events):
            frame = ttk.Frame(sun_frame)
            frame.grid(row=i // 2, column=i % 2, sticky="w", padx=10, pady=5)

            ttk.Label(frame, text=f"{name}:").pack(side=tk.LEFT)
            value_label = ttk.Label(frame, font=("Arial", 10, "bold"))
            value_label.pack(side=tk.LEFT)

            self.sun_times[key + str(i)] = value_label

        # Moon phases
        self.moon_info = {}
        moon_data = [
            ("Moon Phase", "moon_phase"),
            ("Illumination", "moon_illumination"),
            ("Moonrise", "moonrise"),
            ("Moonset", "moonset"),
        ]

        for i, (name, key) in enumerate(moon_data):
            frame = ttk.Frame(moon_frame)
            frame.grid(row=i // 2, column=i % 2, sticky="w", padx=10, pady=5)

            ttk.Label(frame, text=f"{name}:").pack(side=tk.LEFT)
            value_label = ttk.Label(frame, font=("Arial", 10, "bold"))
            value_label.pack(side=tk.LEFT)

            self.moon_info[key] = value_label

    def setup_air_tab(self):
        # Air quality information
        air_frame = ttk.Frame(self.air_tab)
        air_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(air_frame, text="Air Quality Index", style="Header.TLabel").pack(
            anchor="w"
        )

        # Air quality index
        self.aqi_frame = ttk.LabelFrame(
            air_frame, text="Air Quality Index (AQI)", padding=10
        )
        self.aqi_frame.pack(fill=tk.X, pady=5)

        self.aqi_value = ttk.Label(self.aqi_frame, font=("Arial", 24, "bold"))
        self.aqi_value.pack()

        self.aqi_status = ttk.Label(self.aqi_frame, font=("Arial", 12))
        self.aqi_status.pack()

        # Pollutants
        pollutants_frame = ttk.LabelFrame(air_frame, text="Pollutants", padding=10)
        pollutants_frame.pack(fill=tk.X, pady=5)

        self.pollutants = {}
        pollutants = [
            ("Carbon Monoxide", "co"),
            ("Ozone", "o3"),
            ("Nitrogen Dioxide", "no2"),
            ("Sulfur Dioxide", "so2"),
            ("PM2.5", "pm2_5"),
            ("PM10", "pm10"),
        ]

        for i, (name, key) in enumerate(pollutants):
            frame = ttk.Frame(pollutants_frame)
            frame.grid(row=i // 2, column=i % 2, sticky="w", padx=10, pady=5)

            ttk.Label(frame, text=f"{name}:").pack(side=tk.LEFT)
            value_label = ttk.Label(frame, font=("Arial", 10, "bold"))
            value_label.pack(side=tk.LEFT)
            ttk.Label(frame, text="μg/m³").pack(side=tk.LEFT)

            self.pollutants[key] = value_label

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showwarning("Error", "Please enter a city name")
            return

        try:
            self.search_btn.config(state="disabled", text="Loading...")
            self.root.update()

            # Get current weather
            current_url = (
                f"{self.base_url}/current.json?key={self.api_key}&q={city}&aqi=yes"
            )
            current_response = requests.get(current_url, timeout=10)
            current_response.raise_for_status()
            current_data = current_response.json()

            # Get forecast
            forecast_url = (
                f"{self.base_url}/forecast.json?key={self.api_key}&q={city}&days=3"
            )
            forecast_response = requests.get(forecast_url, timeout=10)
            forecast_response.raise_for_status()
            forecast_data = forecast_response.json()

            # Update all displays
            self.update_current_tab(current_data)
            self.update_forecast_tab(forecast_data)
            self.update_astro_tab(forecast_data)
            self.update_air_tab(current_data)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch weather data:\n{str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred:\n{str(e)}")
        finally:
            self.search_btn.config(state="normal", text="Get Weather")

    def update_current_tab(self, data):
        # Location and time
        location = data["location"]
        current = data["current"]

        self.location_label.config(text=f"{location['name']}, {location['country']}")
        local_time = datetime.strptime(location["localtime"], "%Y-%m-%d %H:%M")
        self.local_time.config(
            text=f"Local Time: {local_time.strftime('%Y-%m-%d %H:%M')}"
        )

        # Weather icon
        icon_url = "https:" + current["condition"]["icon"]
        self.load_weather_icon(icon_url)

        # Temperature and condition
        self.temp_label.config(text=f"{current['temp_c']}°C")
        self.condition_label.config(text=current["condition"]["text"])

        # Update details
        self.current_details["humidity"].config(text=current["humidity"])
        self.current_details["wind_kph"].config(text=current["wind_kph"])
        self.current_details["wind_dir"].config(text=current["wind_dir"])
        self.current_details["pressure_mb"].config(text=current["pressure_mb"])
        self.current_details["precip_mm"].config(text=current["precip_mm"])
        self.current_details["cloud"].config(text=current["cloud"])
        self.current_details["vis_km"].config(text=current["vis_km"])
        self.current_details["feelslike_c"].config(text=current["feelslike_c"])
        self.current_details["uv"].config(text=current["uv"])
        self.current_details["last_updated"].config(
            text=current["last_updated"].split()[1]
        )

    def update_forecast_tab(self, data):
        forecast_days = data["forecast"]["forecastday"]

        for i, day in enumerate(forecast_days):
            if i >= 3:  # Only show 3 days
                break

            date = datetime.strptime(day["date"], "%Y-%m-%d")
            self.forecast_days[i]["header"].config(text=date.strftime("%A, %Y-%m-%d"))

            # Get hourly data and group by time of day
            hours = day["hour"]

            # Morning (6-11)
            morn_hours = [
                h for h in hours if 6 <= int(h["time"].split()[1].split(":")[0]) < 12
            ]
            morn_avg = self.calculate_period_avg(morn_hours)
            self.update_forecast_period(self.forecast_days[i]["morning"], morn_avg)

            # Afternoon (12-17)
            aft_hours = [
                h for h in hours if 12 <= int(h["time"].split()[1].split(":")[0]) < 18
            ]
            aft_avg = self.calculate_period_avg(aft_hours)
            self.update_forecast_period(self.forecast_days[i]["afternoon"], aft_avg)

            # Evening (18-23)
            eve_hours = [
                h for h in hours if 18 <= int(h["time"].split()[1].split(":")[0]) < 24
            ]
            eve_avg = self.calculate_period_avg(eve_hours)
            self.update_forecast_period(self.forecast_days[i]["evening"], eve_avg)

            # Night (0-5)
            night_hours = [
                h for h in hours if 0 <= int(h["time"].split()[1].split(":")[0]) < 6
            ]
            night_avg = self.calculate_period_avg(night_hours)
            self.update_forecast_period(self.forecast_days[i]["night"], night_avg)

    def calculate_period_avg(self, hours):
        if not hours:
            return None

        avg = {
            "temp_c": sum(h["temp_c"] for h in hours) / len(hours),
            "condition": hours[len(hours) // 2]["condition"]["text"],
            "icon": hours[len(hours) // 2]["condition"]["icon"],
            "humidity": sum(h["humidity"] for h in hours) / len(hours),
            "wind_kph": sum(h["wind_kph"] for h in hours) / len(hours),
            "chance_of_rain": sum(h["chance_of_rain"] for h in hours) / len(hours),
        }

        return avg

    def update_forecast_period(self, frame, period):
        # Clear previous widgets
        for widget in frame.winfo_children():
            widget.destroy()

        if not period:
            ttk.Label(frame, text="No data").pack()
            return

        # Load icon
        try:
            icon_url = "https:" + period["icon"]
            response = requests.get(icon_url, timeout=5)
            image_data = response.content
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((40, 40), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            icon_label = ttk.Label(frame, image=photo)
            icon_label.image = photo
            icon_label.pack()
        except:
            pass

        ttk.Label(
            frame, text=f"{period['temp_c']:.1f}°C", font=("Arial", 12, "bold")
        ).pack()
        ttk.Label(frame, text=period["condition"], wraplength=150).pack()
        ttk.Label(frame, text=f"Humidity: {period['humidity']:.0f}%").pack()
        ttk.Label(frame, text=f"Wind: {period['wind_kph']:.1f} km/h").pack()
        ttk.Label(frame, text=f"Rain: {period['chance_of_rain']:.0f}%").pack()

    def update_astro_tab(self, data):
        astro = data["forecast"]["forecastday"][0]["astro"]

        # Sun times
        self.sun_times["sunrise0"].config(text=astro["sunrise"])
        self.sun_times["sunrise1"].config(text=astro["sunrise"])
        self.sun_times["sunset0"].config(text=astro["sunset"])
        self.sun_times["sunset1"].config(text=astro["sunset"])

        # Moon data
        self.moon_info["moon_phase"].config(text=astro["moon_phase"])
        self.moon_info["moon_illumination"].config(
            text=f"{astro['moon_illumination']}%"
        )
        self.moon_info["moonrise"].config(text=astro["moonrise"])
        self.moon_info["moonset"].config(text=astro["moonset"])

    def update_air_tab(self, data):
        air_quality = data["current"]["air_quality"]

        # AQI value
        aqi = air_quality.get("us-epa-index", 0)
        self.aqi_value.config(text=str(aqi))

        # AQI status
        if aqi <= 50:
            status = "Good - Little or no risk"
            color = "green"
        elif aqi <= 100:
            status = "Moderate - Acceptable"
            color = "yellow"
        elif aqi <= 150:
            status = "Unhealthy for Sensitive Groups"
            color = "orange"
        elif aqi <= 200:
            status = "Unhealthy"
            color = "red"
        elif aqi <= 300:
            status = "Very Unhealthy"
            color = "purple"
        else:
            status = "Hazardous"
            color = "maroon"

        self.aqi_status.config(text=status, foreground=color)

        # Pollutants
        self.pollutants["co"].config(text=f"{air_quality['co']:.1f}")
        self.pollutants["o3"].config(text=f"{air_quality['o3']:.1f}")
        self.pollutants["no2"].config(text=f"{air_quality['no2']:.1f}")
        self.pollutants["so2"].config(text=f"{air_quality['so2']:.1f}")
        self.pollutants["pm2_5"].config(text=f"{air_quality['pm2_5']:.1f}")
        self.pollutants["pm10"].config(text=f"{air_quality['pm10']:.1f}")

    def load_weather_icon(self, url):
        try:
            response = requests.get(url, timeout=5)
            image_data = response.content
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((100, 100), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            self.weather_icon.config(image=photo)
            self.weather_icon.image = photo
        except Exception as e:
            print(f"Error loading icon: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
