import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    api_key = "d8e1fdd9b9e645189fe104202252004"  # Replace with your actual API key from weatherapi.com
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    try:
        # Show loading state
        search_btn.config(state="disabled", text="Fetching...")
        root.update()

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Update weather display
        update_weather_display(data)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", f"Failed to get weather data:\n{str(e)}")
    except ValueError as e:
        messagebox.showerror("API Error", "Invalid response from weather service")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{str(e)}")
    finally:
        search_btn.config(state="normal", text="Get Weather")


def update_weather_display(data):
    # Clear previous data
    for widget in weather_frame.winfo_children():
        widget.destroy()

    # Get weather data
    location = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    wind_kph = data["current"]["wind_kph"]
    icon_url = "https:" + data["current"]["condition"]["icon"]

    # Display location
    location_label = ttk.Label(
        weather_frame, text=f"{location}, {country}", font=("Arial", 14, "bold")
    )
    location_label.pack(pady=(0, 10))

    # Display temperature
    temp_label = ttk.Label(
        weather_frame, text=f"{temp_c}°C", font=("Arial", 24, "bold")
    )
    temp_label.pack()

    # Display condition
    condition_label = ttk.Label(weather_frame, text=condition, font=("Arial", 12))
    condition_label.pack(pady=5)

    # Display details in a grid
    details_frame = ttk.Frame(weather_frame)
    details_frame.pack(pady=10)

    ttk.Label(details_frame, text=f"Humidity: {humidity}%").grid(
        row=0, column=0, padx=10, sticky="w"
    )
    ttk.Label(details_frame, text=f"Wind: {wind_kph} km/h").grid(
        row=0, column=1, padx=10, sticky="w"
    )

    # Try to display icon (optional)
    try:
        icon_data = requests.get(icon_url, timeout=5).content
        icon_img = tk.PhotoImage(data=icon_data)
        icon_label = ttk.Label(weather_frame, image=icon_img)
        icon_label.image = icon_img  # Keep reference
        icon_label.pack()
    except:
        pass  # Skip if icon can't be loaded


# Create main window
root = tk.Tk()
root.title("Weather App")
root.geometry("350x400")
root.resizable(False, False)

# Configure style
style = ttk.Style()
style.configure("TFrame", background="#f5f5f5")
style.configure("TLabel", background="#f5f5f5")
style.configure("TButton", font=("Arial", 10))

# Main container
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# City input
ttk.Label(main_frame, text="Enter City Name:").pack(pady=(0, 5))
city_entry = ttk.Entry(main_frame, font=("Arial", 12))
city_entry.pack(fill=tk.X, pady=(0, 10))
city_entry.focus()

# Search button
search_btn = ttk.Button(main_frame, text="Get Weather", command=get_weather)
search_btn.pack(fill=tk.X, pady=(0, 15))

# Weather display frame
weather_frame = ttk.Frame(main_frame, relief=tk.GROOVE, borderwidth=1, padding="10")
weather_frame.pack(fill=tk.BOTH, expand=True)

# Initial placeholder text
ttk.Label(
    weather_frame,
    text="Weather data will appear here",
    font=("Arial", 10, "italic"),
    foreground="gray",
).pack(expand=True)

# Run the application
root.mainloop()
