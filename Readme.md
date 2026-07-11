# 🚆 Railway PNR Status Checker

A simple Python application to check the status of an Indian Railways PNR using a RapidAPI-powered Railway PNR Status API.

## Features

* Check the status of any valid 10-digit PNR.
* Simple command-line interface.
* Uses the `requests` library.
* Easy to configure using environment variables.
* Keeps API credentials out of the source code.

## Requirements

* Python 3.8+
* `requests`

Install the required dependency:

```bash
pip install requests
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/SiddUrYrr/Railway-PNR-Status-Checker.git
cd Railway-PNR-Status-Checker
```

## Usage

Run the script:

```bash
python pnr_status.py
```

Example:

```text
Enter PNR: 1234567890
```

## Example Output

```text
==================================================
PNR Status
==================================================
Train: Example Express
Train No: 12345
Journey Date: YYYY-MM-DD
From: Source Station
To: Destination Station

Passengers:
Passenger 1: WL 5 -> CNF/B2/35
```

## Disclaimer

This project uses a third-party Railway PNR Status API. Data availability, accuracy, and uptime depend on the API provider.

