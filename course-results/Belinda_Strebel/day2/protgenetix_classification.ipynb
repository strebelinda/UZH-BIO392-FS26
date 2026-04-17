# Protgenetix Exercise 4
# Exercise 4. Download and interpret CNV frequency data
# Now download the CNV frequency table for:
# Example:
# Small cell carcinoma, NOS
# filter code: pgx:icdom-80413
# Tasks:
# download the frequency table
# inspect its shape
# inspect its columns
# Explain why the frequency table has a different shape from the sample table.
# what one row represents in the sample table
# what one row represents in the frequency table
# why these two tables cannot be merged row by row

#Exercise 1
import requests
import pandas as pd

url = "https://progenetix.org/beacon/biosamples"
params = {
    "filters": "pgx:icdom-80413",
    "limit": 5
}

response = requests.get(url, params=params)
data = response.json()
results = data["response"]["resultSets"][0]["results"]

df_api = pd.json_normalize(results)
df_api.head()



#Exercise 2
from io import StringIO

sampletable_url = "https://progenetix.org/services/sampletable/?filters=pgx:icdom-80413&limit=0"
response = requests.get(sampletable_url)
df_sampletable = pd.read_csv(StringIO(response.text), sep="\t")

print("Shape of sampletable DataFrame:", df_sampletable.shape)
print("Shape of API DataFrame (Exercise 1):", df_api.shape)

df_sampletable.head()
df_api.head()

# One difference is that the API returns nested JSON data, which needs flattening (json_normalize),
# whereas the sampletable service returns a pre-formatted tab-separated table that is easier to read directly into pandas.



# Exercise 3
print("Histological Diagnosis Label counts:")
print(df_sampletable["histological_diagnosis_label"].value_counts())
print("\nICD-O Morphology Label counts:")
print(df_sampletable["icdo_morphology_label"].value_counts())
print("\nICD-O Topography Label counts:")
print(df_sampletable["icdo_topography_label"].value_counts())

# histological_diagnosis_label: The general clinical name of the cancer (e.g., Small cell lung cancer).
# icdo_morphology_label: The specific microscopic appearance or cell type of the tumor (ICD-O 3 code description).
# icdo_topography_label: The anatomical site or organ where the tumor originated.



#Exercise 4
freq_url = "https://progenetix.org/services/intervalFrequencies/?output=pgxseg&filters=pgx:icdom-80413"
response = requests.get(freq_url)
df_freq = pd.read_csv(StringIO(response.text), sep="\t", comment="#")

print("Shape of frequency table:", df_freq.shape)
print("Columns:", df_freq.columns.tolist())

# A row in the sample table represents one biosample (metadata).
# A row in the frequency table represents one genomic interval (bin), here / usually 1Mb wide.
# They cannot be merged row-by-row because they describe different entities at different levels:
#   one is sample-centric metadata, the other is genome-centric aggregate statistics for a group.




# Classification Exercise 3
# Exercise 3. Inspect one informative bin
# Choose one bin from the interpretation table.
#Tasks:
# write down whether that bin favors glioblastoma or ovarian HGSC
# inspect the histogram for that bin
# open the Progenetix collation plot link and describe whether the broad group-level pattern seems consistent with the model result



