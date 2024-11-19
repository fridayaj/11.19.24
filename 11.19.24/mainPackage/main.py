# main.py

import os
from srcPackage.data_cleaner import DataCleaner

if __name__ == "__main__":
    # Specify the path relative to the root directory
    input_file = os.path.join(os.getcwd(), "Data", "fuelPurchaseData.csv")
    
    print("Starting data processing...")
    cleaner = DataCleaner(input_file)
    cleaner.process_data()
    print("Data processing is complete.")



