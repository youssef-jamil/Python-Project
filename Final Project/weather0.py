import requests
import tkinter as tk
from tkinter import messagebox


def get_weather():
    city = city_entry.get()
    api_key = "d8e1fdd9b9e645189fe104202252004"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&lang=en"

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            messagebox.showerror("Error", f"Error: {data['error']['message']}")
        else:
            location = data["location"]["name"]
            country = data["location"]["country"]
            temp_c = data["current"]["temp_c"]
            humidity = data["current"]["humidity"]
            wind_kph = data["current"]["wind_kph"]
            pressure_mb = data["current"]["pressure_mb"]
            precip_mm = data["current"]["precip_mm"]

            result = f"Location: {location}, {country}\n"
            result += f"Temperature: {temp_c}°C\n"
            result += f"Humidity: {humidity}%\n"
            result += f"Wind Speed: {wind_kph} km/h\n"
            result += f"Pressure: {pressure_mb} mb\n"
            result += f"Precipitation: {precip_mm} mm"

            weather_text.config(state="normal")
            weather_text.delete(1.0, tk.END)
            weather_text.insert(tk.END, result)
            weather_text.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")


root = tk.Tk()
root.title("Weather App")
root.geometry("350x350")
root.resizable(False, False)

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(root, text="Search", font=("Arial", 12), command=get_weather).pack(pady=10)

weather_text = tk.Text(root, height=12, width=40, font=("Arial", 10))
weather_text.pack(pady=10)
weather_text.config(state="disabled")

root.mainloop()
