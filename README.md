# CLI To-Do List Application

A simple command-line tool for fetching weather information using Python and OpenWeatherMap API.

## Features

- Fetch current weather for a specified city
- Display temperature, humidity, and weather conditions
- Choose between Celsius and Fahrenheit units

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ColdByDefault/weatherCLI.git
   ```
2. Navigate into the project directory:   
    ```bash
    cd weather-cli-tool
    ```
3. Create env:
    ```bash
    python -m venv venv
    ```
###### venv
    ```bash
    python -m pip install --user virtualenv
    ```

## Usage
1. Activate the virtual environment:
    ```bash
    source venv/bin/activate    # On macOS/Linux
    .\venv\Scripts\activate     # On Windows
    ```
2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python weather.py
    ```


## Contributing

1.    Fork the repository
2.    Create a new branch (git checkout -b feature/your-feature)
3.    Commit your changes (git commit -m 'Add your feature')
4.    Push to the branch (git push origin feature/your-feature)
5.    Create a new Pull Request

