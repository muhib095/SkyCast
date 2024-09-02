import requests  # Import the requests module for making HTTP requests
from tkinter import *  # Import all classes and functions from tkinter for GUI creation
from tkinter import messagebox  # Import messagebox for showing dialog boxes
from tkinter import ttk  # Import ttk module for themed widgets (though not used in this code)
import geocoder  # Import geocoder for retrieving device location

# Ensure these packages are installed via pip
# pip install requests 
# pip install geocoder

# Load API key from environment variable
api_key = "YOUR_API_KEY"  # API key for OpenWeatherMap

def getWeather():
    # Retrieve the city name from the input field
    city_name = input_field.get("1.0", "end-1c").strip()
    
    # Check if the city name was provided
    if not city_name:
        messagebox.showwarning("Input Error", "Please enter a city name.")  # Show warning if input is empty
        return
    
    # Construct the API request URL with the city name
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)  # Make a GET request to the weather API
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse the response data as JSON

        # Check if the request was successful
        if response.status_code == 200:
            temp = data['main']['temp']  # Extract the temperature from the JSON data
            weather_desc = data['weather'][0]['description']  # Extract weather description
            result = f"Temperature: {temp}°C\nWeather: {weather_desc.capitalize()}"  # Format the result string
        else:
            result = f"City not found or error fetching data. Status code: {response.status_code}"  # Handle other response codes

        messagebox.showinfo("Weather Info", result)  # Display the weather info in a message box
        input_field.delete("1.0", "end")  # Clear the input field
    except requests.exceptions.HTTPError as http_err:
        messagebox.showerror("HTTP Error", f"HTTP error occurred: {http_err}")  # Handle HTTP errors
    except requests.exceptions.RequestException as req_err:
        messagebox.showerror("Request Error", f"Request error occurred: {req_err}")  # Handle request errors
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")  # Handle any other exceptions

def getDeviceLocationWeather():
    g = geocoder.ip('me')  # Retrieve the device's location based on IP address
    lat, lon = g.latlng  # Extract latitude and longitude from the geocoder response
    if lat is None or lon is None:
        messagebox.showerror("Location Error", "Could not retrieve device location.")  # Show error if location could not be retrieved
        return
    
    # Construct the API request URL with latitude and longitude
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)  # Make a GET request to the weather API
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse the response data as JSON

        # Check if the request was successful
        if response.status_code == 200:
            temp = data['main']['temp']  # Extract the temperature from the JSON data
            weather_desc = data['weather'][0]['description']  # Extract weather description
            result = f"Temperature: {temp}°C\nWeather: {weather_desc.capitalize()}"  # Format the result string
        else:
            result = f"Error fetching data. Status code: {response.status_code}"  # Handle other response codes

        messagebox.showinfo("Weather Info", result)  # Display the weather info in a message box
    except requests.exceptions.HTTPError as http_err:
        messagebox.showerror("HTTP Error", f"HTTP error occurred: {http_err}")  # Handle HTTP errors
    except requests.exceptions.RequestException as req_err:
        messagebox.showerror("Request Error", f"Request error occurred: {req_err}")  # Handle request errors
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")  # Handle any other exceptions

# Create a new Tkinter window
window = Tk()
window.title("Weather App")  
window.geometry("375x275")  
window.configure(background='#141414')  
window.resizable(False, False)  

# Create a label for the app name
AppName = Label(window, text="Weather App", fg='#FFC300', bg='#141414', font=('Ariel', 15))  
AppName.place(x=20, y=20)  # Position the label

# Create a label for city input
city = Label(window, text="Enter city name", fg='white', bg='#141414', font=('Ariel', 10))  
city.place(x=20, y=65)  

# Create a frame to hold the input text field
frame = Frame(window)
frame.place(x=20, y=90) 

# Create an input text field for the city name
input_field = Text(frame, height=2, width=17, font=('Ariel', 18))
input_field.pack()  

# Create a button to trigger weather data retrieval based on city name
search = Button(window, text='Search', height=3, width=13, bg='blue', fg='white', command=getWeather)
search.place(x=260, y=90) 

# Create a label to separate the two functionalities
line = Label(window, text="----------------------------------------or----------------------------------------", fg='white', bg='#141414', font=('Ariel', 10))
line.place(x=20, y=150)  

# Create a button to trigger weather data retrieval based on device location
location = Button(window, text='Get Device Location', height=3, width=47, bg='purple', fg='white', command=getDeviceLocationWeather)
location.place(x=20, y=180)  

window.mainloop()  # Start the Tkinter event loop
