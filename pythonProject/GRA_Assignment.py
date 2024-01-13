# importing packages

import json  # For reading JSON file
import socket  # To get the IP Address of the domain
import matplotlib.pyplot as plt  # To enable the visual representation of data
from multiprocessing import Pool, freeze_support  # To enable the parallel programming
import pandas as pd  # To read the CSV file
from flatten_json import flatten  # To enable the flattening functionality

# Reading the response.json file from the local
# Loading the nested json data
data = open('response.json', encoding="utf8")
un_flat_json = json.load(data)
print("Json file loaded from directory.")

# Flattening the raw json file completely
flat_json = flatten(un_flat_json)
print("Flattened the Json file.")

# Storing the information in the CSVFile with
# columns names as Notices and Infringing_urls
with open('CSVFile.csv', 'w', encoding="utf-8") as f:
    f.write("Notices,Infringing_urls\n")
    for key in flat_json.keys():  # Loop runs as many as keys available
        f.write("%s,%s\n" % (key, flat_json[key]))  # Each row corresponding to single infringing url
print("CSVFile.csv file generated with column names as Notices and Infringing_urls.")

print("Generating the CSV_Domain_IPAddress.csv file...")
# Getting the Domain name and IPAddress and storing in another CSV file
# Creating a new CSV_Domain_IPAddress.csv file to save the domain and IP address
count = 0
with open('CSV_Domain_IPAddress.csv', 'w', encoding="utf-8") as f:
    f.write("Domain,IPAddress\n")  # Column names in .csv file
    for key, value in flat_json.items():
        try:
            strVal = str(key)
            if "infringing_urls" not in strVal:  # Checking for only keys which has string 'infringing_urls'
                continue
            domain = value.split('/')  # Variable 1: To store the domain of the URL
            ipAddress = socket.gethostbyname(str(domain[2]))  # Variable 2: To store the ipAddress of the URL

            f.write("%s,%s\n" % (domain[2], ipAddress))   # Getting the 2nd Index value which the domain name

            #  Checking for the count of the rows that we are interested to load into CSV_Domain_IPAddress.csv file
            if count == 1000:
                break
            count = count + 1
        except Exception:
            pass
print("CSV_Domain_IPAddress.csv file generated with column names as Domain and IPAddress.")

# Getting the CSV data in the dataframe format to do the operations on the data
df = pd.read_csv("CSV_Domain_IPAddress.csv")

print("")
print("\033[1mSummarization 1: Top 5 names\033[1m")
# Summarization 1: Calculate the frequency of each domain name
# and print the top 5 most common names
name_counts = df['Domain'].value_counts()
# Get the top 5 most common names
top_5_names = name_counts.head(5)
print(top_5_names)

print("")
print("\033[1mSummarization 2: Group by domain and ip address\033[1m")
# Summarization 2: Group data by domain, ipaddress and print the count
url_distribution = df.groupby('Domain').size().reset_index(name='IPAddress')
print("A plot will be displayed to the right.")

# Plotting the domain distribution
plt.bar(url_distribution['Domain'], url_distribution['IPAddress'])
plt.xlabel('Domain')
plt.ylabel('IPAddress')
plt.title('URL Distribution')
plt.show()

print("")
print("\033[1mSummarization 3: Convert the proportions into percentages\033[1m")
# Summarization 3: Domain Distribution - convert the proportions into percentages
domain_distribution = df['Domain'].value_counts(normalize=True) * 100
print(domain_distribution)

"""
# Function to convert a JSON object to a DataFrame row
def json_to_dataframe_row(json_obj):
    return pd.DataFrame([json_obj])


# Parallelize the code using at least 4 cpus
# Number of CPUs to use
num_cpus = 4

# Parallelized the code using at least 4 cpus.
# The if __name__ == '__main__': block is used
# because when \ script is turned into an executable,
# the entire script is executed again as a separate process
if __name__ == '__main__':
    freeze_support()  # to ensure multiprocessing works correctly on windows
    with Pool(processes=num_cpus) as pool:
        dfs = pool.map(json_to_dataframe_row, flat_json)
    df = pd.concat(dfs, ignore_index=True)
"""