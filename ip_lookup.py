import pandas as pd
import ipinfo
import sys
from time import sleep
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_ip_info(ip_list, access_token):
    # Initialize ipinfo handler
    handler = ipinfo.getHandler(access_token)
    
    # Store results
    results = []
    
    for ip in ip_list:
        try:
            # Get IP details
            details = handler.getDetails(ip)
            
            # Extract relevant information
            ip_data = {
                'IP': ip,
                'City': details.city if hasattr(details, 'city') else 'N/A',
                'Region': details.region if hasattr(details, 'region') else 'N/A',
                'Country': details.country_name if hasattr(details, 'country_name') else 'N/A',
                'Organization': details.org if hasattr(details, 'org') else 'N/A',
                'Latitude': details.latitude if hasattr(details, 'latitude') else 'N/A',
                'Longitude': details.longitude if hasattr(details, 'longitude') else 'N/A'
            }
            results.append(ip_data)
            print(f"Processed: {ip}")
            
            # Small delay to avoid rate limiting
            sleep(0.5)
            
        except Exception as e:
            print(f"Error processing {ip}: {str(e)}")
            results.append({
                'IP': ip,
                'City': 'Error',
                'Region': 'Error',
                'Country': 'Error',
                'Organization': 'Error',
                'Latitude': 'Error',
                'Longitude': 'Error'
            })
    
    return pd.DataFrame(results)

def main():
    # Configuration
    INPUT_FILE = 'ips.xlsx'  # Your input spreadsheet
    OUTPUT_FILE = 'ip_locations.xlsx'  # Where results will be saved
    IP_COLUMN = 'IP'  # Column name containing IPs in your spreadsheet
    
    # Get the access token from environment variables
    ACCESS_TOKEN = os.getenv('IPINFO_TOKEN')
    
    if not ACCESS_TOKEN:
        print("Error: IPINFO_TOKEN not found in .env file")
        sys.exit(1)
    
    try:
        # Read the spreadsheet
        df = pd.read_excel(INPUT_FILE)
        
        # Check if IP column exists
        if IP_COLUMN not in df.columns:
            print(f"Error: Column '{IP_COLUMN}' not found in spreadsheet")
            sys.exit(1)
        
        # Get unique IP addresses
        ip_list = df[IP_COLUMN].dropna().unique()
        
        print(f"Found {len(ip_list)} unique IP addresses to process")
        
        # Get IP information
        results_df = get_ip_info(ip_list, ACCESS_TOKEN)
        
        # Save results to new spreadsheet
        results_df.to_excel(OUTPUT_FILE, index=False)
        print(f"Results saved to {OUTPUT_FILE}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{INPUT_FILE}' not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Install required packages if not already installed
    try:
        import pandas
        import ipinfo
        import dotenv
    except ImportError:
        print("Installing required packages...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "openpyxl", "ipinfo", "python-dotenv"])
    
    main()
