import pandas as pd
import re

# Raw data as a single string
data = """
 Bajaj Hindusthan Sugar Ltd 09/21/2023 500.0000 25.76 12882.4509/25/2023 500.0000 26.74 13367.85 0.00 25.76 0.0 485.4 0.0 Bajaj Hindusthan Sugar Ltd 10/04/20231000.0000 25.72 25724.5010/04/20231000.0000 26.73 26725.30 0.00 25.72 1000.8 1000.8 0.0 Bajaj Hindusthan Sugar Ltd 09/29/20231000.0000 26.22 26216.7010/16/20231000.0000 27.04 27035.00 0.00 26.22 0.0 818.3 0.0 Bajaj Hindusthan Sugar Ltd 10/05/2023 200.0000 25.31 5062.9210/18/2023 200.0000 27.48 5496.76 0.00 25.31 0.0 433.84 0.0 Bajaj Hindusthan Sugar Ltd 10/18/2023 800.0000 26.83 21460.7210/18/2023 800.0000 27.53 22020.16 0.00 26.83 559.44 559.44 0.0 Bajaj Hindusthan Sugar Ltd 10/05/2023 800.0000 25.31 20251.6811/01/2023 800.0000 27.13 21707.76 0.00 25.31 0.0 1456.08 0.0 Bajaj Hindusthan Sugar Ltd 10/23/20231000.0000 25.31 25314.8011/01/20231000.0000 27.13 27134.70 0.00 25.31 0.0 1819.9 0.0 Bajaj Hindusthan Sugar Ltd 10/23/20231000.0000 25.46 25464.8011/01/20231000.0000 27.13 27134.70 0.00 25.46 0.0 1669.9 0.0 Bajaj Hindusthan Sugar Ltd 12/12/20231000.0000 28.37 28372.0012/18/20231000.0000 30.28 30277.20 0.00 28.37 0.0 1905.2 0.0 Bajaj Hindusthan Sugar Ltd 12/18/20231000.0000 29.73 29725.8012/18/20231000.0000 30.33 30325.10 0.00 29.73 599.3 599.3 0.0 Bajaj Hindusthan Sugar Ltd 12/13/20231000.0000 27.87 27870.8001/29/20241000.0000 30.53 30526.50 0.00 27.87 0.0 2655.7 0.0 Bajaj Hindusthan Sugar Ltd 12/19/20231000.0000 29.22 29224.0001/29/20241000.0000 30.53 30526.50 0.00 29.22 0.0 1302.5 0.0 Bajaj Hindusthan Sugar Ltd 12/20/2023 500.0000 28.67 14336.6001/29/2024 500.0000 30.53 15263.25 0.00 28.67 0.0 926.65 0.0 Bajaj Hindusthan Sugar Ltd 12/20/20231000.0000 28.67 28673.2001/30/20241000.0000 30.63 30626.30 0.00 28.67 0.0 1953.1 0.0 Bajaj Hindusthan Sugar Ltd 12/20/2023 500.0000 27.57 13785.1001/30/2024 500.0000 30.63 15313.15 0.00 27.57 0.0 1528.05 0.0 Bajaj Hindusthan Sugar Ltd 12/20/20231000.0000 27.57 27570.2001/30/20241000.0000 31.08 31075.20 0.00 27.57 0.0 3505.0 0.0 Bank of India 02/24/2022 200.0000 44.06 8812.5011/13/2023 200.0000107.44 21488.30 0.00 44.06 0.0 0.0 12675.8 Bank of Maharashtra 10/04/2023 400.0000 49.37 19749.5610/05/2023 400.0000 48.83 19533.00 0.00 49.37 0.0-216.56 0.0 Central Bank of India 12/14/2022 500.0000 39.95 19975.4009/08/2023 500.0000 39.41 19702.55 0.00 39.95 0.0-272.85 0.0 Central Bank of India 12/16/2022 500.0000 37.55 18772.7009/08/2023 500.0000 39.41 19702.55 0.00 37.55 0.0 929.85 0.0 Central Bank of India 12/16/2022 500.0000 37.55 18772.7009/11/2023 500.0000 39.95 19976.90 0.00 37.55 0.0 1204.2 0.0 Central Bank of India 12/22/2022 400.0000 33.23 13293.4409/11/2023 400.0000 39.95 15981.52 0.00 33.23 0.0 2688.08 0.0 Central Bank of India 12/22/2022 100.0000 33.23 3323.3609/11/2023 100.0000 39.91 3990.95 0.00 33.23 0.0 667.59 0.0
"""

# Split data into lines
lines = data.strip().split("\n")

# Initialize list to hold structured data
structured_data = []

# Pattern to detect dates and split entries
pattern = re.compile(r'(\d{2}/\d{2}/\d{4})')

for line in lines:
    # Check if line starts with company name
    if not re.match(r'\d', line.strip()):
        # Company name line, append to next entry
        company = line.strip()
        continue
    
    # Split by date patterns to handle breaks
    parts = pattern.split(line)
    parts = [p.strip() for p in parts if p.strip()]
    
    # Reconstruct structured line
    company_data = [company] + parts
    
    # Append to structured data
    structured_data.append(company_data)
    print(structured_data)

# Define column names based on structure
columns = [
    "Company", "Date 1", "Quantity 1", "Price 1", "Value 1", "Date 2", "Quantity 2", "Price 2", "Value 2",
    "Unknown 1", "Price 3", "Unknown 2", "Unknown 3", "Unknown 4"
]

# Create DataFrame
df = pd.DataFrame(structured_data, columns=columns)

# Save to CSV
df.to_csv('stock_data.csv', index=False)
