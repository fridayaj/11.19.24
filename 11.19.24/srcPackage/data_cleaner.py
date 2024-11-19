# data_cleaner.py

import csv
import os
from srcPackage.utils import round_price, remove_duplicates, write_csv
from srcPackage.api_handler import fetch_zip_code

class DataCleaner:
    def __init__(self, input_file):
        # Check if the input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"The input file '{input_file}' does not exist.")
        self.input_file = input_file
        self.cleaned_data = []
        self.anomalies = []

    def process_data(self):
        print(f"Processing data from {self.input_file}...")

        # Open the CSV file and read the data
        with open(self.input_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        # Step 1: Remove duplicates
        print("Removing duplicate rows...")
        rows = remove_duplicates(rows)

        # Process each row
        for row in rows:
            # Step 2: Round Gross Price
            row["Gross Price"] = round_price(row.get("Gross Price"))

            # Step 3: Handle anomalies (e.g., "Pepsi" purchases)
            if "Pepsi" in row.get("Fuel Type", "").lower():  # Checking for anomalies
                print(f"Anomaly detected: {row}")  # Debugging - Print detected anomalies
                self.anomalies.append(row)  # Add to anomalies list
                continue  # Skip this row and don't add to cleaned data

            # Step 4: Handle missing zip codes in the address
            if not self._has_zip_code(row.get("Full Address")):
                row["Full Address"] = self._add_zip_code(row["Full Address"])

            self.cleaned_data.append(row)

        # Step 5: Write cleaned data and anomalies to files
        self._write_to_files()

        print("Data manipulation completed successfully.")

    def _has_zip_code(self, address):
        # Check if the address contains a zip code (any number)
        return any(char.isdigit() for char in address)

    def _add_zip_code(self, address):
        # Extract city from address and fetch a zip code using the API
        city = self._extract_city(address)
        zip_code = fetch_zip_code(city)  # Get zip code from the API
        return f"{address}, {zip_code}"

    def _extract_city(self, address):
        # Logic to extract city from the address (assuming address format "Street, City")
        return address.split(",")[1].strip()

    def _write_to_files(self):
        # Ensure the 'Data' folder exists
        os.makedirs("Data", exist_ok=True)

        # Write cleaned data to 'Data/cleanedData.csv'
        print("Writing cleaned data to 'Data/cleanedData.csv'...")
        write_csv("Data/cleanedData.csv", self.cleaned_data)

        # Write anomalies to 'Data/dataAnomalies.csv'
        print("Writing anomalies to 'Data/dataAnomalies.csv'...")
        if self.anomalies:
            write_csv("Data/dataAnomalies.csv", self.anomalies)
        else:
            print("No anomalies detected.")






"""
import csv
import os
from srcPackage.utils import round_price, remove_duplicates, write_csv
from srcPackage.api_handler import fetch_zip_code

class DataCleaner:
    def __init__(self, input_file):
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"The input file '{input_file}' does not exist.")
        self.input_file = input_file
        self.cleaned_data = []
        self.anomalies = []

    def process_data(self):
        print(f"Processing data from {self.input_file}...")
    
        with open(self.input_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        # Step 1: Remove duplicates
        print("Removing duplicate rows...")
        rows = remove_duplicates(rows)

        # Process each row
        for row in rows:
            # Step 2: Round Gross Price
            row["Gross Price"] = round_price(row.get("Gross Price"))

            # Step 3: Handle anomalies (e.g., Pepsi purchases)
            if "Pepsi" in row.get("Fuel Type", "").lower():
                print(f"Anomaly detected: {row}")  # Debug print to verify anomaly detection
                self.anomalies.append(row)
                continue  # Skip this row from cleaned data

            # Step 4: Handle missing zip codes
            if not self._has_zip_code(row.get("Full Address")):
                row["Full Address"] = self._add_zip_code(row["Full Address"])

            self.cleaned_data.append(row)

        # Step 5: Write anomalies and cleaned data to separate files
        self._write_to_files()
    
        print("Data manipulation completed successfully.")

    
    def _has_zip_code(self, address):
        return any(char.isdigit() for char in address)

    def _add_zip_code(self, address):
        # Extract city and fetch a zip code
        city = self._extract_city(address)
        zip_code = fetch_zip_code(city)
        return f"{address}, {zip_code}"

    def _extract_city(self, address):
        # Logic to extract city from the address
        return address.split(",")[1].strip()

    def _write_to_files(self):
        os.makedirs("Data", exist_ok=True)
        
        print("Writing cleaned data to 'Data/cleanedData.csv'...")
        write_csv("Data/cleanedData.csv", self.cleaned_data)

        print("Writing anomalies to 'Data/dataAnomalies.csv'...")
        write_csv("Data/dataAnomalies.csv", self.anomalies)
"""

