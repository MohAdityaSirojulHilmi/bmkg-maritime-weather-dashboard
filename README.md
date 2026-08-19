# BMKG Tanjung Perak Maritime Weather Monitoring Dashboard

A web-based maritime weather monitoring dashboard developed during an internship at the Meteorological, Climatological, and Geophysical Agency (BMKG) Maritime Meteorological Station Perak II, Surabaya.

The dashboard integrates Automatic Weather Station (AWS) observations, meteorological imagery, maritime weather model imagery, and early warning information into a single monitoring interface.

The project was developed as a supporting tool for maritime weather information and disaster mitigation activities in the BMKG operational area.

## Project Overview

Maritime weather information is obtained from various observation and visualization sources, including Automatic Weather Station (AWS) data, satellite imagery, and maritime weather model products.

This project integrates these different sources into a web-based dashboard using Python and Flask.

The dashboard provides a centralized interface for monitoring:

- AWS meteorological observations
- Cloud Cluster imagery
- Himawari satellite imagery
- Ocean current model imagery
- Wave model imagery
- Wind model imagery
- Maritime early warning information

The system combines data processing, meteorological imagery processing, time-series image visualization, and web-based dashboard development.

## Project Objectives

The main objectives of this project are:

- To develop an integrated maritime weather monitoring dashboard.
- To visualize AWS observation data in an accessible interface.
- To integrate meteorological and maritime imagery into a single dashboard.
- To transform time-series meteorological imagery into video visualizations.
- To present early warning information in a centralized interface.
- To support the availability of maritime weather information for disaster mitigation activities.

## System Workflow

The system consists of several data processing pipelines that are integrated into a single Flask-based dashboard.

### 1. AWS Observation Data

AWS observation data is processed using Python and Pandas.

```text
AWS Observation Data
        │
        ▼
Data Reading
        │
        ▼
Data Validation & Preprocessing
        │
        ▼
Latest AWS Observation
        │
        ├──────────────► Dashboard Information
        │
        ▼
Last 1,440 Observations
        │
        ▼
Matplotlib Visualization
        │
        ▼
AWS Graph
        │
        ▼
Dashboard
```
The AWS data includes several meteorological parameters such as:

* Wind speed
* Wind direction
* Temperature
* Relative humidity
* Atmospheric pressure
* Water level
* Water temperature

### 2. Cloud Cluster Imagery

Cloud Cluster imagery is produced through a processing workflow using GrADS.

```text
Meteorological Data
        │
        ▼
GrADS Processing
        │
        ▼
Cloud Cluster Images
        │
        ▼
Time-Series Image Collection
        │
        ▼
Image-to-Video Processing
        │
        ▼
Cloud Cluster Video
        │
        ▼
Dashboard
```
### 3. Himawari Satellite Imagery

Himawari imagery is obtained from a web-based source. Images are collected at three-hour intervals and then combined into a video to provide a time-series visualization.

```text
Himawari Imagery
      │
      ▼
Images at 3-Hour Intervals
      │
      ▼
Time-Series Image Collection
      │
      ▼
Image-to-Video Processing
      │
      ▼
Himawari Video
      │
      ▼
Dashboard
```

### 4. Maritime Weather Model Imagery

Maritime weather model products are available as images at three-hour intervals.

The model imagery consists of:

* Ocean current
* Wave
* Wind

Each series of images is combined into a video for visualization in the dashboard.

```text
Model Images
      │
      ├── Ocean Current
      ├── Wave
      └── Wind
              │
              ▼
      Images at 3-Hour Intervals
              │
              ▼
      Time-Series Image Collection
              │
              ▼
      Image-to-Video Processing
              │
              ▼
      Model Visualization Videos
              │
              ▼
           Dashboard
```

### 5. Early Warning Information

Early warning information is processed from an Excel dataset using Python and Pandas.

```text
Early Warning Data
        │
        ▼
Excel Data Reading
        │
        ▼
Data Validation
        │
        ▼
Time & Wind Speed Processing
        │
        ▼
Warning Period & Wind Speed Range
        │
        ▼
Dashboard
```

The system extracts information such as:

* Warning start date
* Warning end date
* Warning start time
* Warning end time
* Potential wind speed range

### 6. Dashboard Integration

All processed information is integrated into a Flask web application.

```text
AWS Data ──────────────────┐
                           │
Cloud Cluster Video ───────┤
                           │
Himawari Video ────────────┤
                           │
Current Model Video ───────┤
Wave Model Video ──────────┤
Wind Model Video ──────────┤
                           │
Early Warning Information ─┘
              │
              ▼
      Flask Web Application
              │
              ▼
        HTML / CSS / JS
              │
              ▼
 Maritime Weather Monitoring
          Dashboard
```

## Dashboard Features

