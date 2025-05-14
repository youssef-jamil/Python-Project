import requests
import tkinter as tk
from tkinter import messagebox


def get_weather():
    city = city_entry.get()
    api_key = "d8e1fdd9b9e645189fe104202252004"  # API key
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
            precip_mm = data["current"].get("precip_mm", 0)
            condition = data["current"]["condition"]["text"]
            feels_like = data["current"]["feelslike_c"]
            cloud_coverage = data["current"]["cloud"]
            uv_index = data["current"]["uv"]

            # If precipitation is 0, display no precipitation
            if precip_mm == 0:
                precip_mm = "No precipitation"

            # Displaying the data
            result = f"Location: {location}, {country}\n"
            result += f"Temperature: {temp_c}°C\n"
            result += f"Feels Like: {feels_like}°C\n"
            result += f"Humidity: {humidity}%\n"
            result += f"Wind Speed: {wind_kph} km/h\n"
            result += f"Pressure: {pressure_mb} mb\n"
            result += f"Precipitation: {precip_mm}\n"
            result += f"Condition: {condition}\n"
            result += f"Cloud Coverage: {cloud_coverage}%\n"
            result += f"UV Index: {uv_index}"

            # Display result in the Text widget
            weather_text.config(state="normal")
            weather_text.delete(1.0, tk.END)
            weather_text.insert(tk.END, result)
            weather_text.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")


# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.resizable(False, False)

# City input
tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

# Search button
tk.Button(root, text="Search", font=("Arial", 12), command=get_weather).pack(pady=10)

# Text area for result
weather_text = tk.Text(root, height=15, width=45, font=("Arial", 10))
weather_text.pack(pady=10)
weather_text.config(state="disabled")  # Make it read-only

# Run the GUI
root.mainloop()
