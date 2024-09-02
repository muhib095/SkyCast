# SkyCast
A simple Tkinter-based GUI application that provides weather information based on user input or the device's location. The app fetches weather data from the OpenWeatherMap API.

![image](https://github.com/user-attachments/assets/58f6739c-63a9-476b-bfc5-e90436cfb5a3)

## Features
Search by City Name: Enter the name of a city to get the current weather information.
Get Device Location: Retrieve the weather information based on the device's current location using IP geolocation.

## Prerequisites
Ensure you have the following Python packages installed:

requests: For making HTTP requests to the OpenWeatherMap API.
geocoder: For retrieving the device's location based on IP address.

You can install the required packages using pip:
```
pip install requests
pip install geocoder
```

## Usage
1. Search by City Name:
- Enter a city name in the input field.
- Click the Search button to retrieve weather information for the specified city.

2. Get Device Location:
- Click the Get Device Location button to fetch weather information based on your device's current location.

## Code Overview
- getWeather(): Retrieves weather data based on the city name entered in the input field. Displays the temperature and weather description in a message box.
- getDeviceLocationWeather(): Retrieves weather data based on the device's IP-based location. Displays the temperature and weather description in a message box.
GUI Elements:
- City Input Field: Text area where users can enter the city name.
- Search Button: Triggers the weather data retrieval for the city name.
- Get Device Location Button: Retrieves and displays weather data based on the device's location.
- Labels: For displaying app name, instructions, and separating functionality.

## Example
After running the application, you'll see a window where you can:
- Enter a city name and click Search to see the weather information for that city.
- Click Get Device Location to see the weather information for your current location.

Error Handling
The app handles various exceptions, including:
- HTTP Errors: Issues with the API request.
- Request Errors: Problems with making the HTTP request.
- General Errors: Any other unexpected errors.
If an error occurs, an appropriate message will be shown in a dialog box.

## Links

Contact @ ullah.muhib095@gmail.com

Linkedin @ https://www.linkedin.com/in/muhib095/