The dashboard provides an integrated view of several maritime weather information sources.

### AWS Monitoring

The dashboard displays the latest available AWS observations, including:

* Wind speed
* Wind direction
* Temperature
* Relative humidity
* Atmospheric pressure
* Water temperature
* Water level

The dashboard also provides graphical visualization of selected AWS parameters.

### Meteorological Imagery

The dashboard provides video-based visualization of:

* Cloud Cluster
* Himawari satellite imagery
* Ocean current model
* Wave model
* Wind model

### Early Warning Information

The dashboard displays early warning information including the warning period and potential wind speed range.

The warning information is also supported by a browser-based text-to-speech feature to read the warning information aloud.

## Project Results

The project resulted in a web-based maritime weather monitoring dashboard that integrates multiple meteorological information sources into a single interface.

The main results include:

* A functional Flask-based maritime weather monitoring dashboard.
* Integration of AWS observation data into the dashboard.
* Automated processing and visualization of AWS observations using Python, Pandas, NumPy, and Matplotlib.
* Integration of Cloud Cluster imagery produced through GrADS processing.
* Conversion of time-series Cloud Cluster imagery into video visualization.
* Integration of Himawari imagery obtained from a web-based source.
* Conversion of three-hourly Himawari imagery into time-series video visualization.
* Integration of three-hourly ocean current, wave, and wind model imagery.
* Conversion of model imagery into video-based visualizations.
* Integration of early warning information from meteorological data.
* Implementation of browser-based text-to-speech for early warning information.
* Centralization of multiple maritime weather information sources into one dashboard interface.

The resulting dashboard can serve as a supporting visualization tool for maritime weather information and disaster mitigation activities within the operational area of the BMKG maritime meteorological station.

## Technologies

### Programming & Web Development

* Python
* Flask
* HTML
* CSS
* JavaScript

### Data Processing & Visualization

* Pandas
* NumPy
* Matplotlib

### Meteorological Data & Processing

* Automatic Weather Station (AWS)
* Himawari satellite imagery
* Cloud Cluster processing using GrADS
* Maritime weather model imagery

### Other

* Git
* GitHub
* Web Speech API

## Project Structure

```text
bmkg-maritime-weather-dashboard/
│
├── README.md
├── appp.py
├── requirements.txt
├── .gitignore
│
├── static/
│   ├── arus.mp4
│   ├── aws.png
│   ├── bg_awan.jpg
│   ├── citrastyle.css
│   ├── citra_angin.mp4
│   ├── citra_arus.mp4
│   ├── citra_gelombang.mp4
│   ├── cloud_cluster.mp4
│   ├── logo_bmkg.png
│   ├── normalize.css
│   ├── video_output.mp4
│   ├── wind_video.mp4
│   │
│   └── images/
│       └── peringatan2.png
│
└── templates/
    └── fix.html
```

Operational datasets are stored locally and are not included in the public repository.

## Data and Privacy

The original project used operational meteorological data obtained during the internship period.

The following types of operational data are not included in the public repository:

* AWS observation datasets
* Early warning datasets
* Other restricted operational data

These files are excluded from version control to avoid exposing operational or restricted data.

The repository therefore focuses on demonstrating the dashboard architecture, data processing workflow, visualization approach, and web application implementation.

## How to Run

### 1. Clone the Repository
```text
git clone https://github.com/MohAdityaSirojulHilmi/bmkg-maritime-weather-dashboard.git
cd bmkg-maritime-weather-dashboard
```

### 2. Create a Virtual Environment
```text
python -m venv venv
```
Activate the environment on Windows:
```text
venv\Scripts\activate
```

### 3. Install Dependencies
```text
pip install -r requirements.txt
```

### 4. Prepare Local Data

Place the required operational data files in the project directory.

These files are intentionally not included in the public repository.

### 5. Run the Application
```text
python appp.py
```

The Flask application will run locally at:
```text
http://127.0.0.1:5000
```

## Dashboard Preview

Screenshots of the dashboard interface can be added to this section.

Future improvements may include adding selected screenshots or demonstration images to provide a visual overview of the dashboard.

## Research / Internship Context

This project was developed as part of an internship project at the BMKG Maritime Meteorological Station Perak II, Surabaya.

The project combines meteorological data processing, satellite and model imagery visualization, and web application development to support the presentation of maritime weather information.

## Disclaimer

This repository is a portfolio and development representation of the dashboard project.

The original operational datasets and restricted data sources used during the internship are not included in this public repository.

The dashboard should not be considered an official BMKG operational system unless explicitly authorized by the relevant institution.

## Author

Moh. Aditya Sirojul Hilmi

Bachelor of Mathematics

Developed during an internship at BMKG Maritime Meteorological Station Perak II, Surabaya.




   
