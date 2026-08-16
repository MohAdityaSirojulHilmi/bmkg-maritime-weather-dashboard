# BMKG Tanjung Perak Real-Time Weather Monitoring Dashboard

A real-time maritime weather monitoring dashboard developed during an internship at BMKG Tanjung Perak using Python and Flask, integrating AWS observation data and Himawari satellite imagery.

## Project Overview

This project presents a web-based dashboard for monitoring maritime weather conditions at BMKG Tanjung Perak.

The dashboard integrates meteorological observation data from an Automatic Weather Station (AWS) with satellite imagery to provide a visual representation of maritime weather conditions.

The system was developed to support weather monitoring and analysis by presenting several important weather parameters through an interactive dashboard interface.

## Dashboard Features

The dashboard provides visualization of several maritime weather parameters, including:

- Wind speed
- Wind direction
- Temperature
- Relative humidity
- Atmospheric pressure
- Water level
- Himawari satellite imagery
- Maritime weather model imagery
- Weather warning information

## System Workflow

The general workflow of the dashboard is:

AWS Observation Data
        │
        ▼
   Data Processing
   (Python / Pandas)
        │
        ▼
    Data Visualization
     (Matplotlib)
        │
        ├──────────────► Weather Dashboard
        │
        ▼
Himawari Satellite Imagery
        │
        ▼
   Flask Web Application

## Technologies

- Python
- Flask
- Pandas
- NumPy
- Matplotlib
- HTML
- CSS
- Himawari Satellite Imagery
- Automatic Weather Station (AWS) Data

## Data

The original dashboard used meteorological observation data obtained from BMKG operational sources during the internship period.

The data included observations from an Automatic Weather Station (AWS), such as:

- Wind speed
- Wind direction
- Temperature
- Relative humidity
- Atmospheric pressure
- Water level

Himawari satellite imagery and maritime weather model imagery were also used as part of the dashboard visualization.

Due to data access and usage considerations, the original operational datasets and restricted data sources are not included in this public repository.

## Dashboard Preview

The dashboard interface includes displays of AWS observations, satellite imagery, weather model imagery, and maritime weather warnings.

Dashboard screenshots can be added to this section.

## Research Context

This project was developed as part of an internship research/project activity at BMKG Tanjung Perak, Surabaya.

The dashboard was developed to support the visualization and monitoring of maritime weather conditions by combining AWS observation data and Himawari satellite imagery in a web-based interface.

## Project Structure

The repository contains the main components required to demonstrate the dashboard development and its workflow.

bmkg-maritime-weather-dashboard/
│
├── README.md
├── app.py
├── templates/
├── static/
└── ...

Some original BMKG data files and operational data sources are not included in this repository due to data access and usage considerations.

## Disclaimer

The data used in the original development were obtained from BMKG operational sources during the internship period.

For privacy, access, and data usage considerations, the original operational datasets and restricted data sources are not included in this public repository.

This repository focuses on demonstrating the development approach, data processing workflow, visualization techniques, and dashboard implementation.

   
