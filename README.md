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
