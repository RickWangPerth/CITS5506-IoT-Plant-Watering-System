# CITS5506 The Internet of Things SEM-2 Group Project
### The University of Western Australia 
### Group 8: Smart Plant Watering and Monitoring System 
#### Jai Castle (22465418) & Blake Fordham (22708346) & Leon Li (23031208) & Wenjie Song (22470722) & Xinlyu Wang (22200099)

## How to launch the web application
Clone this application to local directory <code> git clone https://github.com/RickWangPerth/CITS5506-IoT-Plant-Watering-System.git </code> <br>
 <br>
Set up python virtual environment <code> python3 -m venv venv </code> <br>
 <br>
Activate the python virtual environment <code> source venv/bin/activate </code> <br>
 <br>
Download the required packages <code> pip install -r requirements.txt </code> <br>
 <br>
Upgrade the database: <code> flask db upgrade </code> <br>
<br>
Launch the web application: <code> flask run </code> <br>
 <br>
Go to the generated url, you can see the application on the website.
 <br>
 <br>
Stop the web application: <code> ^C </code> <br>

Exit the environment: <code> deactivate </code>


## Source code
The source code is organised under the `app` directory.

- **sensors** directory: classes for managing each of the sensors in the project.
  - **VEML6030** directory: contains the PiicoDev VEML6030 Library [2].
  - **tests** directory: contains code for testing each sensor individually.
  - `Camera.py`: manages the connection to the camera and taking pictures.
  - `Collect_sensors.py`: centrally manages all connected sensors.
  - `Moisture_sensor.py`: returns the moisture percentage by reading the analogue value from the moisture sensor.
  - `Temperature_sensor.py`: returns the temperature by reading the analogue value from the moisture sensor.
  - `Water_level_sensor.py`: returns the state of the water level by reading the digital input from the water level sensor.
- **static** directory: contains CSS, JavaScript and images required for the user interface.
  - **CSS** directory: Contains the style.css file with the CSS styles for the user interface.
  - **images** directory: contains the emojis, images and logos used in the user interface. This directory will also contain the images taken of the plant once this occurs.
  - **JS** directory: contains JavaScript files for the Index, Historical, and Advanced pages. These scripts facilitate the functionality of the website (pressing buttons, etc) and updating the values on the screen in near real-time.
- **templates** directory: Stores the Jinja HTML templates used for rendering the user interface. This directory consists of a template for the Index, Historical and Advanced pages – all of which extend the base template that includes elements common to all pages.
- `__init__.py`: Initialises the Flask application, SQLite Database and other objects when the application starts.
- `Automatic_watering.py`: contains a class that will check whether automatic watering of the plant is required, based on the most recent sensor data.
- `Models.py`: defines the ‘Settings’ and ‘History’ database tables for the SQLite database.
- `Pump.py`: defines a class that facilitates turning the water pump on or off (via the 5V relay).
- `Routes.py`: defines each of the website’s HTTP routes and the responses that are returned 
