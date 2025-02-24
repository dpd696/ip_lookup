# IP Lookup Tool

This Python script reads IP addresses from an Excel spreadsheet, looks up their geolocation and public information using the [ipinfo.io](https://ipinfo.io/) API, and saves the results to a new Excel file.

## Prerequisites

- **Python 3**: Version 3.12+ (ships with Ubuntu 24.04).
- **Excel File**: An input file named `ips.xlsx` with a column labeled "IP" containing IP addresses.
- **ipinfo API Token**: A free token from [ipinfo.io](https://ipinfo.io/signup).

## Setup

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/dpd696/IP_Lookup.git
cd IP_Lookup
```

### 2. ipinfo API Token
A free token from [ipinfo.io](https://ipinfo.io/signup).
Open .env Replace abc123xyz789 with your actual token.

### 3. Create a Virtual Environment
Create a virtual environment (e.g., named venv):
```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment
Activate it:
```bash
source venv/bin/activate
```
Your prompt should change (e.g., (venv) $), indicating you’re in the virtual environment.

### 5. Install the Required Packages
Inside the virtual environment, install the packages:
```bash
pip install pandas openpyxl ipinfo
```
No sudo or --break-system-packages needed—PEP 668 doesn’t apply here.

### 6. Run the Script
Run your script within the virtual environment:
```bash
python ip_lookup.py
```
Note: It’s just python now, not python3, because the virtual environment’s python is the active one.

### 7. Deactivate When Done
When you’re finished, exit the virtual environment:
```bash
deactivate
```
