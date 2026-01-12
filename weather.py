import tkinter as tk
import requests

API_KEY = "PASTE_YOUR_API_KEY_HERE"

def get_weather():
    city = city_entry.get()
    if city == "":
        result_label.config(text="Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"].title()

        result_label.config(
            text=f"City: {city.title()}\n"
                 f"Temperature: {temp} °C\n"
                 f"Humidity: {humidity}%\n"
                 f"Weather: {weather}"
        )
    else:
        result_label.config(text="City not found")

app = tk.Tk()
app.title("Weather App")
app.geometry("320x400")
app.configure(bg="#e3f2fd")

tk.Label(
    app,
    text="Weather App",
    font=("Arial", 18, "bold"),
    bg="#2196f3",
    fg="white",
    pady=10
).pack(fill="x")

tk.Label(
    app,
    text="Enter City Name",
    bg="#e3f2fd",
    font=("Arial", 12)
).pack(pady=10)

city_entry = tk.Entry(app, font=("Arial", 14), justify="center")
city_entry.pack(pady=5)

tk.Button(
    app,
    text="Check Weather",
    font=("Arial", 12),
    bg="#4caf50",
    fg="white",
    command=get_weather
).pack(pady=15)

result_label = tk.Label(
    app,
    text="",
    font=("Arial", 12),
    bg="white",
    fg="black",
    justify="left",
    padx=10,
    pady=10
)
result_label.pack(pady=10, fill="x", padx=20)

app.mainloop()
