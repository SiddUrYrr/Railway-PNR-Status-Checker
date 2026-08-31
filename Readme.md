# 🚆 Railway PNR Status Checker

A simple Python application to check the status of an Indian Railways PNR using a RapidAPI-powered Railway PNR Status API.

## Features

* Check the status of any valid 10-digit PNR.
* Simple web interface using Streamlit.
* Uses the `requests` library.
* Easy to enter API credentials via the web UI.

## Requirements

* Python 3.8+
* `requests`
* `streamlit`

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/SiddUrYrr/Railway-PNR-Status-Checker.git
cd Railway-PNR-Status-Checker
```

## Usage

Run the script using Streamlit:

```bash
streamlit run pnr_status.py
```

This will open the web application in your default browser. Enter your RapidAPI key and the 10-digit PNR number, then click "Check Status".

## Disclaimer

This project uses a third-party Railway PNR Status API. Data availability, accuracy, and uptime depend on the API provider.
