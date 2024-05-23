import sys
import pandas as pd
import matplotlib.pyplot as plt
import yaml
from collections import Counter
"""
This program takes a log file as argument, filtered by status code, count
the numbers of each
status code, plot and saves a pie chart and a YAML file containing the
status codes and counts
"""
# check if an argument is given
if len(sys.argv) < 2:
    print("Please provide the filename to parse as an argument")
    exit(1)

# load the file
file = []
try:
    print(f"Try to load: {sys.argv[1]}")
    file = open(sys.argv[1], "r")
    print("Load successfully")
except:
    print(f"File not found: {sys.argv[1]}")
    exit(1)

# load the log file into a panda dataframe
df = pd.read_csv(file, sep=" ", header=None)
# remove unused columns
df = df.drop(df.columns[[0, 1, 2, 3, 4, 5, 7]], axis=1)
df.columns = ["status_code"]
status_codes = df['status_code'].values.tolist()

ordered_status_codes = Counter(status_codes)
ordered_status_codes = dict(ordered_status_codes)

# plot the pie chart with labels
plt.pie([float(v) for v in ordered_status_codes.values()],
        labels=[int(k) for k in ordered_status_codes.keys()],
        autopct="%1.2f%%")
plt.savefig("./statuscode.png")

# write the yaml file
with open("./result.yml", "w") as yaml_file:
    yaml.dump(ordered_status_codes, yaml_file)

print("Successfully saved pie chart and wrote result.yml")
